 #include <PubSubClient.h>
void Command_Shell(String data){
String device="";
char tempr[2];
char humid[2];

if (data[0]=='/'){
  if (data[1]=='m' && data[2]=='h'){ 
  device=data.substring(3,7); 
   
   if (device=="temp"){
    device=data.substring(7,9);
    tempr[0]=device[0];
    tempr[1]=device[1];
    Serial.print(tempr[0]);
    Serial.println(tempr[1]);
    client.publish("/Topic/Temperature",tempr,2);
    
    }
    else if (device=="humd"){
      device=data.substring(7,9);
      humid[0]=device[0];
      humid[1]=device[1];

      client.publish("/Topic/Humidity",humid,2);
    }
    else if (device=="alrm"){      
      client.publish("/Topic/Flood","Pnigwmaste");
      }  
}
else if (data[1]=='n' && data[2]=='1'){
 
  radio.stopListening();
  
  delay(100);
  radio.openWritingPipe(pipe[2]);
  
  device=data.substring(3,data.length());
  device="#mh"+device;

  sendData(device);
  delay(50); 
  radio.openReadingPipe(1,pipe[0]);
  delay(50);
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
}

}
