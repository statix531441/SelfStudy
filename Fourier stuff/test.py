import numpy as np
import math
import matplotlib.pyplot as plt

import fft
import gk


#Making images and shiz
N = 16
wave1 = np.zeros((N,N))
wave2 = np.zeros((N,N))

xf = 4
yf = 0
for row in range(len(wave1)):
    for col in range(len(wave1[0])):
        wave1[col][row] = 0.5*(1+math.sin(2*math.pi*(row*xf + col*yf)/N))

xf = 1
yf = 4
for row in range(len(wave2)):
    for col in range(len(wave2[0])):
        wave2[col][row] = 0.5*(1+math.sin(2*math.pi*(row*xf + col*yf)/N))

wave = wave1

N = 16
shape = (N,N)
sig = 8

wave = gk.Gkernel(shape,sig)


#Calculation stuff

fd = fft.FFT2D(wave,(N-1)//2,(N-1)//2)
wave_rec = fft.iFFT2D(fd,(N-1)//2,(N-1)//2)

#plotting things
plt.figure(0)
ax = plt.gca()
ax.set_xticks(np.arange(-0.5,N,1))
ax.set_yticks(np.arange(-0.5,N,1))
ax.set_xticklabels(np.arange(0,N+1))
ax.set_yticklabels(np.arange(0,N+1))
plt.grid()
plt.imshow(wave)

plt.figure(1)
ax = plt.gca()
ax.set_xticks(np.arange(-0.5,N,1))
ax.set_yticks(np.arange(-0.5,N,1))
ax.set_xticklabels(np.arange(-(N-1)//2,(N-1)//2 +2))
ax.set_yticklabels(np.arange(-(N-1)//2,(N-1)//2 +2))
plt.grid()
plt.imshow(abs(fd))
plt.pause(0.1)

##plt.figure(2)
##ax = plt.gca()
##ax.set_xticks(np.arange(-0.5,N,1))
##ax.set_yticks(np.arange(-0.5,N,1))
##ax.set_xticklabels(np.arange(0,N+1))
##ax.set_yticklabels(np.arange(0,N+1))
##plt.imshow(wave_rec)
##plt.grid()

plt.show()
