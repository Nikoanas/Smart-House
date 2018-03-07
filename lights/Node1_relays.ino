#include  <SPI.h>
#include "RF24.h"
#include "Wire.h"

#define RELAY1  9
#define RELAY2  6
#define COFFEE  4
#define DS3231_I2C_ADDRESS 0x68
     
RF24 radio(7,8);
const uint64_t pipe = 0xE8E8F0F0E1LL;
String command="";
String timer,Day;
bool flag=false;


String getData(void);     
void Command_Shell(String data); 
void readDS3231time(byte *second,byte *minute,byte *hour,byte *dayOfWeek,byte *dayOfMonth,byte *month,byte *year);
String getDay(int dayOfWeek);

//......Other functions............
byte decToBcd(byte val)
{
  return( (val/10*16) + (val%10) );
}

byte bcdToDec(byte val)
{
  return( (val/16*10) + (val%16) ); 
} 
           
void setup(){
   Wire.begin();
   Serial.begin(57600);
   Serial.println("Welcome...Node1");
   radio.begin();
   radio.setPALevel(RF24_PA_LOW);
   radio.openReadingPipe(0,pipe);
   radio.startListening();
   
   pinMode(RELAY1, OUTPUT);  
   pinMode(RELAY2, OUTPUT);
   pinMode(COFFEE, OUTPUT);   
}

void loop(){
delay(10);

//Read Date-Time
 byte second, minute, hour, dayOfWeek, dayOfMonth, month, year;  
 readDS3231time(&second, &minute, &hour, &dayOfWeek, &dayOfMonth, &month,&year);
 Day=getDay(dayOfWeek);

 
//Check RF
while (radio.available()) {
     command = getData();
     Command_Shell(command);     
    }

//Check Time/Timer -> Activate COFFEE
if (flag==true){
if( int(timer.toInt()/100)==hour && int(timer.toInt()%100)==minute-5){
  digitalWrite(COFFEE,HIGH);  }
  }


 
 }


 
