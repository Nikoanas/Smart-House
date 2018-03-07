
<h1> Light Control- Coffee Maker/ Dimmer  </h1>


<h2> What will you need? </h2>

<ul>
    <li>	1 Arduino Uno board</li>
    <li>	1 5V Relay module 220v </li>
    <li>  1 lamp 16W</li>
    <li>	1 multi socket </li>
</ul>

<h2> How we connect a relay to our circuit? </h2>

<img src = 'https://github.com/Nikoanas/Smart-House/blob/master/lights/1.png?raw=true' />

<h2> What is a relay? <h2>

<p> A Relay is an electrically operated switch. Many relays use an electromagnet to mechanically operate the switch and provide electrical isolation between two circuits. There are three terminals: NO, COM, NC. </p>

<ul>
 <li> COM (Common connection)--> it is the center terminal, It is hot as power to the load is connected at this terminal.
</li>
<li> NO (Normally open) ---> It acts like a switch, since it is open. There is no contact between COM and NO. When we trigger the relay module, it connects to COM by the electromagnet inside the relay and supply to the load is provided. Thus the circuit is closed until we trigger the state to low in relay.
</li>
<li>NC Normally closed---->It is always in contact with COM, even when relay is not powered. When we trigger the relay it opens the circuit, so the connection is lost. it behaves just opposite to NO </li>
</ul>

<img src = 'https://github.com/Nikoanas/Smart-House/blob/master/lights/2.png?raw=true' /> 

<h2> Dimmer </h2>

<p>What will you need?
 </p>

<ul>
  <li>	Arduino Uno board
 </li>
  <li> Resistors: 330ohm(1No.s), 33k(2no.s), 22k(1No.s), 220ohm(1No.s)
</li>
  <li> 	Optocoupler: 4N35(1No.s)
</li>
  <li>	Diode: 1N4508(4No.s), 1N4007(1No.s), Zener 10V.4W(1No.s)
 </li>
  <li> Capacitor 2.2uF/63V(1No.s), 220nF/275V(1No.s)
</li>
  <li> MOSFET: IRF830A
</li>
  <li> Lamp: 100W
</li>
  </ul>
  
  <h3> What is the MOSFET ? </h3>
  <p> The metal–oxide–semiconductor field-effect transistor (MOSFET) is a type of transistor used for amplifying or switching electronic signals.  The MOSFET is a four-terminal device with source (S), gate (G), drain (D), and body (B) terminals. The Body and the source are connected to each other internally and only three terminals appear in electrical diagrams. The IRF830A in a diode bridge is used to control the voltage across the bulb with pulse wave modulation (PWM). The power supply voltage for driving the gate is supplied by the voltage across the MOSFET.
 </p>

<h3> What is an Optocoupler?
 </h3>
 
 <p> An opto-isolator or optocoupler  is a semiconductor device that uses a short optical transmission path to transfer an electrical signal between circuits or elements of a circuit, while keeping them electrically isolated from each other. These components are used in a wide variety of communications, control and monitoring systems that use light to prevent electrical high voltage from affecting a lower power system receiving a signal.
 </p>
 
<h3> How does it work? </h3>

<p>  In this project, we are going to adjust the brightness of the lamp connected to the circuit by serial port. The brightness can be changed according to the commands we are providing to the serial port. We will be using these particular commands in this arduino project:
</p> 
 <ul> 
  <li>‘0’ to TURN OFF
 </li>
  <li>	‘1’ for 25% brightness
 </li>
  <li>	‘2’ for 50% brightness
 </li>
  <li> ‘3’ for 75% brightness</li>
  <li> ‘4’ for 100% brightness</li>
  </ul>
  
  <img src = 'https://github.com/Nikoanas/Smart-House/blob/master/lights/3.png' />
