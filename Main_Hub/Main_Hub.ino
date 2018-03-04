#include <SPI.h>
#include <Ethernet.h>
#include <PubSubClient.h>
#include "RF24.h"
#include "Wire.h"
#include <DigitalIO.h> 

// Update these with values suitable for your network.
byte mac[]    = {  0x00, 0xAA, 0xBB, 0xCC, 0xDE, 0x02 };
IPAddress ip(192, 168, 1, 73);
IPAddress server(192, 168, 1, 68);



RF24 radio(7,8);
const uint64_t pipe[3]={0xB3B4B5B6CD05 , 0xE8E8F0F0E1F1, 0xE8E8F0F0E1LL};//temp/curtains/relay
//String command="";
int tempr=-255, humid=0;


String getData(void);  
bool sendData(String Datain);   
void Command_Shell(String data); 


void callback(char* topic, byte* payload, unsigned int length) {
  String tempor="";
  String data="";
  String device="";
  for (int i=0;i<length;i++) {
    tempor=tempor + ((char)payload[i]);
  }
  
  Serial.println(tempor);
  
  Command_Shell(tempor);

  /*if (data[0]=='#'){
  if (data[1]=='m' && data[2]=='h'){ 
  device=data.substring(3,7); 
   if (device=="temp"){
    device=data.substring(7,9);
    tempr=device.toInt();
    //SEND MQTT to OPENHAB
    
    }
    else if (device=="humd"){
      device=data.substring(7,9);
      humid=device.toInt();
      //SEND MQTT to OPENHAB
    }
    else if (device=="alrm"){      
      //SEND AlLARM to OPENHAB
      }  
}
else if (data[1]=='n' && data[2]=='1'){
  Serial.println("Step 1");
  radio.stopListening();
  Serial.println("Step 1.5");
  delay(115);
  radio.openWritingPipe(pipe[2]);
  
  device=data.substring(3,data.length());
  device="#mh"+device;
  Serial.print("Step 2:");
  Serial.println(device);
  sendData(device);
  delay(10); 
  radio.openReadingPipe(1,pipe[0]);
  delay(10);
  radio.startListening(); 
  } 
else if (data[1]=='n' && data[2]=='2'){ 
  radio.stopListening();
  radio.openWritingPipe(pipe[1]);
  device=data.substring(3,data.length());
  device="#mh"+device;
  sendData(device);
  radio.openReadingPipe(1,pipe[0]);
  radio.startListening();
}
} */
  
  }
 


EthernetClient ethClient;
PubSubClient client(ethClient);

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("arduinoClient")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("/Topic","MainHub connected");
      // ... and resubscribe
      client.subscribe("/Topic");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() {
   Wire.begin();
   Serial.begin(57600);
   //RF Configurations
   radio.begin();
   radio.setPALevel(RF24_PA_LOW);
   radio.openReadingPipe(1,pipe[0]);
   radio.startListening();
    //MQTT & Ethernet configurations
   client.setServer(server, 1883);
   client.setCallback(callback);
   Ethernet.begin(mac, ip);
  // Allow the hardware to sort itself out
  delay(1500);
  
}

void loop() {
  
String data="";
//Get Data from RF

//MQTT SIDE
if (!client.connected()) {
    reconnect();}
    
client.loop();
while (radio.available()) {
     data= getData();
     Command_Shell(data);
}
  

}
