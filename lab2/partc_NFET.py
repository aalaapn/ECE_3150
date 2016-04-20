import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pylab
#gate is upper smu (1)
#drain is lower smu (2)
data = np.loadtxt("data/NFET_output_curve_partc.txt")
Id1 = data[:, 2]
Vds1 = data[:, 1]

Id2 = data[:, 6]
Vds2 = data[:, 5]

Id3 = data[:, 10]
Vds3 = data[:, 9]

Id4 = data[:, 14]
Vds4 = data[:, 13]

Id5 = data[:, 18]
Vds5 = data[:, 17]

Id6 = data[:, 22]n
Vds6 = data[:, 21]

plt.figure()
plt.title("NFET Output Curve")
plt.xlabel('$V_{DS}$')
plt.ylabel('$I_D$')

plt.plot(Vds1, Id1, label = '$V_{GS} = 1 V$')
plt.plot(Vds2, Id2, label = '$V_{GS} = 1.25 V$')
plt.plot(Vds3, Id3, label = '$V_{GS} = 1.5 V$')
plt.plot(Vds4, Id4, label = '$V_{GS} = 1.75 V$')
plt.plot(Vds5, Id5, label = '$V_{GS} = 2 V$')
plt.plot(Vds6, Id6, label = '$V_{GS} = 2.25 V$')
plt.legend()
plt.show()