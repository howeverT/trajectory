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
x1=[]
y1=[]
alpha=[]
alphaAction=[]
for n in range(50):
 #alpha.append(np.random.uniform(0,1))
 alpha.append(0)
 #alphaAction.append(random.randint(0,1))
 alphaAction.append(1)

def set_alpha(alphaAction,alpha,i):
 #for i in range(50):
 if(alphaAction[i]==1):
  if(alpha[i]<0.95):
   alpha[i]+=0.001
  else:
   alphaAction[i]=0
 else:
  if(alpha[i]>0.2):
   alpha[i]-=0.1
  else:
   alphaAction[i]=1
 return alpha[i]

for n in range(100):
 x1.append(np.random.uniform(-100,100))
 y1.append(np.random.uniform(-100,100))
 

v0=float(input('input the initial speed:'))
x0=float(input('input the initial location of x:'))
y0=float(input('input the initial location of y:'))
#vx=input('input the initial speed of x:')
#vy=input('input the initial speed of y:')
a0=float(input('input the initial angle:'))

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
point,= plt.plot([x[0]], [y[0]], 'ro')


#plt.figure(facecolor=bg_color, edgecolor=fg_color)


def XandY():
 plt.xticks([-100,100])
 plt.yticks([-100,-4,100],[-100,'Earth',100])
 bx = plt.gca()
 bx.spines['right'].set_color('none')
 bx.spines['top'].set_color('none')
 bx.xaxis.set_ticks_position('none')
 bx.spines['bottom'].set_position(('data', 0))
 bx.yaxis.set_ticks_position('none')
 bx.spines['left'].set_position(('data',0))
 bx.spines['left'].set_color(fg_color)
 bx.spines['bottom'].set_color(fg_color)

 bx.patch.set_facecolor(bg_color)
 bx.xaxis.set_tick_params(color=fg_color, labelcolor=fg_color)
 bx.yaxis.set_tick_params(color=fg_color, labelcolor=fg_color)





def trajectory(vx,vy,ax,ay,t):
 #x.append(x0)
 #y.append(y0)
 for n in range(1,1000):
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

def update_point(n, x, y, x1 , y1 , point):
 point.set_xdata(np.array(x[n]))
 point.set_ydata(np.array(y[n]))
 #plt.cla()
 for i in range(50):
  plt.plot(x1[i],y1[i],c='w',marker='o',markersize=2,alpha=set_alpha(alphaAction,alpha,i))
 return point

XandY()
plt.plot(0,0,'bo')
'''for n in range(130):
 plt.scatter(x1[n],y1[n],c='w',s=2)'''
trajectory(vx,vy,ax,ay,t)
plt.axis([-100,100,-100,100])
ani=animation.FuncAnimation(fig, update_point, 1000, interval=1, fargs=(x, y, x1 ,y1 , point))
plt.show()
