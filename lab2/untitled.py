import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pylab
#gate is upper smu (1)
#drain is lower smu (2)
data = np.loadtxt("data/NFET_output_curve_partc.txt")
Id1 = data[:, 2]
Vds1 = data[:, 1]
go1 = Id1/Vds1

Id2 = data[:, 6]
Vds2 = data[:, 5]
go2 = Id2/Vds2

Id3 = data[:, 10]
Vds3 = data[:, 9]
go3 = Id3/Vds3

Id4 = data[:, 14]
Vds4 = data[:, 13]
go4 = Id4/Vds4

Id5 = data[:, 18]
Vds5 = data[:, 17]
go5 = Id5/Vds5

Id6 = data[:, 22]
Vds6 = data[:, 21]
go6 = Id6/Vds6



plt.figure()
plt.title("NFET Output Conductance")
plt.xlabel('$V_{DS}$')
plt.ylabel('$I_D$')

plt.plot(Vds1, go1, label = '$V_{GS} = -1 V$')
plt.plot(Vds2, go2, label = '$V_{GS} = -1.25 V$')
plt.plot(Vds3, go3, label = '$V_{GS} = -1.5 V$')
plt.plot(Vds4, go4, label = '$V_{GS} = -1.75 V$')
plt.plot(Vds5, go5, label = '$V_{GS} = -2 V$')
plt.plot(Vds6, go6, label = '$V_{GS} = -2.25 V$')
pylab.xlim([-1,5])


plt.legend()
plt.show()

