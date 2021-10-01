# Programs 17a: Plotting the Koch Square fractal.
# See Figure 17.2.

import numpy as np
import matplotlib.pyplot as plt
from math import floor

k=7
n_lines = 5**k      # Five segments.
h = 3**(-k);        # Each segment is one third length of previous.
x = [0]*(n_lines+1)
y = [0]*(n_lines+1)
x[0], y[0] = 0, 0
                                        
segment=[0] * n_lines;
        
# The angles of the four segments. 
angle=[0, np.pi/2, 0, -np.pi/2, 0]  # Five angles. 
for i in range(n_lines):
    m=i
    ang=0
    for j in range(k):
        segment[j] = np.mod(m, 5)     # Five segments.
        m = floor(m / 5)              # Five segments. 
        ang = ang + angle[segment[j]]
        
    x[i+1] = x[i] + h*np.cos(ang)
    y[i+1] = y[i] + h*np.sin(ang)

plt.axis('equal')
plt.plot(x,y)  
plt.show()