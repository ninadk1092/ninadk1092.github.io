
## Task:
* Use the microcontroller chip(Atmega328) standalone - w/o the Arduino board
* Burn a bootloader on the Atmega328 so as to be able to program the IC
* Program the IC after the bootloader has been burned to it

## Issues faced: 
* Programmer is not responding
	- device signature for Atmega328-pu is 0x1e 0x95 0x14
	- device signature for Atmega328p is 0x1e 0x95 0x0f
	- Once bootloader is installed remember to change the device signatire back to 0x1e 0x95 0x0f
* Yikes! Double check your connections
	- Capacitors connected from the 16MHz crystal and GND were way too high(10uF). The circuit works without them

***********************************************************

To be researched:
* What is the bootloader and why is it required.
* What is the difference between Atmega328p and Atmega328-pu.
* Why is it recommended to use capacitors between the ground and the crystal terminals?
* After changing back the device signatures, is the Atmega328-pu programmable from the UNO?
* What would have changed in the above process if we were given Atmega328p?

-------------------------------------------------------------------- 
