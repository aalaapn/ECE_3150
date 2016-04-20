#!/usr/bin/python

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pylab


c=np.loadtxt('test.txt')

x = c[:,0]
y = c[:,1]

r=(x/y)/10

print(x[121])
print(r[121])

fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.set_yscale('log')
ax1.set_title("Diode Differential Resistance")    
ax1.set_xlabel('Bias Voltage [V]')
ax1.set_ylabel('Differential Resistance [$\Omega$]')

ax1.plot(x,r, c='r')
pylab.xlim([.09,.505])

leg = ax1.legend()

plt.show()