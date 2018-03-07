<h1> Temperature/Humidity Sensor
</h1>

<p>The purpose of this project is to get you started with the Arduino microcontroller and a temperature/humidity sensor, as well as sending the data wirelessly to other nodes.
</p>

<img src= ' https://github.com/Nikoanas/Smart-House/blob/master/Temperature-%20Humidity/Picture1.png?raw=true' />

<h2>What will you need?
 </h2>
 
 <ul>
  <li> 1 Arduino Uno board
 </li>
  <li> 	1 DHT11 sensor
 </li>
  <li> Some jumper wires
 </li>
  <li> RF Chip(@2.4 Ghz)
 </li>
  </ul>
  
  <h3> Basic functions of this library :
</h3>

<ul> 
  <li>dht.readHumidity ()
This function let you read from the sensor the humidity in percentage(%).
 </li>
  <li> dht.readTemperature ()
This function let you read from the sensor the temperature in Celsius(default). If you want to measure the temperature in Fahrenheit you have to include inside the parentheses the word “true”.
</li>
  <li>dht.computeHeatIndex(x, y, false)
This function let you calculate the heat index (human-perceived equivalent temperature) where x is the temperature, y is the humidity, and false is used when the temperature is given in Celsius.
 </li>
  </ul>
  
  <img src= 'https://github.com/Nikoanas/Smart-House/blob/master/Temperature-%20Humidity/Picture2.png' />
  
  <h3> RF Chip Operation
</h3> 

<p>  The whole RF operation relies on wireless channels created between the nodes. Each channel has a unique address, and only nodes using that specific address can see the traffic within the channel.
When you want to send data at the channel, you issue the following commands:
radio.openWritingPipe(pipe);
where pipe is the address for the specific channel.
</p>

<h3>Before the Setup()

</h3> 

<p> Firstly, you have to declare the pins in which you connected the CE/CSN pins of the chip. For our application we will be using pins 7,8 and to declare them you have to add to the code the line: 
RF24 radio(7,8);
Next, we declare the channel address(pipe). For this node we have to declare its unique address. To do so, we create an array with the addresses like so:
const uint64_t pipe= 0xB3B4B5B6CD05
You also have to include in your code the functions sendData() and getData(), which will be taking care of the data transmission. In order to declare the functions and use them inside your code, you have to save the files inside the same folder of your main Arduino sketch, and call them before the setup routine of the code.
Inside the Setup()
Within the Setup function, you have to instantiate the radio object, as well as start the Wire and Serial bus. In order to do that, you will have to use the commands:
   Wire.begin();
   Serial.begin(57600);
   radio.begin();
   radio.setPALevel(RF24_PA_LOW);->set the transmission power to Low for lower error rates
   radio.openWritingPipe(pipe);

   Inside the Main Loop

If you wish to check for incoming data, you use the command :
radio.available()
which will return you the number of characters incoming. Using the supplied getData, u can retrieve the whole incoming string.
On the other hand, in order to transmit a command of your choosing, you call the sendData(string command), which will transmit your data, and return you an acknowledgment based of the success of the transmission.
 </p>

<h3> Command Structure
 </h3>
 
<p> All of the network’s commands have to follow a specific format. The structure is as follows:
General format:	#TTXXXXYY!
# 			->	frame start
TT			-> 	transmission code (mh, n1,etc)
XXXX			->	action id	(rel1,coff,curt..etc)
YY			->	action/value		(on, of,20..etc)
!			-> 	frame ending 
The frame start and end has to be included, otherwise the command will be invalid and disregarded from the nodes/server.
</p>

<p> RF Outgoing Commands

Node 3 (Temp/Humidity/flood)[only sends] --pipe =0xB3B4B5B6CD05;
/_mh_temp_value_!		Eg. /mhtemp19		-->temp=19
/_mh_humd_value_!
/_mh_alrm!	
 </p>
