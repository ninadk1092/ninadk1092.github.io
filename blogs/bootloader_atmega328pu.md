29, Oct 2014
Ninad Kulkarni

## Loading the bootloader to Atmega328pu from Arduino UNO.

#### Task:
* Use the microcontroller chip(Atmega328) standalone - w/o the Arduino board
* Burn a bootloader on the Atmega328 so as to be able to program the IC
* Program the IC after the bootloader has been burned to it

### Issues faced: 

##### Programmer is not responding
* avrdude.conf file
	* Selecting the Arduino UNO from Arduino IDE->Tools->Board->Arduino UNO implies chosing the device signature for Atmega328p which is 0x1E 0x95 0x0F which is mentioned in the avrdude.conf file.
	* In Mac OS, to navigate to this file, ensure that Arduino.app is listed under /Applications directory. If its not, simply drag and drop the Arduino.app file(the one which you execute to open the Arduino IDE) to the Applications tab on the left of the Finder window. 
	* avrdude.conf can now be found under /Applications/Arduino.app/Contents/Resources/Java/hardware/tools/avr/etc/avrdude.conf
	* The device signature for Atmega328-pu is 0x1e 0x95 0x14 and will be defined somewhere in the avrdude.conf file. Find this device signature and replace it by 0x1e 0x95 0x14, which is the device signature for Atmega328-pu. Save and close the file.
	* Now the bootloader should be burned onto the Atmega328-pu without any problems. In case it does not work, but the error changes from "Programmer not responding" to "Yikes!...Double check connections", then there are two things you will need to cater to in you connections.
	
	* Once bootloader is installed remember to change the device signatire back to 0x1e 0x95 0x0f

 
##### Yikes! Double check your connections
This error occurs if one of your connections is lose or incorrect. Double check all connections. If the issue persists, here is what worked for me.
	* Connect a 10uF (104 if ceramic) capacitor between the Reset and GND pins on the Arduino UNO. If you are using an electrolytic capacitor, insert the positive terminal into the Reset terminal.
	* If this does not solve the problem, check the capacitors connected from the 16MHz crystals to GND on the Atmega328-pu circuit. They should not be of a value higher than 10pF. My circuit worked without them. But some circuits online recommend that you connect them. So for the time being, even if you don't connect these capacitors, its alright. 
	* If the "Yikes.." issue persists, check all your connections once more. Although there is no reason why it won't work. 
	* Once bootloader is burned successfully, remember to change the device signature back to 0x1e 0x95 0x0f in the /Applications/Arduino.app/Contents/Resources/Java/hardware/tools/avr/etc/avrdude.conf file.

***********************************************************

#### To be researched:
* What is the bootloader and why is it required.
* What is the difference between Atmega328p and Atmega328-pu.
* Why is it recommended to use capacitors between the ground and the crystal terminals?
* After changing back the device signatures, is the Atmega328-pu programmable from the UNO?
* What would have changed in the above process if we were given Atmega328p?

-------------------------------------------------------------------- 
