from math import *
import random



######################################################
# Method 1
def Bisection(fun , mmin , mmax , epsilon):

	a = 1
	while( fun(a) < 0 ):
		a = random.randint(mmin, mmax)
	b = 1
	while( fun(b) > 0):
		b = random.randint(mmin,mmax)

	count = 0
	while(abs(a-b) >= epsilon):
		count = count + 1

		c = (a+b)/2
		if ( fun(c) == 0):
			return c , count
		if ( fun(a) * fun(c) < 0):
			b = c
		else:
			a = c

	return (a+b)/2 , count

######################################################
#Method 2
def FlasePosition(fun , mmin , mmax , epsilon):

	a = 1 
	while( fun(a) < 0):
		a = random.randint(mmin , mmax)
	b = 1
	while( fun(b) > 0):
		b = random.randint(mmin , mmax)

	old = a
	new = b

	count = 0
	while( abs(new - old) >= epsilon):
		count = count + 1

		old = new 
		new = (a * fun(b) - b*fun(a) ) / (fun(b) - fun(a))

		if( fun(new) == 0):
			return new , count

		if( fun(a)*fun(new) < 0):
			b = new
		else:
			a = new

	return new,count

######################################################
#Method 3
def ModifyFalsePosition(fun, mmin, mmax, epsilon):

	a = 1
	while(fun(a) < 0 ):
		a = random.uniform(mmin,mmax)
	b = 1
	while(fun(b) > 0):
		b = random.uniform(mmin,mmax)

	old = a
	new = b
	tempa = fun(a)
	tempb = fun(b)

	count = 0

	while(abs(new - old) >= epsilon):
		count = count + 1

		old = new 
		new = (a*tempb - b*tempa)/(tempb-tempa)
		tempc = fun(new)

		if(tempc == 0):
			return new,count

		if(tempa * tempc < 0):
			b = new
			tempa = tempa / 2
			tempb = fun(b)
		else:
			a = new
			tempa = fun(a)
			tempb = tempb/2

	return new,count	
######################################################
#Method 4
def Secant(fun,mmin,mmax,epsilon):

	a = random.uniform(mmin,mmax)
	b = random.uniform(mmin,mmax)

	count = 0
	while( abs(a-b) >= epsilon):
		count = count + 1
		x = ( a*fun(b) - b*fun(a) )/(fun(b) - fun(a))
		a = b
		b = x

	return b ,count

######################################################
#Method 5
def Newton(fun, fundiff , mmin , mmax , epsilon):
	x = random.uniform(mmin,mmax)
	delta = -fun(x)/fundiff(x)

	count = 0
	while( abs(delta) >= epsilon):
		count = count + 1

		x = delta + x
		delta = -fun(x)/fundiff(x)

		if count == 10000:
			return x , count

	return x , count

######################################################
#Method 6
def FixedPoint(fun , mmin , mmax , epsilon):

	x = random.randint(mmin,mmax)
	old = x + 2 * epsilon

	count = 0
	while( abs(x - old ) >= epsilon):
		count = count + 1

		old = x
		x = fun(x)

	return x , count

######################################################


def fun1(x):
	if( abs(x) > 100 ):
		return inf
	return (exp(x) - 3*x*cos(2*x) - 8.3)
def fun1diff(x):
	if( abs(x) > 100 ):
		return inf
	return (exp(x) - 3*cos(2*x) - 6*x*sin(2*x))
def fun1G(x):
	if( abs(x) > 100 ):
		return inf
	return (8.3-exp(x))/(3*cos(2*x)) 	

mmin = -10
mmax = 2

firstfile = open("first.data","w")

for i in range (0,5):
	ans,count = Bisection(fun1,mmin,mmax,1e-8)
	print("---------------------------------------------------------------------------",file = firstfile)
	print("  Method                   X               F(X)          Times",file = firstfile)
	print("Bisection:          {:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= firstfile)
	
	ans,count = FlasePosition(fun1,mmin,mmax,1e-8)
	print("FlasePosition:      {:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= firstfile)
	
	ans,count = ModifyFalsePosition(fun1,mmin,mmax,1e-8)
	print("ModifyFalsePosition:{:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= firstfile)
	
	ans,count = Secant(fun1,mmin,mmax,1e-8)
	print("Secant:             {:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= firstfile)
	
	ans,count = Newton(fun1,fun1diff,mmin,mmax,1e-8)
	print("Newton:             {:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= firstfile)

	ans,count = FixedPoint(fun1G,mmin,mmax,1e-8)
	print("FixedPoint:{:+15.10f}   {:+15.10f}            {:>5d}" .format(ans, fun1(ans) , count), file= firstfile)
	print("---------------------------------------------------------------------------",file = firstfile)

######################################################

def fun2(x):
	if( abs(x) > 100 ):
		return inf
	return (exp(x*sin(x)) - x*cos(2*x) - 2.8)
def fun2diff(x):
	if( abs(x) > 100 ):
		return inf
	return (exp(x*sin(x)) * (sin(x) + x * cos(2*x) ) + 2*x*sin(x) )
def fun2G(x):
	if( abs(x) > 100 ):
		return inf
	return ((exp(x*sin(x)) - 2.8) / x*cos(2*x) )

mmin = -5
mmax = 5

secondfile = open("second.data","w")

for i in range (0,5):
	ans,count = Bisection(fun1,mmin,mmax,1e-8)
	print("---------------------------------------------------------------------------",file = secondfile)
	print("  Method                   X               F(X)          Times",file = secondfile)
	print("Bisection:          {:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= secondfile)
	
	ans,count = FlasePosition(fun1,mmin,mmax,1e-8)
	print("FlasePosition:      {:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= secondfile)
	
	ans,count = ModifyFalsePosition(fun1,mmin,mmax,1e-8)
	print("ModifyFalsePosition:{:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= secondfile)
	
	ans,count = Secant(fun1,mmin,mmax,1e-8)
	print("Secant:             {:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= secondfile)
	
	ans,count = Newton(fun1,fun1diff,mmin,mmax,1e-8)
	print("Newton:             {:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= secondfile)

	ans,count = FixedPoint(fun1G,mmin,mmax,1e-8)
	print("FixedPoint:{:+15.10f}   {:+15.10f}            {:>5d}" .format(ans, fun1(ans) , count), file= secondfile)
	print("---------------------------------------------------------------------------",file = secondfile)

######################################################

def fun3(x):
	if( abs(x) > 100 ):
		return inf
	return ( exp(sin(x)) + exp(cos(x)) )
def fun3diff(x):
	if( abs(x) > 100 ):
		return inf
	return ( exp(sin(x))* cos(x) ) - ( exp(cos(x)) * sin(x) )
def fun3G(x):
	if( abs(x) > 100 ):
		return inf
	return (exp(sin(x)))/(exp(cos(x)))

mmin = -10
mmax = 10

thirdfile = open("three.data","w")

for i in range (0,5):
	ans,count = Bisection(fun1,mmin,mmax,1e-8)
	print("---------------------------------------------------------------------------",file = thirdfile)
	print("  Method                   X               F(X)          Times",file = thirdfile)
	print("Bisection:          {:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= thirdfile)
	
	ans,count = FlasePosition(fun1,mmin,mmax,1e-8)
	print("FlasePosition:      {:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= thirdfile)
	
	ans,count = ModifyFalsePosition(fun1,mmin,mmax,1e-8)
	print("ModifyFalsePosition:{:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= thirdfile)
	
	ans,count = Secant(fun1,mmin,mmax,1e-8)
	print("Secant:             {:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= thirdfile)
	
	ans,count = Newton(fun1,fun1diff,mmin,mmax,1e-8)
	print("Newton:             {:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= thirdfile)

	ans,count = FixedPoint(fun1G,mmin,mmax,1e-8)
	print("FixedPoint:{:+15.10f}   {:+15.10f}            {:>5d}" .format(ans, fun1(ans) , count), file= thirdfile)
	print("---------------------------------------------------------------------------",file = thirdfile)

######################################################

def fun4(x):
	if( abs(x) > 100 ):
		return inf
	return (3*sin(x**2) + exp(cos(x**2)))
def fun4diff(x):
	if( abs(x) > 100 ):
		return inf
	return (6*x*cos(x**2)) - (2*exp())
def fun4G(x):
	if( abs(x) > 100 ):
		return inf
	return (3*sin(x**x))/(exp(cos(x**2)))

mmin = -10
mmax = 10

fourthfile = open ("four.data","w")

for i in range (0,5):
	ans,count = Bisection(fun1,mmin,mmax,1e-8)
	print("---------------------------------------------------------------------------",file = fourthfile)
	print("  Method                   X               F(X)          Times",file = fourthfile)
	print("Bisection:          {:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= fourthfile)
	
	ans,count = FlasePosition(fun1,mmin,mmax,1e-8)
	print("FlasePosition:      {:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= fourthfile)
	
	ans,count = ModifyFalsePosition(fun1,mmin,mmax,1e-8)
	print("ModifyFalsePosition:{:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= fourthfile)
	
	ans,count = Secant(fun1,mmin,mmax,1e-8)
	print("Secant:             {:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= fourthfile)
	
	ans,count = Newton(fun1,fun1diff,mmin,mmax,1e-8)
	print("Newton:             {:+15.10f}   {:+15.10f}   {:>5d}" .format(ans, fun1(ans) , count), file= fourthfile)

	ans,count = FixedPoint(fun1G,mmin,mmax,1e-8)
	print("FixedPoint:{:+15.10f}   {:+15.10f}            {:>5d}" .format(ans, fun1(ans) , count), file= fourthfile)
	print("---------------------------------------------------------------------------",file = fourthfile)

######################################################
