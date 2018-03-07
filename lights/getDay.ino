String getDay(int dayOfWeek)
{ String Date;
  // convert the byte variable to a decimal number when displayed
  switch(dayOfWeek){
  case 1:
    Date="Sun";
    break;
  case 2:
    Date="Mon";
    break;
  case 3:
    Date="Tue";
    break;
  case 4:
    Date="Wed";
    break;
  case 5:
    Date="Thu";
    break;
  case 6:
    Date="Fri";
    break;
  case 7:
    Date="Sat";
    break;
  }
  return Date;
}

