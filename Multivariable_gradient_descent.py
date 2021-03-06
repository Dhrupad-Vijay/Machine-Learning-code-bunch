#==================================================================================================================
#==================================================================================================================
#---------------------House price prediction using Multivariable gradient descent algorithm------------------------ 
#==================================================================================================================
#==================================================================================================================
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

path = open('/content/gdrive/MyDrive/Colab Notebooks/ML work/House cost data2.csv')             # Enter the file path
array = np.loadtxt(path, delimiter=",",dtype = 'int')
no_fetures = len(array[0])-1
x = array[:,0:no_fetures]
y = np.transpose([array[:,no_fetures]])

theta = np.zeros((len(x[0])+1,1)) # theta is a n X 1 matrix

# Normalization function
def normalize(x):
    mu = x.mean(axis = 0)
    temp1 = x-mu
    sigma = np.std(temp1,axis = 0)
    temp2 = temp1/sigma
    X = np.c_[np.ones((len(x),1)),temp2]       # X is a m X n matrix
    na = [X,mu,sigma]
    return na

# Cost Function
def cost(X, y, theta):
    l = len(y)
    err = np.sum(np.power((np.dot(X,theta) - y), 2))
    cc = (1/(2*l))*(err)
    return cc

# Gradient descent
def grad_dec(X,y,theta,alpha,num_iter):
    l = len(y)

    for i in range(1,num_iter+1):

        err = np.dot(X,theta) - y
        theta = theta - (alpha/l)*(np.dot(np.transpose(X),err))
    return theta

temp3 = normalize(x)
alpha = 0.1
num_iter = 1000
theta = grad_dec(temp3[0],y,theta,alpha,num_iter)

inp = np.zeros((1,no_fetures))

print('===============================================================================')
print('===============================================================================\n')
print('############### Welcome to the House price prediction algorithm ###############')
print('                         Location :- Portland Oregon\n')
print('===============================================================================')
print('===============================================================================\n')

print('Enter the values of the House Parameters (Area ; Number of rooms ; Age of house)\n')
for i in range(0,no_fetures):
    inp[0][i] = int(input('           ---------> '))

print('\n===============================================================================')
print('===============================================================================\n')

temp5 = (inp - temp3[1])/temp3[2]
i_price = np.dot(np.c_[1,temp5],theta)

print('The approximate price of your desired house is = ',round(((i_price[0][0])/1000),3),' Thousand Dollars')
print('\n=============================:==:==:==:==:=====================================')
