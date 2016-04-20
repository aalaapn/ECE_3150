import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pylab
#gate is upper smu (1)
#drain is lower smu (2)
data = np.loadtxt("data/NFET_output_curve_partc.txt")
Id1 = data[:, 2]
Vds1 = data[:, 1]
go1=np.array([])
for i in range(1,50):
	vds=((Vds1[i+1]-Vds1[i-1]))
	if(vds==0):
		vds = 1
	g01 = (Id1[i+1]-Id1[i-1])/(vds)
	go1=np.append(go1,g01)

Id2 = data[:, 6]
Vds2 = data[:, 5]
go2=np.array([])
for i in range(1,50):
	vds=(Vds2[i+1]-Vds2[i-1])
	if(vds==0):
		vds = 1
	g02 = (Id2[i+1]-Id2[i-1])/vds
	go2=np.append(go2,g02)

Id3 = data[:, 10]
Vds3 = data[:, 9]
go3=np.array([])
for i in range(1,50):
	vds=(Vds3[i+1]-Vds3[i-1])
	if(vds==0):
		vds = 1
	g03 = (Id3[i+1]-Id3[i-1])/vds
	go3=np.append(go3,g03)

Id4 = data[:, 14]
Vds4 = data[:, 13]
go4=np.array([])
for i in range(1,50):
	vds=(Vds4[i+1]-Vds4[i-1])
	if(vds==0):
		vds = 1
	g04 = (Id4[i+1]-Id4[i-1])/vds
	go4=np.append(go4,g04)

Id5 = data[:, 18]
Vds5 = data[:, 17]
go5=np.array([])
for i in range(1,50):
	vds=(Vds5[i+1]-Vds5[i-1])
	if(vds==0):
		vds = 1
	g05 = (Id5[i+1]-Id5[i-1])/vds
	go5=np.append(go5,g05)

Id6 = data[:, 22]
Vds6 = data[:, 21]
go6=np.array([])
for i in range(1,50):
	vds=(Vds6[i+1]-Vds6[i-1])
	if(vds==0):
		vds = 1
	g06 = (Id6[i+1]-Id6[i-1])/vds
	go6=np.append(go6,g06)


plt.figure()
plt.title("NFET Output Conductance")
plt.xlabel('$V_{DS}$')
plt.ylabel('$g_0$')

#plt.plot(Vds1, Id1, label = '$V_{GS} = -1 V$')
plt.plot(Vds1[0:49], go1, label = '$V_{GS} = -1 V$')
plt.plot(Vds2[0:49], go2, label = '$V_{GS} = -1.25 V$')
plt.plot(Vds3[1:49], go3[1:49], label = '$V_{GS} = -1.5 V$')
plt.plot(Vds4[3:49], go4[3:49], label = '$V_{GS} = -1.75 V$')
plt.plot(Vds5[5:49], go5[5:49], label = '$V_{GS} = -2 V$')
plt.plot(Vds6[9:49], go6[9:49], label = '$V_{GS} = -2.25 V$')
pylab.xlim([-1,5])


plt.legend()
plt.show()