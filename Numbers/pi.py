#Finds Pi to Nth digit

#Input is Nth digit
from math import pi 

print "This program gets Pi to the Nth digit (up to 48th)."
digit = input("Enter a digit: ")
print ("{0:.%df}" % min(48, digit)).format(pi)
