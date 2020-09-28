import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt
from math import exp

d=27
f = lambda x: 1-(x-(d/10))**2+exp(1.1-(1/d+2))
Dfdx = lambda x:(-2*(x-(d/10)+(1.1-(1/d+2))*x))


#Oppgave 1
# a)
# Siden f(-2) < 0 < f(2) kan man ihht. Intermediate value theorem
# argumentere for at det må finnes en verdi f(c) = 0 på intervallet [-2,2]
print('f(-2)= ', (f)(-2))
print('f(2)=  ', (f)(2))

# b)

#plot of f(x)
xpts = np.linspace(-2, 2, 1000)
plt.plot(xpts, f(xpts), label ='f(x)')
plt.axhline(f(2), linewidth=1, color='b', linestyle='--')
plt.axvline(2, linewidth=1, color='b', linestyle='--', label='b')
plt.axhline(f(-2), linewidth=1, color='r', linestyle='--')
plt.axvline(-2, linewidth=1, color='r', linestyle='--', label='a' )
plt.show()

# Oppgave 2
 # a)

 #halverings metoden:
halvering = opt.bisect(f, a=1.5, b=1.750, xtol=0.5e-8, full_output=True)
print(halvering)
print('')
print('')
print('Halverings metoden rundet ned til 7 desimalers nøyaktighet = '"%.7f" % halvering[0]+', ved 25 iterasjoner')

#sekant metoden:
def secant(f, x0, x1, tol, n):
    '''Tar inn f, x0, x1, tol(ønsket accuracy), n(antall iterasjoner) og returnerer approksimert x for funksjon'''
    for iteration in range(n):
        xnew = x1 - (x1-x0)/(f(x1)-f(x0))*f(x1)
        if abs(xnew-x1) < tol : break
        else:
            x0 = x1
            x1 = xnew
    else:print('reach max iteration reached')

    return xnew, iteration

print('')
print('')
print('Sekantmetoden: ',secant(f, x0=1 , x1=2, tol= 0.00001, n=100))
sekant2 = opt.newton(func=f,x0=1.5, tol=0.5e-7, full_output=True)
print('sekant2 ',sekant2)

#Newton method
Dfdx = lambda x:(-2*(x-(d/10)+(1.1-(1/d+2))*x))

newton=opt.newton(func=f,x0=1.5,fprime=Dfdx, tol=0.5e-7, full_output=True)
print('')
print('')
print('Newtons metode: ', newton)

