from matplotlib.patches import Ellipse,Rectangle
import matplotlib.pyplot as plt
import numpy as np
#import turtle as t
fig=plt.figure()
def plot_ellipse(x,y,a,b,angle,color,apha):
 #fig=plt.figure()
 ax=fig.add_subplot(111)
 #ax=plt.subplots()
 #ell1=Ellipse(xy = (0.0, 0.0), width = 0.8, height = 2, angle = 0, facecolor= 'yellow', alpha=0.3)
 ell1=Ellipse(xy = (x, y), width = a, height = b, angle = angle, facecolor= color, alpha=apha)
 ax.add_patch(ell1)

def plot_tangle(x,y,a,b,angle,color):
 #fig=plt.figure()
 ax=fig.add_subplot(111)
 #ax=plt.subplots()
 #ell1=Ellipse(xy = (0.0, 0.0), width = 0.8, height = 2, angle = 0, facecolor= 'yellow', alpha=0.3)
 tang1=Rectangle(xy = (x, y), width = a, height = b, angle = angle, facecolor= color)
 ax.add_patch(tang1)
 
'''def plot_tangle():
 t.seth(0)
 t.fd(100)
 t.seth(120)
 t.fd(100)
 t.seth(240)
 t.fd(100) 
 t.done()'''
plt.text(0, -0.5, "NEWBEE", size=9, rotation=0, color="brown",ha="center", va="center")
plt.text(0, 0, "GroupExercise", size=9, rotation=0, color="brown",ha="center", va="center")
#x,y=0,0
#ax.plot(x,y)
#leg 
plot_tangle(0,-0.6,0.75,0.75,45,'black')
plot_tangle(0,-0.8,0.7,0.7,45,'black')
plot_tangle(0,-1,0.65,0.6,45,'black')
#needle
plot_tangle(0,-1.2,0.2,0.2,45,'silver')
#body
plot_ellipse(0,0,0.8,2,0,'brown',1)
#head
plot_ellipse(0,1,0.8,1.3,0,'yellow',1)
#antenna
plot_tangle(0.2,1.5,0.3,0.1,45,'black')
plot_tangle(-0.15,1.55,0.3,0.1,135,'black')
#eyes
plot_tangle(-0.25,1,0.1,0.2,0,'black')
plot_tangle(0.15,1,0.1,0.2,0,'black')
#plot_ellipse(-0.2,1.15,0.2,0.4,45,'black',1)
#plot_ellipse(0.2,1.15,0.2,0.4,135,'black',1)
#mouth
plot_tangle(-0.05,0.5,0.1,0.2,0,'red')
#wing
#plot_ellipse(0.6,-0.8,0.3,2,30,'blue',0.1)
plot_ellipse(0.95,0.5,0.3,2,120,'blue',0.1)
plot_ellipse(0.6,0.8,0.3,2,150,'blue',0.1)
plot_ellipse(-0.6,0.8,0.3,2,30,'blue',0.1)
#plot_ellipse(-0.6,-0.8,0.3,2,150,'blue',0.1)
plot_ellipse(-0.95,0.5,0.3,2,60,'blue',0.1)
#bodys
plot_ellipse(0,0,0.81,0.3,0,'black',0.8)
plot_ellipse(0,-0.5,0.71,0.3,0,'black',0.8)
plt.axis('off')
plt.axis([-2,2,-2,2])
plt.show()