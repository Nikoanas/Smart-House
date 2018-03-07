#include <DigitalIO.h>
#include <DigitalPin.h>
#include <I2cConstants.h>
#include <PinIO.h>
#include <SoftI2cMaster.h>
#include <SoftSPI.h>

#include  <SPI.h>
#include "RF24.h"
#include "Wire.h"

String msg;
char lol;
RF24 radio(7,8);
const uint64_t pipe =  0xE8E8F0F0E1LL;
//const uint64_t pipe2 = 0xB3B4B5B6CDLL;


void setup(void){
 Serial.begin(57600);
 radio.begin();
 radio.setPALevel(RF24_PA_LOW);
 radio.openWritingPipe(pipe);
// radio.openWritingPipe(pipe2);
 radio.stopListening();}

void loop(void){


if (Serial.available()>0) {
  delay(10);

  
while (Serial.available()>0){
  lol= Serial.read();
  msg +=lol;  }

int leng=msg.length();
Serial.print(msg);
Serial.println(leng);
//bool ok = radio.write( &lol, 1 ); 
bool ok = sendData(msg);
Serial.println(ok);
msg="";
 

 

/*
 while (Serial.available()>0){
 char lol= Serial.read();
 bool ok = radio.write( &lol, 1 );
 delay(50);
*/
 
  }
}

 
