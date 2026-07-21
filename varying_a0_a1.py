#VARYING a0 - a1

import matplotlib.pyplot as plt #for scatter plot
import numpy as np 

def S(a0,a1):
  #function to find SSE for each a0,a1
    x=[1,2,3,4,5]
    y=[1,1,2,2,4]
    m=len(x)
  # x and y are the observations provided; m=length of observations 
    sse=0
    for i in range(0,m):
        ycap = a0 + (a1*x[i])
        err = y[i] - ycap
        sse = err**2 + sse
    # returning ONLY SSE
    return round(sse,4)

# range of a0 and a1 values
min_x= -20
max_x= 20
min_y= -20
max_y=20

# creates all combinations of a0 and a1
X, Y = np.meshgrid(np.arange(min_x/10, max_x/10+0.1, 0.1),
                   np.arange(min_y/10, max_y/10+0.1, 0.1))

# initializes Z array to store SSE values
Z = np.zeros_like(X)

# calculates SSE for every (a0, a1) pair
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i, j] = S(X[i, j], Y[i, j])
        

# creates a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # 3d surface

# plots the 3D surface (paraboloid)
ax.plot_surface(X, Y, Z)
plt.title("surface plot")
ax.set_xlabel("a0")
ax.set_ylabel("a1")
ax.set_zlabel("SSE")
#ax.view_init(elev=0, azim=25) # can change elevation angle (vertically) and azimuth angle (horizontally) 
plt.show() # SHOWS the surface plot
