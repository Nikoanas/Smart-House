#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"
char msg;
RF24 radio(7,8);
const uint64_t pipe1 = 0xE8E8F0F0E1LL;    // Node1
const uint64_t pipe2 = 0xE8E8F0F0E1F1;
byte Numpipe[]={0, 1};


void setup(void){
 Serial.begin(9600);
 radio.begin();
 radio.setPALevel(RF24_PA_MAX);
 radio.openReadingPipe(0,pipe1);
 radio.openReadingPipe(1,pipe2);
 radio.startListening();
 
 
}

void loop(void){
 
  
   while (radio.available()) {
     String data= getData();
     
     //radio.read(&msg, 1);     
     Serial.println(data);
     delay(10);
     }
     
  

     }
