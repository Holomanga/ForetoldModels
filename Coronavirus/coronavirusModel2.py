import numpy as np

from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern

cases = np.array([55,81.25,255,277.5,412.5,706.25,830,1407.5,2260,3121.25,3657.5,6986.25,9767.5,12273.75,14171.25,17492.5,21673.75,24845,29831.25,35332.5,38521.25,42971.25,46388.75,50167.5,53411.25,53895,56463.75,60412,66894,67193,71230,71449,75129,75304,76186,77272]).reshape(-1,1)
days = np.array(range(17,52+1)).reshape(-1,1)


plt.figure()

plt.scatter(days[:,np.newaxis], cases, c='r')

x = np.linspace(30,60,1000)
y = 179089.40730963 -5171390.48938843/x


plt.plot(x,y)

plt.show()