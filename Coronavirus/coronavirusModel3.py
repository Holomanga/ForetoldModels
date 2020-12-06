from scipy.optimize import curve_fit
import numpy as np
from matplotlib import pyplot as plt

def linearPlusExponential(y,a,b,c,d):
	return np.minimum(a*np.exp(y/b),c*np.exp(y/d))

cases = [1,1,2,2,3,3,3,4,6,9,15,30,40,56,66,84,102,125,153,168,180,184,212,241,275,325,352,379,461,476,521,583,604,693,777,892,995,1113,1198,1378,1711,2047,2421,2742,3304,4257,5302,6676,8955,10640,11474]
date = range(12,63)

popt, pcov = curve_fit(linearPlusExponential,date,cases,p0=[1,1/0.16,0.02,1/0.304])

print(popt)

plt.scatter(date,cases)
plt.plot(np.linspace(12,100),linearPlusExponential(np.linspace(12,100),popt[0],popt[1],popt[2],popt[3]))
plt.yscale('log')
plt.show()

print(pcov)