# Raspberry Pi motion sensitive camera
# this program is started when the wifi interface is up and running 

# import required libraries
import os, picamera, sys, time
import RPi.GPIO as GPIO
import subprocess

# GPIO pin for the PIR sensor
PIR_GPIO_PIN = 23 

# camera mode
PHOTO = "Photos"
VIDEO = "Videos"

# location on raspberry pi to store photos and videos
LOCAL_DIRECTORY = "/home/pi/python_programs/camera_output/"

# location of the program used to upload files to dropbox
DROPBOX_COMMAND = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh"

# video recording time in seconds
RECORDING_TIME = 15

# time to wait after taking photo or video in seconds
WAIT_TIME = 10

# generate a file name based on the local date and time 
# year-month-day-hour-minutes-seconds-timezone
def generate_file_name():
	return time.strftime("%Y-%m-%d-%H-%M-%S-%Z", time.localtime())     # e.g., 2014-09-14-15-23-45-PST

# when motion is detected, take a photo or record a video
# based on what mode was specified by the user
def motion_detected(pir_sensor):
	fname = LOCAL_DIRECTORY + generate_file_name()
	print "rpi-ms-camera: Motion detected!"	
	if camera_mode == PHOTO:
		fname = fname + ".jpg"
		snap_photo(fname)
	else:
		fname = fname + ".h264"
		record_video(fname, RECORDING_TIME)	
	upload_to_dropbox(fname)
	os.remove(fname)
	print "rpi-ms-camera: " + fname + " deleted."

# take a photo and store it a file with a unique name
# based on the current date and time	
def snap_photo(file_name):
	camera.resolution = (1024, 768)	
	camera.capture(file_name)
	print "rpi-ms-camera: Photo taken."

# record video for the specified number of seconds and
# store it in a file with a unique name based on the
# current date and time	
def record_video(file_name, rec_time):
	camera.resolution = (650,480)		
	camera.start_recording(file_name)  
	print "rpi-ms-camera: Video recording started."
	camera.wait_recording(rec_time)
	camera.stop_recording()
	print "rpi-ms-camera: Video recording stopped."

# upload the file to the specified folder in dropbox 
# and delete the file after the upload completes
def upload_to_dropbox(local_file_name):	
	dropbox_file_name = os.path.basename(local_file_name)
	print "rpi-ms-camera: Uploading " + dropbox_file_name + " to Dropbox."
	upload_command = DROPBOX_COMMAND + ' upload ' + local_file_name + ' ' + dropbox_file_name
	# print "rpi-ms-camera: " + upload_command	  
	subprocess.call([upload_command], shell=True)

# create a file with the IP address of the raspberry pi
# and upload it to dropbox so the user can easily get the
# address if ssh is needed to connect to it
def upload_ip_address():
	print "rpi-ms-camera: Uploading IP address to Dropbox."
	ip_file_name = LOCAL_DIRECTORY + "IP-" + generate_file_name() + ".txt"
	ip_command = "hostname -I > " + ip_file_name
	subprocess.call([ip_command], shell=True)
	upload_to_dropbox(ip_file_name)
	os.remove(ip_file_name)

# call the dropbox-uploader script for the first time to get it to 
# ask the user for the API keys needed to configure the uploader.
# this is used as part of the setup process
def first_time_config():
	subprocess.call([DROPBOX_COMMAND], shell=True)
	
# call the dropbox uploader command to make sure it's working properly
# by uploading a file with the IP address of the Raspberry Pi.
# this is used as part of the setup process
def test_dropbox():
	print "rpi-ms-camera: Testing Dropbox connection."
	upload_ip_address()
	print "rpi-ms-camera: Check your Dropbox app folder for the uploaded file"
	
# Main program

# the switch specified on the command determines whether 
# a photo or video should be captured and uploaded
# the program can be started one of three ways:
#   
#   'sudo python rpi-ms-camera.py -p'         snaps photos
#   'sudo python rpi-ms-camera.py -v'         capture video 
#   'sudo python rpi-ms-camera.py -firsttime' runs first time configuration 
#   'sudo python rpi-ms-camera.py -test'      tests to make sure upload is working

# determine what command line parameters were specified
if len(sys.argv) > 1:
	if sys.argv[1] == "-p":
		camera_mode = PHOTO
	elif sys.argv[1] == "-v":
		camera_mode = VIDEO
	elif sys.argv[1] == "-firsttime":
		first_time_config()
		sys.exit()
	elif sys.argv[1] == '-test':
		test_dropbox()
		sys.exit()
	else:
		print "Invalid option specified"
		sys.exit()
else:
	print "Valid options are:"
	print "  -p          Snap photos when motion is detected"
	print "  -v          Record video when motion is detected"
	print "  -firsttime  Run to configure the Dropbox application"
	print "  -test       Used to test the connection to Dropbox"
	sys.exit()

print "rpi-ms-camera: Raspberry Pi motion sensitive camera started."
print "rpi-ms-camera: " + camera_mode + " will be captured when motion is detected."

# setup raspberry pi camera
camera = picamera.PiCamera()
camera.hflip = True
camera.vflip = True

# setup GPIO pin for the PIR (motion) sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_GPIO_PIN, GPIO.IN)

# upload the IP address of the Raspberry Pi to Dropbox so the
# user can use "ssh" to connect to it if needed 
upload_ip_address()

# main loop to detect motion and snap pictures or record videos
while True:
	try:
		print "rpi-ms-camera: Waiting for motion."
		GPIO.wait_for_edge(PIR_GPIO_PIN, GPIO.RISING)
		motion_detected(PIR_GPIO_PIN)
		print "rpi-ms-camera: Sleeping for " + str(WAIT_TIME) + " seconds."
		time.sleep(WAIT_TIME)
	except:
		print "rpi-ms-camera: Stopping due to keyboard interrupt."
		camera.close()
		GPIO.cleanup()
		break
