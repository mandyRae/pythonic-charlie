# pythonic-charlie
Python class for controlling SparkFun 8x7 LED Array with the Raspberry Pi utilizing RPi.GPIO.

This is a single-file class written in Python 2 for controlling the the SparkFun 8x7 LED Array 
(https://www.sparkfun.com/products/13795) that is controlled by eight charlieplexed pins. 

V0.0.0 is fully compatiable with the latest versions of both Python 2 and Python 3. 

#Repository Contents
* **charlie.py** - source file for class Charlie
* **/examples** - Examples utilizing charlie.py

#Documentation

###Installing

Here are three easy ways to convientently use pythonic-charlie on your Raspberry Pi:

1. **Copy and paste contents of charlie.py into existing code:** the class Charlie is short enough that you can 
easily paste it directly into your Python script. 

2. **Place the file charlie.py in the same directory as your script:** Placing the charlie.py file in within your script will 
enable you to call "import charlie" in your code.

3. **Copy charlie.py into directory `usr/lib/python2.7/dist-packages` and `usr/lib/python3/dist-packages`:** simply copy the
charlie.py file into the Python dist-packages directories. Any script locally run on your Raspberry Pi will then be able to 
`import charlie`.

###Contents of charlie.py
For help on the usage of charlie.py, see examples. For documentation on the methods of the Charlie class, type `import charlie`
and then `help(Charlie)`.

#License etc
This software is open source!
