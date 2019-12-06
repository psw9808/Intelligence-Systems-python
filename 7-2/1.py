import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

name_file = './data_lab1_iis.txt'

columns = ['x','y']
data_in = pd.read_csv(name_file,names=columns,sep=' ')

data_in.plot(kind='scatter',x='x',y='y',color='red')  

x = np.asarray(data_in['x'])
y = np.asarray(data_in['y'])

plt.figure(5)
plt.plot(x,y,'ro')
plt.xlabel('x')
plt.ylabel('y')

a = np.array([[2,0],[0,2]])
b = np.array([[4,1],[2,2]])
c = np.matmul(a,b)
k = np.dot(a,b)
d = np.transpose(c)
e = np.linalg.inv(d)
