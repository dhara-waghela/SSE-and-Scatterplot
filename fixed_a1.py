#FIXED a1

import matplotlib.pyplot as plt #for scatter plot
import numpy as np 

def S(a1):
  #function to find SSE for each a1
    x=[1,2,3,4,5]
    y=[1,1,2,2,4]
    m=len(x)
  # x and y are the observations provided; m=length of observations 
    sse=0
    for i in range(0,m):
        ycap = (-0.1) + (a1*x[i])
        err = y[i] - ycap
        sse = err**2 + sse
    # returning list for answer
    return [a1,round(sse,4)]

minimum=-20
maximum=20
xcord=[] # a0 on X axis
ycord=[] # sse on Y axis
for i in range(minimum, maximum+1):
    answer=S(i/10)
    xcord.append(answer[0]) # gets a0 / can be "xcord.append(i/10)"
    ycord.append(answer[1]) # gets sse
"""
for i in range(len(xcord)):
    print(xcord[i],ycord[i],sep=" , ")
    #printing values for reference
"""
# using numpy to make arrays
x1 = np.array([i for i in xcord])
y1 = np.array([i for i in ycord])

plt.scatter(x1, y1) # MAKES the scatter plot
plt.title("S(-0.1,a1)") 
plt.xlabel("a1")
plt.ylabel("SSE")
plt.show() # SHOWS the scatter plot
