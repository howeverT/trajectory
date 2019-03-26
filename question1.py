import matplotlib.pyplot as plt
import numpy as np
import math
plt.figure()
t=0.1
#G=6.67*10^-11
#M=5.965*10^24
v0=input('input the initial speed:')
x0=input('input the initial location of x:')
y0=input('input the initial location of y:')
a0=input('input the initial angle:')

def XandY():
 plt.xticks([-100,100])
 plt.yticks([-100,-4,100],[-100,'Earth',100])
 ax = plt.gca()
 ax.spines['right'].set_color('none')
 ax.spines['top'].set_color('none')
 ax.xaxis.set_ticks_position('none')
 ax.spines['bottom'].set_position(('data', 0))
 ax.yaxis.set_ticks_position('none')
 ax.spines['left'].set_position(('data',0))
  
  
  
def trajectory(x0,y0,t):
 #x=x0
 #y=y0
 x=[]
 y=[]
 x.append(x0)
 y.append(y0)
 for n in xrange(1,1000):
  z=np.sqrt(x[n-1]*x[n-1]+y[n-1]*y[n-1])
  #a=G*M/(z*z)
  #x.append(x0+v0*t*(abs(x[0])/z))
  #y.append(y0+v0*t*(abs(y[0])/z))
  x.append(x0+v0*t*np.cos(math.radians(a0)))
  y.append(y0+v0*t*np.sin(math.radians(a0)))
  t=t+0.1
  #x=np.linspace(-100,100,100)
  #y=x+1
  #plt.plot(x,y,'ro')
  plt.plot(x,y)

  
XandY()
trajectory(x0,y0,t)
plt.axis([-100,100,-100,100])
plt.show()
  
