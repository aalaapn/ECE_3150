import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pylab
from scipy.interpolate import spline
from scipy import interpolate
#gate is upper smu (1)
#drain is lower smu (2)

#NFET

nfetData = np.loadtxt("data/partbb.txt")
nfetV1 = nfetData[:, 0]
#nfetC1 = nfetData[:, 1]
#nfetV2 = nfetData[:, 2]
nfet_C2 = nfetData[:, 1]/340
#nfetSquare = nfetData[:, 4]
#print(nfet_C2.size)

#nfet_gm=np.array([])
#for i in range(1,120):
#	gm = (nfetC2[i+1]-nfetC2[i-1])/(nfetV1[i+1]-nfetV1[i-1])
#	nfet_gm=np.append(nfet_gm,gm) 
# nfetV1=nfetV1[0:119]
nfet_C22 = nfet_C2[55:120]
nfetV11 = nfetV1[55:120]
nfetFit = np.polyfit(nfetV11, nfet_C22, 1)
nfetFit_fn = np.poly1d(nfetFit)
m2, b2 =  np.polyfit(nfetV11, nfet_C22, 1)
print(m2)
print (b2)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("Transconductance for NFET")
ax1.set_ylabel('Transconductance $g_m$')
ax1.set_xlabel('Gate to Source Voltage $V_{GS}$')
ax1.plot(nfetV1, nfetFit_fn(nfetV1), label = 'Straight Fit Line')
ax1.plot(nfetV1, nfet_C2, label = '$g_m$')
leg = ax1.legend()
#pylab.ylim([2e-4, 10e-4])



#PFET
pfetData = np.loadtxt("data/partf.txt")
pfetV1 = pfetData[:, 0]
pfetC1 = pfetData[:, 1]
pfetV2 = pfetData[:, 2]
pfetC2 = pfetData[:, 3]
pfetSquare = pfetData[:, 4]

pfet_gm=np.array([])
for i in range(1,120):
	gm = (pfetC2[i+1]-pfetC2[i-1])/(pfetV1[i+1]-pfetV1[i-1])
	pfet_gm=np.append(pfet_gm,gm)
print(pfetV1.size)
print(pfet_gm.size)
pfetV1=pfetV1[0:119]
pfet_gm2 = pfet_gm[70:120]
pfetV11 = pfetV1[70:120]
pfetFit = np.polyfit(pfetV11, pfet_gm2, 1)
m1, b1 =  np.polyfit(pfetV11, pfet_gm2, 1)
print(m1)
print (b1)
pfetFit_fn = np.poly1d(pfetFit)


fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.set_title("Transconductance for PFET")
ax2.set_ylabel('Transconductance $g_m$')
ax2.set_xlabel('Gate to Source Voltage $V_{GS}$')
ax2.plot(pfetV1, pfetFit_fn(pfetV1), label = 'Straight Fit Line')
ax2.plot(pfetV1, pfet_gm, label = '$g_m$')
#pylab.ylim([2e-4, 10e-4])
leg = ax2.legend()
plt.show()