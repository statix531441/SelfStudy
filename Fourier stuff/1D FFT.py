import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
import cv2

j = complex(0, 1)

N = 4
base = np.arange(0, N)

def empty(a):
    pass

#broadcast a function f to all elements of array
def broadcast(f, arr):
    ans = []
    for ele in arr:
        ans.append(f(ele))
    return np.array(ans)

def DFT(x,offset=0):
    N = len(x)
    X = np.zeros(N, dtype = complex)
    for k in range(N):
        amp = 0
        for n in range(N):
            amp += x[n] * cmath.exp(-j*2*math.pi*(k-offset)*n/N)
        X[k] = amp
    return X

def FFT(P, offset=0):
    N = len(P) #assuming this is a power of 2
    if N==1:
        return P

    w = cmath.exp(-j*2*math.pi/N)
    Pe,Po = P[::2],P[1::2]
    ye,yo = FFT(Pe,offset),FFT(Po,offset)
    
    y = [0]*N
    for k in range(int(N/2)):
        y[k] = ye[k] + (w**(k-offset))*yo[k]
        y[k+int(N/2)] = ye[k] - (w**(k-offset))*yo[k]
    return y

def iFFT(P,offset=0,summationCompleted=True):
    N = len(P) #assuming this is a power of 2
    if N==1:
        return P

    w = cmath.exp(j*2*math.pi/N)
    Pe,Po = P[::2],P[1::2]
    ye,yo = iFFT(Pe,offset,False),iFFT(Po,offset,False)
    
    y = [0]*N
    for n in range(int(N/2)):
        y[n] = ye[n] + (w**(n))*yo[n]
        y[n+int(N/2)] = ye[n] - (w**(n))*yo[n]

    if not summationCompleted:
        return np.array(y)
    
    temp = np.array(y)/N
    for n in range(len(temp)):
        temp[n] *= cmath.exp(-j*2*math.pi*n*offset/N)

    return temp

#Calculations
offset = 1

inp = [5,3,2,1]
dft = DFT(inp,offset)
fft = FFT(inp,offset)
ifft = iFFT(fft,offset)

fig = plt.figure(0, figsize = (7,7))

#inp
plt.subplot(2,2,1)
plt.plot(inp, 'ro')
plt.title("input")

#dft
plt.subplot(2,2,2)
plt.plot(base-offset,broadcast(abs,dft),'bo')
plt.title("dft")

#fft
plt.subplot(2,2,3)
plt.plot(base-offset,broadcast(abs,fft),'go')
plt.title("fft")

#ifft
plt.subplot(2,2,4)
plt.plot(np.array(ifft).real, 'mo')
plt.title("ifft")


plt.show()










