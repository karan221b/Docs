#import libraries
import tensorflow as tf
from keras.utils import np_utils
from keras.datasets import mnist
import seaborn as sns
from keras.initializers import RandomNormal
%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
import time

#function for updating plots for each each epoch and error
def plt_dynamic (x,vy, ty, ax, colors=['b']):
ax.plot (x, vy, 'b',label='Validation Loss')
ax.plot(x,vy, 'r',label='Trin Loss')
plt.legend()
plt.grid()
#fig.canvas.draw()

#train and test data
(X_train,y_train), (X_test,y_test)=mnist.load_data()

X_train=X_train.reshape(X_train.shape [0], X_train.shape [1]*X_train.shape[2])
X_test=X_test.reshape(X_test.shape [0],X_test.shape [1]*X_test.shape [2])

#print('Number of Training Examples:', X_ train. shape [0], 'and each image is of shape (%d,%d)' %(X_train.shape[1]*X_train.shape[2]))
#print('Number of Test Examples:', X_test.shape[0], 'and each image is of shape (%d,%d)' %(X_test.shape[1],X_test.shape[2]))
print('Number of Training Examples:',X_train.shape [0], 'and each image is of shape (%d)' %(X_train.shape[1]))
print('Number of Test Examples:',X_test.shape [0], 'and each image is of shape (%d)' %(X_test.shape[1]))

# example of data point
print(X_train[0])

# normalize the data
X_train=X_train/255
X_test=X_test/255
# example of data after normalization
print(X_train[0])

class number for each image
print('Class label of first image:',y_train[0])

# convert this into 10 decimal vector
Y_train=np_utils.to_categorical(y_train,10)
Y_test=np_utils.to_categorical(y_test,10)
print('After converting the output into a vector:',Y_train[0])

# build softmax classifier
from keras.models import Sequential
from keras.layers import Dense, Activation
#model=Sequential([Dense(32, input_shape=(784,)),
#Activation('relu'),Dense(10),Activation('softmax')])
#model parameters
output_dim=10
input_dim=X_train.shape[1]
batch_size=128
nb_epoch=20
#start building model
#from keras.layers import Activation, Dense
model=Sequential()
#model.add(Dense(64))
#model.add(Activation('tanh'))
model.add(Dense(output_dim,input_dim=input_dim, activation='softmax'))
print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)

# Configure the learning process
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
# train using fit()
history = model.fit(X_train, Y_train, batch_size=batch_size, epochs=nb_epoch, verbose=1, validation_data=(X_test, Y_test))

score=model.evaluate (X_test,Y_test, verbose=0)
print('Test Score',score [0])
print('Test Accuracy',score[1])
'''fig,ax=plt.subplot(1,1)
ax.set_xlabel('epoch');
ax.set_ylabel('Categorical Crossentropy Loss')

#List the epoc numbers
x=list(range(1, nb_epoch+1))
vy=history.history['val loss']
ty=history.history['loss']
plt_dynamic (x,uy,ty,ax)

# multilayer perceptron
model_sigmoid=Sequential()
model_sigmoid.add(Dense(512,activation='sigmoid', input_shape=(input_dim,)))
model_sigmoid.add(Dense(128, activation='sigmoid'))
model_sigmoid.add(Dense(output_dim,activation='softmax'))
model_sigmoid.summary()

model_sigmoid.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

history = model_sigmoid.fit(X_train, Y_train, batch_size=batch_size, epochs=nb_epoch, verbose=1, validation_data=(X_test, Y_test))

w_after = model_sigmoid.get_weights()
h1_w = w_after[0].flatten().reshape(-1,1)
h2_w = w_after[2].flatten().reshape(-1,1)
out_w = w_after[4].flatten().reshape(-1,1)
fig = plt.figure()
plt.title("Weight matrices after model trained")
plt.subplot (1, 3, 1)
plt.title("Trained model Weights")
ax = sns.violinplot (y=h1_w, color='b')
plt.xlabel('Hidden Layer 1')

plt.subplot (1, 3, 2)
plt.title("Trained model Weights")
ax = sns.violinplot (y=h2_w, color='r')
plt.xlabel('Hidden Layer 2 ')
plt.subplot (1, 3, 3)
plt.title("Trained model Weights")
ax = sns.violinplot (y=out_w,color='y')
plt.xlabel('Output Layer')
plt.show()
