import math as mt
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import jn, yn, jn_zeroes, yn_zeroes

def RMS(x):
    return (x / mt.sqrt(2))

##
##class rootmeansquare:
##    
##    def __init__(self, x):
##        self.x = x
##     self.xRMS = RMS(x)
##   
##   def __str__(self):
##        return("Point at [%f, %f]" % (self.x, self.xRMS))
##
    
##np.myRMSVal = rootmeansquare(55)
##print(np.myRMSVal)

myArray = np.arange(0,100,5)
myArray2 = np.array([0])
for I in myArray:
    myArray2 = RMS(myArray)
    
plt.figure()
plt.plot(myArray, myArray2)
plt.xlabel("Decibal value")
plt.ylabel("RMS value")
plt.show()