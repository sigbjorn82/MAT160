import matplotlib as plt
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt
from math import exp
d=27

f = lambda x: 1-(x-(d/10))**2+exp(1.1-(1/d+2))
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
halvering = opt.bisect(f, a=1.5, b=2.0, rtol=1.0e-8, full_output=True)
print(halvering)
print('rundet ned til 7 desimalers nøyaktighet = '"%.7f" % halvering[0]+', ved 25 iterasjoner')