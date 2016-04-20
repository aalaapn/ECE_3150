#!/usr/bin/python

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pylab
import scipy


c=np.loadtxt('test.txt')

x = c[:,0]
y = c[:,1]



r=x/y
A=97700/r*10

vout4=4.2e-9*97700*np.exp((.4)/(.0258*1.94))*2*.1/(1.94*.0258)

vout5=4.2e-9*97700*np.exp((.5)/(.0258*1.94))*2*.1/(1.94*.0258)
vout4=4
vout5=19

y2 = [vout4, vout5]
x2 = [.4, .5]

y3 = [29.202206020901031, A[160]]
print(A[160])
x3 = [.4, x[160]]


fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Gain")    
ax1.set_xlabel('Bias Voltage [V]')
ax1.set_ylabel('Gain')

#ax1.plot(x,A, c='r', label='Theoretical Gain')
plt.plot(x2, y2, 'bo', label ='Measured Gain')
plt.plot(x3,y3, 'ro', label='Theoretical Gain')

pylab.ylim([-1,220])
pylab.xlim([.38,.505])
ax1.yaxis.set_ticks(np.arange(-1, 220, 21))
leg = ax1.legend()

plt.show()