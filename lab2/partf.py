import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pylab
#gate is upper smu (1)
#drain is lower smu (2)
data = np.loadtxt("Data/inverter_parth.txt")
V1 = data[:, 0]
V2 = data[:, 2]


plt.figure()
plt.title("CMOS Inverter")
plt.xlabel("Voltage In")
plt.ylabel("Voltage Out")
plt.plot(V1,V2)

l = plt.axvline(x=1.118, color='k')
l = plt.axvline(x=3.28, color='r')
l = plt.axvline(x=3.35, color='g')
l = plt.axvline(x=5-1.42, color='k')

pylab.xlim([0,5.5])
pylab.ylim([-.3,5.5])
plt.show()