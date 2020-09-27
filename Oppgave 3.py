import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt
from math import exp
from math import log10
d=27

f = lambda x: 1-(x-(d/10))**2+exp(1.1-(1/d+2))
Dfdx = lambda x:(-2*(x-(d/10)+(1.1-(1/d+2))*x))

tol = 0.5*10**(-7)

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

def secant_method(f, x0, x1, tol):
    '''Tar inn f, x0, x1, tol(ønsket accuracy), n(antall iterasjoner) og returnerer approksimert x for funksjon'''
    xnew = x1 - (x1-x0)/(f(x1)-f(x0))*f(x1)
    if abs(xnew-x1) < tol : break
    else:
        x0 = x1
        x1 = xnew

    yield xnew, iteration



data = np.array(list(bisection_method(f, a, b, tol)))
data2 = np.array(list(secant_method(f, x0, x1, tol)))
plt.plot(data[:,0], data[:,1])
plt.yscale('log')
plt.show()
print(data2)