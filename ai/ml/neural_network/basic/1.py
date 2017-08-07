import numpy as np
import random

def test(elem_size,size=100):
 print('testing.......')
 X,y = gendata(elem_size,size)
 result = pridict(X)
 count = 0
 for i in range(len(result)):
  cat = 1 if result[i] > 0.5 else 0
  if y[i] == cat:
   count = count + 1
 print('accuracy:',count*100/size)
 
def gendata(elem_size,data_size):
 total_data_size = 2**elem_size
 #Xmainarray = [[0 for x in range(elem_size)] for y in range(data_size)]
 #Ymainarray = [[0 for x in range(1)] for y in range(data_size)]
 Xmainarray = np.zeros(shape=(data_size,elem_size))
 Ymainarray = np.zeros(shape=(data_size,1))
 for i in range(data_size):
  array = []
  array = map(int,list(bin(random.randint(0,total_data_size-1))[2:]))
  array = [0]*(elem_size - len(array))+array
  category = 1 if array.count(1) > elem_size/2 else 0
  Xmainarray[i] = array
  Ymainarray[i][0] = category
 #print Xmainarray
 #Xmainarray = np.array(Xmainarray)
 #Ymainarray = np.array(Ymainarray)
 return  Xmainarray,Ymainarray
#Input array
X,y=gendata(5,16)

#Sigmoid Function
def sigmoid (x):
 return 1/(1 + np.exp(-x))

#Derivative of Sigmoid Function
def derivatives_sigmoid(x):
 return x * (1 - x)

#Variable initialization
epoch=5000 #Setting training iterations
lr=0.1 #Setting learning rate
inputlayer_neurons = X.shape[1] #number of features in data set
hiddenlayer_neurons = 6 #number of hidden layers neurons
output_neurons = 1 #number of neurons at output layer

#weight and bias initialization
wh=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bh=np.random.uniform(size=(1,hiddenlayer_neurons))
wout=np.random.uniform(size=(hiddenlayer_neurons,output_neurons))
bout=np.random.uniform(size=(1,output_neurons))

for i in range(epoch):

 #Forward Propogation
 hidden_layer_input1=np.dot(X,wh)
 hidden_layer_input=hidden_layer_input1 + bh
 hiddenlayer_activations = sigmoid(hidden_layer_input)
 output_layer_input1=np.dot(hiddenlayer_activations,wout)
 output_layer_input= output_layer_input1+ bout
 output = sigmoid(output_layer_input)

 #Backpropagation
 E = y-output
 slope_output_layer = derivatives_sigmoid(output)
 slope_hidden_layer = derivatives_sigmoid(hiddenlayer_activations)
 d_output = E * slope_output_layer
 Error_at_hidden_layer = d_output.dot(wout.T)
 d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
 wout += hiddenlayer_activations.T.dot(d_output) *lr
 bout += np.sum(d_output, axis=0,keepdims=True) *lr
 wh += X.T.dot(d_hiddenlayer) *lr
 bh += np.sum(d_hiddenlayer, axis=0,keepdims=True) *lr

def pridict(X):
 hidden_layer_input1=np.dot(X,wh)
 hidden_layer_input=hidden_layer_input1 + bh
 hiddenlayer_activations = sigmoid(hidden_layer_input)
 output_layer_input1=np.dot(hiddenlayer_activations,wout)
 output_layer_input= output_layer_input1+ bout
 output = sigmoid(output_layer_input)
 return output

test(5)
