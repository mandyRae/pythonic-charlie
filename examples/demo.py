# -------------PYTHONIC-CHARLIE-------------#
#                                           #
#       Python class for controlling        #
#          SparkFun 8x7 LED Array           #
#           with the Raspberry Pi           #
#            utilizing RPi.GPIO.            #
#                                           #
#  https://www.sparkfun.com/products/13795  #
#                                           #
#---------------DEMO OF USAGE---------------#
#                                           #
#          V0.0.0 -- 18 Jun 2016            #
#                                           #
#-------------------------------------------#

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
