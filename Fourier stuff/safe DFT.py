import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
import cv2

N = 101

j = complex(0, 1)
base = np.arange(0, N)

def empty(a):
    pass

cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar', 640, 280)
cv2.createTrackbar('offset', 'Trackbar', (N-1)//2, N, empty)
cv2.createTrackbar('freq1', 'Trackbar', 2, 20, empty)
cv2.createTrackbar('freq2', 'Trackbar', 5, 20, empty)



offset = (N-1)//2
freq1 = 2 
freq2 = 5



#broadcast a function f to all elements of array
def broadcast(f, arr):
    ans = []
    for ele in arr:
        ans.append(f(ele))
    return np.array(ans)


#Xk is the fourier transform value of the wave of frequency = k-offset

def DFT(x):
    N = len(x)
    X = np.zeros(N, dtype = complex)
    for k in range(N):
        amp = 0
        for n in range(N):
            amp += x[n] * cmath.exp(-j*2*math.pi*(k-offset)*n/N)
        X[k] = amp
    return X

def iDFT(X):
    N = len(X)
    x = np.zeros(N, dtype = complex)
    for n in range(N):
        val = 0
        for k in range(N):
            val += X[k] * cmath.exp(j*2*math.pi*(k-offset)*n/N)
        x[n] = val/N
    return x

fig = plt.figure(0, figsize = (7,7))
f1=freq1
f2=freq2
ofs=offset

flag = False
while True:
    
    f1 = cv2.getTrackbarPos('freq1','Trackbar')
    f2 = cv2.getTrackbarPos('freq2','Trackbar')
    ofs = cv2.getTrackbarPos('offset','Trackbar')
    
    if not (flag==1 and f1==freq1 and f2==freq2 and ofs==offset):
        
        fig.clear(True)
        flag = True
        freq1 = f1
        freq2 = f2
        offset = ofs

        x = np.sin(2*cmath.pi*freq1*base/N) + np.sin(2*cmath.pi*freq2*base/N)
        X = DFT(x)
        Xamp = broadcast(abs, X)
        Xphase = broadcast(cmath.phase, X)
        x_idft = iDFT(X).real

        #fig1
        plt.subplot(2, 2, 1)
        plt.plot(x, color = 'b')
        plt.title('x(n)')

        #fig2
        plt.subplot(2, 2, 2)
        plt.xlim(base[0]-offset,base[N-1]-offset)
        plt.plot(base-offset, Xamp, color = 'b')
        plt.title('Xamp(k-offset)')

        #fig3
        plt.subplot(2, 2, 3)
        plt.xlim(base[0]-offset,base[N-1]-offset)
        plt.plot(base-offset, Xphase, color = 'b')
        plt.title('Xphase(k-offset)')

        #fig4
        plt.subplot(2,2,4)
        plt.plot(x_idft, color = 'g')
        plt.title("iDFT(X)")

    plt.draw()
    plt.pause(0.1)

    key = cv2.waitKey(1)
    
    if key==ord('q'):
        print('ggez')
        break

plt.close(fig)
cv2.destroyAllWindows()
exit()
























