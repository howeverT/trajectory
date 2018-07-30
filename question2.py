import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import animation
bg_color = 'black'
fg_color = 'white'
fig=plt.figure(facecolor=bg_color, edgecolor=fg_color)
t=0.1
G=6.67*10**-11
M=5.965*10**24
D=G*M*10**-13
v0=input('input the initial speed:')
x0=input('input the initial location of x:')
y0=input('input the initial location of y:')
#vx=input('input the initial speed of x:')
#vy=input('input the initial speed of y:')
a0=input('input the initial angle:')

x=[]
y=[]
x.append(x0)
y.append(y0)
z=np.sqrt(x0**2+y0**2)
a=D/(z*z)
vx=v0**np.cos(math.radians(a0))
vy=v0**np.sin(math.radians(a0))
ax=a*(abs(x[-1])/z)
ay=a*(abs(y[-1])/z)
point,= plt.plot([x[0]], [y[0]], 'o')


#plt.figure(facecolor=bg_color, edgecolor=fg_color)


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
 ax.spines['left'].set_color(fg_color)
 ax.spines['bottom'].set_color(fg_color)

 ax.patch.set_facecolor(bg_color)
 ax.xaxis.set_tick_params(color=fg_color, labelcolor=fg_color)
 ax.yaxis.set_tick_params(color=fg_color, labelcolor=fg_color)





def trajectory(vx,vy,ax,ay,t):
 #x.append(x0)
 #y.append(y0)
 for n in xrange(1,1000):
  z=np.sqrt(x[-1]*x[-1]+y[-1]*y[-1])
  #print(z,a)
  #print(a)
  x.append(x[-1]+vx*t+0.5*ax*t*t)
  y.append(y[-1]+vy*t+0.5*ay*t*t)
  z=np.sqrt(x[-1]**2+y[-1]**2)
  a=D/(z*z)
  ax=a*((-x[-1]/z))
  ay=a*((-y[-1]/z))
  vx=vx+ax*t
  vy=vy+ay*t
  #print(0.5*a*t*t*(-x[-1]/z),0.5*a*t*t*(-y[-1]/z),z,x[:-1],y[:-1])
  #print(v0*t*np.cos(math.radians(a0)))
  #print(v0*t*np.sin(math.radians(a0)))
 plt.plot(x,y)

def update_point(n, x, y, point):
 point.set_xdata(np.array(x[n]))
 point.set_ydata(np.array(y[n]))
 return point

XandY()
plt.plot(0,0,'ro')
trajectory(vx,vy,ax,ay,t)
plt.axis([-100,100,-100,100])
ani=animation.FuncAnimation(fig, update_point, 1000, interval=10, fargs=(x, y, point))
plt.show()
