'''
Interpolation and Curve Fitting
Newton Forward Interpolation  
language: Python

Motahare Soltani
soltani.wse@gmail.com

'''

import numpy as np

def s_cal(s, n): 
	temp = s; 
	for i in range(1, n): 
		temp = temp * (s - i); 
	return temp; 

#Entering X and Y values
x = np.array([0, 2, 4, 6, 8, 10],float)
y = np.array([0.15, 1.56, 2.15, 2.60, 3, 3.30],float)

n = len(x)
p = np.zeros([n, n+1])

for i in range(n):
    p[i, 0] = x[i]
    p[i, 1] = y[i]

for i in range(2, n+1): 
	for j in range(n+1-i): 
		p[j][i] = p[j + 1][i - 1] - p[j][i - 1]

for i in range(n): 
	for j in range(n+1 - i): 
		print(round(p[i][j], 4), end = "\t") 
	print("")		

#Enter the point at which you want to calculate	 
z = float(input('Enter the point at which you want to calculate:'))

sum = p[0][1]
s = (z - x[0]) / (x[1] - x[0])

for i in range(1,n): 
	sum = sum + (s_cal(s, i) * p[0][i+1]) / np.math.factorial(i)

print("\nValue at", z, "is", round(sum, 6)) 