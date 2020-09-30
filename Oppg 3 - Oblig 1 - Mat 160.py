import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt
from math import exp
from math import log10

d=27
f = lambda x: 1-(x-(d/10))**2+exp(1.1-(1/(d+2)))
Dfdx = lambda x:(-2*(x-(d/10)+(1.1-(1/(d+2))*exp(1.1-(1/(d+2))*x)))

tol = 0.5e-7

a = 1.5
b = 2
x0 = 1
x1 = 2
# Oppgave 3
 # a)


#Iteration
def bisection_method(f, a, b, tol):
    if f(a) * f(b) > 0:
        # end function, no root.
        print("No root found.")
    else:
        iter = 0
        while (b - a) / 2.0 > tol:
            midpoint = (a + b) / 2.0
            yield iter, abs(f(midpoint))
            if f(a) * f(midpoint) < 0:  # Increasing but below 0 case
                b = midpoint
            else:
                a = midpoint
            iter += 1


def sekant_method(f, x0, x1, tol):
    i = 0
    while abs((x1 - (x1 - x0) / (f(x1) - f(x0)) * f(x1)) - x1) > tol:
        xnew = x1 - (x1 - x0) / (f(x1) - f(x0)) * f(x1)
        yield i, xnew
        x0 = x1
        x1 = xnew
        i += 1


def newtons_method(f, Dfdx, x0, tol):
    i = 0
    while abs((x0 - f(x0) / Dfdx(x0)) - x0) > tol:
        x1 = x0 - f(x0) / Dfdx(x0)
        print(i, x1)
        x0 = x1
        i += 1


#iteration arrays
data_B = np.array(list(bisection_method(f, a, b, tol)))
data_S = np.array(list(sekant_method(f, x0, x1, tol)))
data_N = np.array(list(newtons_method(f, Dfdx, x1, tol)))


#error
r_sann = opt.brentq(f, a=1.5, b=1.750, full_output=True)

error_bisection = np.array([abs(r_sann[0]-x) for x in data_B[0]])
error_newton = list([abs(r_sann[0]-x) for x in data_N[0]])
error_sekant = np.array([abs(r_sann[0]-x) for x in data_S[0]])


#plot of
#plt.ylabel('Absolutt Error')
#plt.xlabel('Iterasjoner')
#plt.plot(error_bisection[:,0], list(1,len(error_bisection)))
#plt.plot(error_newton[:,0], error_newton[:,1])
#plt.plot(error_sekant[:,0], error_sekant[:,1])
#plt.yscale('log')
#plt.show()


error_newton
