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

<img src = '
