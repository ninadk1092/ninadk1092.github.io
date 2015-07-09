
## Using an ATmega328p, fresh from a factory, on your custom board

ATmega328P, fresh from the factory are set by default to use the internal RC at 1MHz. Whenever you upload code to this chip, through ISP, you first need to change the fuse bits to suit the design of your board. For instance, if your board is designed so as to use an external 8MHz crystal, you will need to set the relevant fuse bits.

If this is not done, the code will still upload without errors, but the clock will work as if its using a 1 MHz clock, instead of the 8 MHz clock. So technically, this code will work 8 times "slower". In Arduino terms, delay(1000) will actually work like delay(8000). This happens because delay() in arduino is implemented to count from the counter until the desired value is reached. This count will count 8 times slower, because the controller is using a clock source thats 8 times slower than expected. 

**So how to rectify this?**

I used **avrdude** and **USBASP** to do this. Follow this process.

* **Using the right avrdude** 
For macOS:
```
cd /Applications/Arduino.app/Contents/Java/hardware/tools/avr/bin
```
There will be an **avrdude** in this location.

* **Setting fuse bits to use external 8 MHz crystal**
```
avrdude -p atmega328p -c usbasp -U lfuse:w:0xdc:m -U hfuse:w:0xDF:m -U efuse:w:0xFF:m -U lock:w:0xFF:m 
```
Refer to this [link](http://www.pocketmagic.net/how-to-set-the-avr-fusebits/) for complete documentation.

Now your ATmega328P is ready to use external 8 MHz crystal.

### Further Reading:
* Detailed explanation about XTAL usage can be found [here](http://treehouseprojects.ca/fusebits/)
* Uploading USBASP firmware [process.](http://www.rogerclark.net/updating-firmware-on-usbasp-bought-from-ebay/) 
