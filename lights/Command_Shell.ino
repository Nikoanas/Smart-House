void Command_Shell(String data){
Serial.println(data);
String device="";

if (data[0]=='#'){
  if (data[1]=='m' && data[2]=='h'){ 
  device=data.substring(3,7);  
  if (device=="rel1"){   
    if (data.substring(7,9)=="on"){ digitalWrite(RELAY1,HIGH);}
    else if (data.substring(7,9)=="of"){digitalWrite(RELAY1,LOW);}  
   }
  else if (device=="rel2"){
    if (data.substring(7,9)=="on"){ digitalWrite(RELAY2,HIGH);}
   else if (data.substring(7,9)=="of"){digitalWrite(RELAY2,LOW);}  
   }
  else if (device=="caff"){
    if (data.substring(7,9)=="of"){
      digitalWrite(COFFEE,LOW);
      flag=false;}
   else if (data.substring(7,9)=="on"){
    if (data[9]!='i'){
     timer = data.substring(9,13);
     timer=timer.toInt();
     flag=true;   
    } else {
    digitalWrite(COFFEE,HIGH);}
    }
  } 
  } 
}
device="";
data="";
}
