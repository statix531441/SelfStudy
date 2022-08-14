import numpy as np
import math
import matplotlib.pyplot as plt

import fft
j = complex(0,1)

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

b = np.array([[1,2,0],
              [3,4,0],
              [0,0,0]])

fd1 = fft.FFT2D(a)
fd2 = fft.FFT2D(b)

fd3 = []

for m in range(4):
    temp = []
    for n in range(4):
        temp.append(fd1[m][n]*fd2[m][n])
    fd3.append(temp)

c = fft.iFFT2D(fd3)


#this is how you can pad after finding which power of 2 you wanna make
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
z = np.zeros((4,4))
z[:3,:3] = a
