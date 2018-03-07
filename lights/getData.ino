String getData(){
  char lol;
  String data="";
  delay(10);

 while (lol!='!'){
  if (radio.available()){
  radio.read(&lol,1);
  data +=lol;}
 }  
  data.remove(data.length()-1);
 
 return data;
  
  }
