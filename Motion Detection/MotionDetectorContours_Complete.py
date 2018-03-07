#------------------------------------------------------------------- LIBRARIES BEGIN --------------------------------------------------------------------------

import cv2.cv as cv
from datetime import datetime
import time
import smtplib
import subprocess  #dropbox
import os  #dropbox

#------------------------------------------------------------------- LIBRARIES END --------------------------------------------------------------------------

#------------------------------------------------------------------- DROPBOX BEGIN --------------------------------------------------------------------------
DROPBOX_COMMAND = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh"  #dropbox

def upload_to_dropbox(local_file_name):   #dropbox
        
            dropbox_file_name = os.path.basename(local_file_name)
            print "MotionDetectionContours: Uploading " + dropbox_file_name + " to Dropbox."  #dropbox
            upload_command = DROPBOX_COMMAND + ' upload ' + local_file_name + ' ' + dropbox_file_name
            # print "rpi-ms-camera: " + upload_command	    #dropbox
            subprocess.call([upload_command], shell=True)  #dropbox

#------------------------------------------------------------------- DROPBOX END --------------------------------------------------------------------------            
class MotionDetectorAdaptative():
    
    def onChange(self, val): #callback when the user change the detection threshold
        self.threshold = val
    
    def __init__(self,threshold=100, doRecord=True, showWindows=True):
        self.writer = None
        self.font = None
        self.doRecord=doRecord #Either or not record the moving object
        self.show = showWindows #Either or not show the 2 windows
        self.frame = None
    
        self.capture=cv.CaptureFromCAM(0)
        self.frame = cv.QueryFrame(self.capture) #Take a frame to init recorder
        
        self.gray_frame = cv.CreateImage(cv.GetSize(self.frame), cv.IPL_DEPTH_8U, 1)
        self.average_frame = cv.CreateImage(cv.GetSize(self.frame), cv.IPL_DEPTH_32F, 3)
        self.absdiff_frame = None
        self.previous_frame = None
        
        self.surface = self.frame.width * self.frame.height
        self.currentsurface = 0
        self.currentcontours = None
        self.threshold = threshold
        self.isRecording = False
        self.trigger_time = 0 #Hold timestamp of the last detection
        self.captureCounter = 0 

        
        if showWindows:
            cv.NamedWindow("Image")
            cv.CreateTrackbar("Detection treshold: ", "Image", self.threshold, 100, self.onChange)
        

#------------------------------------------------------------------- COMPUTER VISION BEGIN --------------------------------------------------------------------------         
    
    def processImage(self, curframe):
            cv.Smooth(curframe, curframe) #Remove false positives
            
            if not self.absdiff_frame: #For the first time put values in difference, temp and moving_average
                self.absdiff_frame = cv.CloneImage(curframe)
                self.previous_frame = cv.CloneImage(curframe)
                cv.Convert(curframe, self.average_frame) #Should convert because after runningavg take 32F pictures
            else:
                cv.RunningAvg(curframe, self.average_frame, 0.05) #Compute the average
            
            cv.Convert(self.average_frame, self.previous_frame) #Convert back to 8U frame
            
            cv.AbsDiff(curframe, self.previous_frame, self.absdiff_frame) # moving_average - curframe
            
            cv.CvtColor(self.absdiff_frame, self.gray_frame, cv.CV_RGB2GRAY) #Convert to gray otherwise can't do threshold
            cv.Threshold(self.gray_frame, self.gray_frame, 50, 255, cv.CV_THRESH_BINARY)

            cv.Dilate(self.gray_frame, self.gray_frame, None, 15) #to get object blobs
            cv.Erode(self.gray_frame, self.gray_frame, None, 10)
            
#------------------------------------------------------------------- COMPUTER VISION END --------------------------------------------------------------------------
   
    def somethingHasMoved(self):
        
        # Find contours
        storage = cv.CreateMemStorage(0)
        contours = cv.FindContours(self.gray_frame, storage, cv.CV_RETR_EXTERNAL, cv.CV_CHAIN_APPROX_SIMPLE)

        self.currentcontours = contours #Save contours

        while contours: #For all contours compute the area
            self.currentsurface += cv.ContourArea(contours)
            contours = contours.h_next()
#------------------------------------------------------------------- COMPUTER VISION BEGIN --------------------------------------------------------------------------       
        avg = (self.currentsurface*100)/self.surface #Calculate the average of contour area on the total size
        self.currentsurface = 0 #Put back the current surface to 0
          
        if avg > self.threshold:
            return True
        else:
            return False
#------------------------------------------------------------------- COMPUTER VISION END --------------------------------------------------------------------------  
    def initRecorder(self): #Create the recorder
        codec = cv.CV_FOURCC('M', 'J', 'P', 'G')
        self.writer=cv.CreateVideoWriter(datetime.now().strftime("/home/pi/python_programs/camera_output/"+"%b-%d_%H_%M_%S")+".wmv", codec, 5, cv.GetSize(self.frame), 1)
        #FPS set to 5 because it seems to be the fps of my cam but should be ajusted to your needs
        self.font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 2, 8) #Creates a font
        
         # Comments:
        """ By changing threshold in def __init__(..,self.threshold = 15,...) you control sensitivity of image capture"""
        """e.g threshold = 15 is more sensitive in threshold = 25"""
        # end

        self.captureCounter += 1 
        img = cv.QueryFrame(self.capture) 
        filename = "capture"+str(self.captureCounter)
        file = "/home/pi/python_programs/camera_output/"  + filename + ".png" 
        cv.SaveImage(file,img)
#------------------------------------------------------------------- DROPBOX BEGIN --------------------------------------------------------------------------        
       # upload_to_dropbox(file)    #dropbox
#------------------------------------------------------------------- DROPBOX END --------------------------------------------------------------------------

    def run(self):
        started = time.time()
        while True:
            
            currentframe = cv.QueryFrame(self.capture)
            instant = time.time() #Get timestamp of the frame
            
            self.processImage(currentframe) #Process the image
            
            if not self.isRecording:
                if self.somethingHasMoved():
                    self.trigger_time = instant #Update the trigger_time
                    if instant > started + 0:#Wait 5 second after the webcam start for luminosity adjusting etc..
                        print "Something is moving !"
#------------------------------------------------------------------- EMAIL BEGIN --------------------------------------------------------------------------
##                        content = 'Your House is Compromised ... run nigga run'  # email                       
##                        mail = smtplib.SMTP('smtp.gmail.com',587)  # email
##                        mail.ehlo()  # email
##                        mail.starttls()  # email
##                        mail.login('academic.team2016@gmail.com','sanmplouzaki')  # email
##
##                        mail.sendmail('academic.team2016@gmail.com','academic.team2016@gmail.com',content)  # email
##                        mail.close()     # email
#------------------------------------------------------------------- EMAIL END --------------------------------------------------------------------------

                        self.initRecorder() 
                        
                        if self.doRecord: #set isRecording=True only if we record a video
                            self.isRecording = True  # rasfasdsd---------------------------------------------------------------------  DANGER
                cv.DrawContours (currentframe, self.currentcontours, (0, 0, 255), (0, 255, 0), 1, 2, cv.CV_FILLED)
            else:
                if instant >= self.trigger_time +10: #Record during 10 seconds
                    print "Stop recording"
                    self.isRecording = False
                    time.sleep(8)
            
            if self.show:
                cv.ShowImage("Image", currentframe)                
            c=cv.WaitKey(1) % 0x100
            if c==27 or c == 10: #Break if user enters 'Esc'.
                break   
        
if __name__=="__main__":
    detect = MotionDetectorAdaptative(doRecord=True)
    detect.run()
