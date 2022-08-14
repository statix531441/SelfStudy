import numpy as np
import math
import matplotlib.pyplot as plt

import fft
import gk


wave = [5,3,2,1,0,0,0,0]

plt.figure(0)
base = np.arange(0,len(wave))
fd1=np.array(fft.FFT(wave,4))
plt.plot(wave)
#plt.plot(base-4,abs(fd1), 'bo')
wave = [0.5,1,0.5,0,0,0,0,0]

plt.figure(1)
base = np.arange(0,len(wave))
fd2=np.array(fft.FFT(wave,4))
plt.plot(base-4,abs(fd2), 'bo')


fd3 = [0]*8
for i in range(8):
    fd3[i] = fd1[i]*fd2[i]

plt.figure(2)
wave3 = fft.iFFT(fd3,4)
plt.plot(wave3.real,'go')
print(wave3.real)

plt.show()





