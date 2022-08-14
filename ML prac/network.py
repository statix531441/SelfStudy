import numpy as np
import matplotlib.pyplot as plt

def squish(z):
    a = 1/(1+np.exp(-z))
    return a

def squishprime(z):
    fprime = np.multiply(squish(z),(1-squish(z)))
    return fprime

class NeuralNetwork():
    #lis contains sizes of each layer
    def __init__(self, lis): 
        
        self.n = len(lis) # number of layers in total
        self.reset()
        self.WML = [[[0]] ] #dummy weight matrix associated with first layer
        self.BL = [[[0]] ] #dummy bias matrix/list associated with first layer
        self.Jprogress = []
        
        #initialize random weight matrices here...
        for i in range(len(lis)-1):  
            #random weight matrix per layer
            shape = (lis[i], lis[i+1])
            wm = np.random.randn(lis[i], lis[i+1])
            self.WML.append(wm)
            #random biases per layer
            b = np.random.randn(1, lis[i+1])
            self.BL.append(b)
            
    def reset(self):
        
        self.AL = [] #list of layer activations
        self.FprimeL = [[] ] #AL0 does not have z value to find fprime
        self.DL = [[[]] ] #AL0 does not have delta values       
        self.err =[[]]
        self.C =[]
        self.J = 0
    
    def forward(self, X):
        
        self.reset()
        self.AL.append(X)
        for i in range(self.n-1):
            wm = self.WML[i+1]
            b = self.BL[i+1]
            z = np.matmul(self.AL[i], wm) + b
            a = squish(z)
            fp = squishprime(z)
            self.AL.append(a)
            self.FprimeL.append(fp)
        return self.AL[-1]
        
    def backward(self, Y):
        
        for i in range(1, self.n):
            #i = 1 represents the last layer L
            #then you count backwards
            #E = dC/da
            if(i == 1):
                E = self.AL[-1] - Y
            else:
                wm = self.WML[-i + 1]  #weights of l+1 layer
                E = np.matmul(self.DL[1], wm.T) #propogated errors
            f = self.FprimeL[-i]
            d = np.multiply(f, E)
            self.DL.insert(1, d)

    def updateWeights(self, alpha=0.2):
        
        for i in range(1, self.n):
            al1 = self.AL[i-1]
            dl2 = self.DL[i]
            T = len(dl2) #number of training samples in batch
            changeInWeights = np.matmul(al1.T, dl2)/T
            changeInBiases = np.matmul(np.ones(len(dl2)).reshape(1,len(dl2)), dl2)/T
            
            self.WML[i] = self.WML[i] - alpha*changeInWeights
            self.BL[i] = self.BL[i] - alpha*changeInBiases         
        
    def batchTrain(self, X, Y, alpha):
        self.forward(X)
        self.backward(Y)
        self.updateWeights(alpha)
        
    def plotProgress(self):
        plt.plot(self.Jprogress, 'ro', ms=2)
        plt.xlabel('Epoch')
        plt.ylabel('Cost')
        plt.title('Cost progress with each epoch')
        plt.show()

    def train(self, X, Y, batchSize=10, epochs=1, alpha=0.2):
        
        for epoch in range(epochs):
            for i in range(0, len(X), batchSize):
                if(i+batchSize<len(X)):
                    Xbatch = X[i:i+batchSize]
                    Ybatch = Y[i:i+batchSize]
                else:
                    Xbatch = X[i:]
                    Ybatch = Y[i:]
                    
                self.batchTrain(Xbatch, Ybatch, alpha)
                
            self.Jprogress.append(self.cost(X, Y))

    def cost(self, X, Y):
            err = self.forward(X) - Y
            err2 = err**2
            C = [sum(i) for i in err2/2] # C[t] gives cost of a sample
            J = sum(C)/len(X) #total cost after running a batch
            return J

    def classify(self, X):
        return (self.forward(X)>0.5).astype('int32')
