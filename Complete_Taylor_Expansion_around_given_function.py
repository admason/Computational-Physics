
# ## Complete Taylor Expansion around a given function:

import numpy as np
import matplotlib.pyplot as plt

####### select variables
h = float(input("Enter step size "))
x0 = int(input("Enter Arguement at which the derivatives will be calculated "))
nmax = int(input("Enter maximum iterations "))


########### Define the function (example given as 2sin(x)^2)

def func(x):
    return 2*np.sin(x)**2

######### For higher derivatives of nth degree
def nDerivative(f,x,h,n):
    # f: function
    # x: arguement
    # h: stepsize
    # n: order
    t=0
    for k in range(n+1):
        t= t + (-1)**(k+n)*np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k))*f(x + k*h)
    return t/h**n


########## Taylor Polynomial Code
def taylor(f, x , x0, nmax, h):
    # f: Function
    # x: argument
    # x0: argument at which derivative is calculated
    # nmax: n at which the series will terminate
    # h: stepsize
    t = 0
    for n in range(nmax+1):
        t = t + nDerivative(f,x0,h,n) * (x-x0)**n / np.math.factorial(n)
    return t

######### Plot the function and taylor series
plt.xlabel('x')
plt.ylabel('y')
plt.ylim([-5,5])
x_list = np.linspace(-5,5,101)
plt.scatter(x_list,func(x_list))

#nmax = 15
#h = 0.05

plt.plot(x_list, taylor(func,x_list,x0,nmax,h),'red')
plt.plot(x_list, taylor(func,x_list,x0+1,nmax,h),'green')
plt.plot(x_list, taylor(func,x_list,x0+2,nmax,h),'blue')
