<h1>Home Automation:Automated Curtain controlled from smartphone including motion and light sensor</h1>

<h2>How to use a photoresistor:</h2>

A photoresistor or photocell is a light-controlled variable resistor. The resistance of a photoresistor decreases with increasing incident light intensity. A photoresistor can be applied in light-sensitive detector circuits, and light- and dark-activated switching circuits. It's also called light-dependent resistor (LDR). 

For our circuit we will need: 

                             1.Arduino uno
                             2.Breadboard
                             3.LED
                             4.Photoresistror
                             5.Resistor

![alt text](https://github.com/Nikoanas/Smart-House/blob/master/curtains/curtains.jpg)

<h2>Let's connect our motion sensor(Ultrasonic)</h2>
                            Parts List

                           1 Arduino uno
                           1 SR04 Ultrasonic Sensor
                           1 breadboard
                           4 jumper Wires 
                     
    You Need 4 Jumper wires to conect the SR04 Ultrasonic Sensor to the Arduino:
                                                                -1 From the SR04 VCC pin to the Arduino 5v
                                                                -1 From the SR04 GND pin to the Arduino GND
                                                                -1 From the SR04 TRG pin to the Arduino Digital pin 12
                                                                -1 From the SR04 ECHO pin to the Arduino Digital pin 11 

<h2>About The Stepper</h2>
                              
![alt text](https://github.com/Nikoanas/Smart-House/blob/master/curtains/curtains_driver.png)

![alt text](https://github.com/Nikoanas/Smart-House/blob/master/curtains/curtains_driver_2.jpg)

<h2>The Stepper Code :</h2>
   
     int x; 
    #define BAUD (9600)
    void setup() {
    Serial.begin(BAUD);
    pinMode(6,OUTPUT); // Enable
    pinMode(5,OUTPUT); // Step
    pinMode(4,OUTPUT); // Dir
    digitalWrite(6,LOW); // Set Enable low

    }

    void loop() {
    digitalWrite(6,LOW); // Set Enable low
    digitalWrite(4,HIGH); // Set Dir high
    Serial.println("Loop 200 steps (1 rev)");
     for(x = 0; x < 200; x++) // Loop 200 times
    {
    digitalWrite(5,HIGH); // Output high
    delay(10); // Wait
    digitalWrite(5,LOW); // Output low
    delay(100); // Wait
    }
    Serial.println("Pause");
    delay(1000); // pause one second
    }

<h2> The Curtains</h2>

     #include <NewPing.h>
     #include <Stepper.h>
    #include <AccelStepper.h>


     #define LSENSOR A1
     #define trigPin 13
     #define echoPin 12 
     #define TRIGGER_PIN  9
     #define ECHO_PIN     10
     #define MAX_DISTANCE 200

    NewPing sonar(9, 10, 200);
    boolean light_mode=true,sonar_mode=true;

    void setup() {
    Serial.begin(9600);
    pinMode(6,OUTPUT); // Enable
    digitalWrite(6,LOW); // Set Enable low
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
     }

    void loop() {
    delay(50);
    if(sonar_mode){
     int cm = sonar.ping();
    if (cm<200){
    //open curtain
    }else if (cm>200){
    //close curtain
    }
    }
    
    if(light_mode){
     int lum = analogRead(LSENSOR);
    Serial.println(lum);
    if (lum>750){
     //open curtain
    }else if (lum<750){
    //close curtain
