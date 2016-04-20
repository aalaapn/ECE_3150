import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pylab
#gate is upper smu (1)
#drain is lower smu (2)

#NFET

nfetData = np.loadtxt("data/partb.txt")
nfetV1 = nfetData[:, 0]
nfetC1 = nfetData[:, 1]
nfetV2 = nfetData[:, 2]
nfetC2 = nfetData[:, 3]
nfetSquare = nfetData[:, 4]


nfetC21 = nfetC2[25:50]
nfetV11 = nfetV1[25:50]

nfetFit = np.polyfit(nfetV11, nfetC21, 1)
nfetFit_fn = np.poly1d(nfetFit)
a,b=np.poly1d(nfetFit)
print(a)
print(b)
print(nfetV1[25])
print(nfetV1[50])


pos = np.where(np.abs(np.diff(nfetC21)) >= 0.5)[0]+1
nfetV11 = np.insert(nfetV11, pos, np.nan)
nfetC21 = np.insert(nfetC21, pos, np.nan)




fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_yscale('log')
ax1.set_title("Subthreshold Condition")
ax1.set_ylabel('Transconductance $g_m$')
ax1.set_xlabel('Gate to Source Voltage $V_{GS}$')

v=np.arange(0,.5,.01)
v2=(19.5*(v)-24.5)
ax1.plot(v, np.exp(v2))
ax1.plot(nfetV1[0:121], nfetC2[0:121], 'o')
#pylab.ylim([2e-4, 10e-4])x = np.insert(x, pos, np.nan)



plt.show()
#second array of current values log 10 of current
