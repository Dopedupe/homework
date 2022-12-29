import matplotlib.pyplot as plt 
import numpy as np  
from scipy import integrate
from math import sqrt
import warnings

warnings.filterwarnings('ignore')

x = np.arange(0, 5.5, 0.5) 

x0 = 3      
f = pow((2*x-3),2)*np.sin(pow(x,2)+2)

def func(x):
    return pow((2*x-3),2)*np.sin(pow(x,2)+2)

def find_max(x, max): 
    for i in x: 
        if max == pow((2*i-3),2)*np.sin(pow(i,2)+2): 
            return i 

def find_min(x, min): 
    for i in x: 
        if min == pow((2*i-3),2)*np.sin(pow(i,2)+2): 
            return i 

def first_d(x):
    return (8*x-12) * np.sin(pow(x,2)+2) + pow((2*x-3),2) * 2*x*np.cos(pow(x,2)+2) 

def length(x):
 return sqrt(1+(first_d(x)**2))
result, xz = integrate.quad(length, 0, 5)
print('Длина кривой через интеграл =',result)

def line(x, x0, y0):
    return first_d(x0)*(x - x0) + y0

def xr(c):
    xrange = np.linspace(c-1, c+1)
    return xrange

def tan(c):
    d = func(c)
    plt.scatter(c, d, s=10)
    plt.plot(xr(c), line(xr(c), c, d), '--', linewidth = 1)

normal =  (func(x0) - 1 / (first_d(x0)) * (x-x0))
fd = (8*x-12) * np.sin(pow(x,2)+2) + pow((2*x-3),2) * 2*x*np.cos(pow(x,2)+2) 
sd = 2*(20*x**2-36*x+9)*np.cos(x**2+2)+4*(-4*x**4+12*x**3-9*x**2+2)*np.sin(x**2+2) 

ax1 = plt.subplot(221) 
plt.plot(x,f,'b')
plt.plot(find_max(x, max(f)), max(f),'or') 
plt.plot(find_min(x, min(f)), min(f),'or') 
plt.plot(x,normal,'--r')
plt.title("Function") 
plt.grid() 
 
ax2 = plt.subplot(222) 
plt.plot(x,fd, 'b')
plt.title("1DFunction") 
plt.grid() 
 
ax3 = plt.subplot(223) 
plt.plot(x,sd, 'b')
plt.title("2DFunction") 
plt.grid() 

ax4 = plt.subplot(224) 
plt.plot(x, func(x), 'b')
tan(0), tan(1), tan(3), tan(5)
plt.xlim(0, 6) 
plt.ylim(-40,50) 
plt.title("Tangent") 
plt.grid() 

plt.show()