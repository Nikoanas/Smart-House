<h1> openHAB </h1>

<h2> Software needed </h2>

<ul>
<li>Openhab_runtime (http://www.openhab.org/getting- started/downloads.html) </li>
<li>Openhab/Downloads/addons </li>
<li>openHAB Designer </li>
<li> mosquito</li>
<li> MQTT.fx</li>
</ul> 

<p>  We will use openHAB to set up a server and configure our own special application to control our house remotely. Also we will set mosquito as the broker of the MQTT protocol.</p>

<h4>  OpenHAB_runtime :</h4>
<p>This is the package, which you will actually run on your server and which does the “real” work ! </p>

<h4>  openHAB-Designer :</h4>
<p> openhab-designer: This is a configuration tool for the openhab-runtime. It comes with user-friendly editors to configure your runtime, to define your UIs and to implement your rules.</p>

<h4>  Mosquito : </h4>

<p>Mosquitto is an open source (EPL/EDL licensed) message broker that implements the MQTT protocol versions 3.1 and 3.1.1. MQTT provides a lightweight method of carrying out messaging using a publish/subscribe model. This makes it suitable for "Internet of Things" messaging such as with low power sensors or mobile devices such as phones, embedded computers or microcontrollers like the Arduino. </p>

<h3> 
How to make our Configurations</h3>

<p>  First, we need to declare our Items
Our Items should be all devices of the Smart House. Complete the file.items keeping in mind the syntax :</p>
<ul> 
<li> Itemtype itemname[“label text”][<icon name>][(group1group2...)][binding configuration]
 </li>
 </ul>
 
 <p> Example :
String LED "LED” {mqtt=">[mosquitto:/Topic:command:*:default]" } Do not forget the Item types : </p>

<img src = 'https://github.com/Nikoanas/Smart-House/blob/master/openHAB/Screen%20Shot%202018-03-07%20at%2018.44.34.png' />

<img src = 'https://github.com/Nikoanas/Smart-House/blob/master/openHAB/Screen%20Shot%202018-03-07%20at%2018.44.56.png' />

<p> Item Name : The item name is the unique name of the item and must be unique across all item files. It should only consist of letters, numbers and the underscore character. Spaces cannot be used.
P.S. Capitalization is important Sensor is different from sensor. </p>

<p> Label Text : The label text is used on the hand side to display a description for the specific item </p>

<p>  Icon Name :
The icon name is used to reference a png image file from folder ${openhab_home}/webapps/images/ .
These icons are used in the openHAB frontends.
We can put our own icons into that directory, but they need to be in png format and have a size of 32x32 pixel and a name only with small letters and the underscore.  </p>

<p>Binding Config : The most important part of an item.
Defines from where the item gets its values and where a given value/command should be send.
{ namespace = “bindingconfig”}  </p>


<p> MQTT Binding :
The MQTT binding bundle is available as a separate (optional) download. This binding allows openHAB to act as an MQTT client, so that openHAB items can send and receive MQTT messages to/from an MQTT broker. Mosquitto is our MQTT broker.
 </p>
 
 
 <h3> Item Binding Configuration for Inbound Messages </h3>
 
 <p> Syntax :
Item myItem {mqtt="<direction>[<broker>:<topic>:<type>:<transformer>] </p>
 
 <img src= ' https://github.com/Nikoanas/Smart-House/blob/master/openHAB/Screen%20Shot%202018-03-07%20at%2018.46.20.png' />
 
 <h3> Item Binding Configuration for Outbound Messages </h3>
 
 <p> 
Item itemName {mqtt="<direction>[<broker>:<topic>:<type>:<trigger>:<transformation >]"} </p>
 
 <img src= 'https://github.com/Nikoanas/Smart-House/blob/master/openHAB/Screen%20Shot%202018-03-07%20at%2018.46.30.png' />
 
 <h4> Sitemaps </h4>
  <p>
• Are used to create elements of a user interface for making openHAB items accessible to various frontends.
• Sitemap files are stored in ${openhab_home}/configurations/sitemaps </p>

<p> Syntax
• sitemap [sitemap_name] [label=“<title of the main screen>”]</p>
 
 <img src= 'https://github.com/Nikoanas/Smart-House/blob/master/openHAB/Screen%20Shot%202018-03-07%20at%2018.46.38.png' />
 
 <p>Frames : Frames are used to create visually separated areas of items
Frame [label=“<labelname”>] [icon=“<icon>”] [item=<item>] {
[additional sitemap elements] }
 </p>
  <p>Group : Creates a clickable area that opens up on a new page where we can show various elements.
Group [item=<itemname>] [label=“labelname>”] [icon=”<iconname>”] </p>
   <p>Selection :
• Selection item=<itemname> [label=“<labelname>”]
[icon=“<iconname>”] [mappings=“<mapping definition>”] </p>
    <p> Mappings :
Can be used to let the user chose an item from a list
mappings = [ “value1”=“name1”, “value2”=”name2” ]
f.e. : mappings = [ ”1”=“ON”, “0”=“OFF” ]
mappings = [ 1=“BBC”, 2=“CNN”, 3=”BLOOMBERG”]
</p>
    
<p>Switch: 
 Switch item=<itemname> [label=“<labelname>”] [icon=“<iconname>”]
[mappings=“<mapping definition>”]
Note : Switch elements with and without mapping are rendered differently in the interface </p>
