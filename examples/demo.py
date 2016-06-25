'''
# -----------PYTHONIC-CHARLIEPLEX-----------#
#                  demo.py                  #
#                                           #
#    Demo of Python class for controlling   #
#    charlieplexed SparkFun 8x7 LED Array   #
#           with the Raspberry Pi.          #
#                                           #
#  https://www.sparkfun.com/products/13795  #
#                                           #
#---------------DEMO OF USAGE---------------#
#                                           #
#          V0.0.0 -- 18 Jun 2016            #
#                                           #
#-------------------------------------------#

The MIT License (MIT)

Copyright (c) 2016 Amanda Cole

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
#import charlie, of course
import charlie

#denote the hookup of the GPIO pins, using BCM numbering
a = 26
b = 19
c = 13
d = 6
e = 5
f = 22
g = 27
h = 17

pins = [a,b,c,d,e,f,g,h]

#initialize the LED array
array = charlie.Charlie(pins)

#test the array to verfiy proper wiring
array.test()

#light the first column of pixels on the array for 5 seconds
array.display([[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7]], 5)

#light the first row of pixels on the array for 5 seconds
array.display([[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]], 5)

#run the random screensaver for 5 seconds
array.screensaver(5)

#clear display
array.clearDisplay()
