import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pylab
#gate is upper smu (1)
#drain is lower smu (2)
data = np.loadtxt("data/PFET_threshold_partg.txt")
Id1 = data[:, 3]
Vds1 = data[:, 2]
go1 = Id1/Vds1

Id2 = data[:, 8]
Vds2 = data[:, 7]
go2 = Id2/Vds2

Id3 = data[:, 13]
Vds3 = data[:, 12]
go3 = Id3/Vds3

Id4 = data[:, 18]
Vds4 = data[:, 17]
go4 = Id4/Vds4

Id5 = data[:, 23]
Vds5 = data[:, 22]
go5 = Id5/Vds5

Id6 = data[:, 28]
Vds6 = data[:, 27]
go6 = Id6/Vds6

Id7 = data[:, 33]
Vds7 = data[:, 32]
go7 = Id7/Vds7

plt.figure()
plt.title("PFET Output Curve")
plt.xlabel('$V_{DS}$')
plt.ylabel('$I_D$')

#plt.plot(Vds1, Id1, label = '$V_{GS} = -1 V$')
plt.plot(Vds2, Id2, label = '$V_{GS} = -1 V$')
plt.plot(Vds3, Id3, label = '$V_{GS} = -1.25 V$')
plt.plot(Vds4, Id4, label = '$V_{GS} = -1.5 V$')
plt.plot(Vds5, Id5, label = '$V_{GS} = -1.75 V$')
plt.plot(Vds6, Id6, label = '$V_{GS} = -2 V$')
plt.plot(Vds7, Id7, label = '$V_{GS} = -2.25 V$')

plt.legend()
plt.show()