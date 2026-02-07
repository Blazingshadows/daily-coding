import numpy as np
x = np.array([20,43,63,26,53,31,58,46,58,70,46,53,50,20,63,43,26,19,31,23])
y = np.array([120,128,141,126,134,128,136,132,140,144,128,136,146,124,143,130,124,121,126,123])
xy = np.prod(x,y)
x_2 = np.prod(x,x)
c = ((np.sum(y)*np.sum(x_2)) - (np.sum(x) * np.sum(xy)))/(20 *(np.sum(x_2) - (np.sum(x)*np.sum(x)))) 
m = (20 * (np.sum(xy) - (np.sum(x)*np.sum(y)))) / (20 *(np.sum(x_2) - (np.sum(x)*np.sum(x))))
print(m)
print(c)