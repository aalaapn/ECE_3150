import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pylab
#gate is upper smu (1)
#drain is lower smu (2)
data = np.loadtxt("data/diode_connected_NFET_partd.txt")
V = data[:,0]
I = data[:,1]
gd=np.array([])
for i in range(1,50):
	vds=(V[i+1]-V[i-1])
	
	g03 = (I[i+1]-I[i-1])/vds
	gd=np.append(gd,g03)
print(V.size)
gd=I/V
plt.figure()
plt.title("Diode-Connected NFET")
plt.xlabel("Applied Voltage ($V$)")
plt.ylabel("Differential Conductance $g_d$ $\Omega^-1$")

plt.plot(V,gd, label='$Diode$ $Connected$ $NFET$')
plt.legend()
plt.show()