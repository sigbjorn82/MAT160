import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt
from math import exp
from math import log10
d=27

f = lambda x: 1-(x-(d/10))**2+exp(1.1-(1/d+2))
Dfdx = lambda x:(-2*(x-(d/10)+(1.1-(1/d+2))*x))

tol = 0.5e-7

a = 1.5
b = 2
x0 = 1
x1 = 2
# Oppgave 3
 # a)



def bisection_method(f, a, b, tol):
    if f(a)*f(b) > 0:
        #end function, no root.
        print("No root found.")
    else:
        iter = 0
        while (b - a)/2.0 > tol:
            midpoint = (a + b)/2.0
            yield iter, abs(f(midpoint))
            if f(a)*f(midpoint) < 0: # Increasing but below 0 case
                b = midpoint
            else:
                a = midpoint
            iter += 1

def newtons_method(f,Dfdx, x0, tol):
    iter = 0
    x1=x0-((f(x0))/(Dfdx(x0)))
    while abs(x1-x0) > tol:
        yield iter, f(x1)
        x0=x1
        iter += 1




data = np.array(list(bisection_method(f, a, b, tol)))
data2 = np.array(list(newtons_method(f,Dfdx, x0, tol)))
plt.plot(data[:,0], data[:,1])
plt.yscale('log')
plt.show()
print(data)
print(data2)