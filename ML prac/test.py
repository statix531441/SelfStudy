import network
import numpy as np

#making data
N = 1000
shape = (N,1)
height = np.random.randint(160,201,shape)
fit = np.random.randint(1,11,shape)
funny = np.random.randint(1,11,shape)

y = (height+2*fit+4*funny-210>=0).astype('int32')
data = np.hstack((height,fit,funny,y))
data

X_train = data[:,1:len(data)]
y_train = data[:,-1:]

net = network.NeuralNetwork([X_train.shape[1],y_train.shape[1]])
for i in range(100):
    net.train(X_train, y_train, 10, 10, 0.01)
net.plotProgress()
