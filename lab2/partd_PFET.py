import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pylab
#gate is upper smu (1)
#drain is lower smu (2)
data = np.loadtxt("data/PFET_threshold_partg.txt")
Id1 = data[:, 3]
Vds1 = data[:, 2]
go1=np.array([])
for i in range(1,50):
	g01 = (Id1[i+1]-Id1[i-1])/(Vds1[i+1]-Vds1[i-1])
	go1=np.append(go1,g01)

Id2 = data[:, 8]
Vds2 = data[:, 7]
go2=np.array([])
for i in range(1,50):
	g02 = (Id2[i+1]-Id2[i-1])/(Vds2[i+1]-Vds2[i-1])
	go2=np.append(go2,g02)

Id3 = data[:, 13]
Vds3 = data[:, 12]
go3=np.array([])
for i in range(1,50):
	g03 = (Id3[i+1]-Id3[i-1])/(Vds3[i+1]-Vds3[i-1])
	go3=np.append(go3,g03)

Id4 = data[:, 18]
Vds4 = data[:, 17]
go4=np.array([])
for i in range(1,50):
	g04 = (Id4[i+1]-Id4[i-1])/(Vds4[i+1]-Vds4[i-1])
	go4=np.append(go4,g04)

Id5 = data[:, 23]
Vds5 = data[:, 22]
go5=np.array([])
for i in range(1,50):
	g05 = (Id5[i+1]-Id5[i-1])/(Vds5[i+1]-Vds5[i-1])
	go5=np.append(go5,g05)

Id6 = data[:, 28]
Vds6 = data[:, 27]
go6=np.array([])
for i in range(1,50):
	g06 = (Id6[i+1]-Id6[i-1])/(Vds6[i+1]-Vds6[i-1])
	go6=np.append(go6,g06)

Id7 = data[:, 33]
Vds7 = data[:, 32]
go7=np.array([])
for i in range(1,50):
	g07 = (Id7[i+1]-Id7[i-1])/(Vds7[i+1]-Vds7[i-1])
	go7=np.append(go7,g07)

plt.figure()
plt.title("PFET Output Conductance")
plt.xlabel('$V_{DS}$')
plt.ylabel('$g_o$')

#plt.plot(Vds1, Id1, label = '$V_{GS} = -1 V$')
plt.plot(Vds2[0:49], go1, label = '$V_{GS} = -1 V$')
plt.plot(Vds3[0:49], go2, label = '$V_{GS} = -1.25 V$')
plt.plot(Vds4[0:49], go3, label = '$V_{GS} = -1.5 V$')
plt.plot(Vds5[0:49], go4, label = '$V_{GS} = -1.75 V$')
plt.plot(Vds6[0:49], go5, label = '$V_{GS} = -2 V$')
plt.plot(Vds7[0:49], go6, label = '$V_{GS} = -2.25 V$')
pylab.xlim([-1,5])


plt.legend()
plt.show()