import matplotlib.pyplot as plt
import numpy as np

def LeastSquare(DATAX,DATAY):

	OUT = open("output.out","w")

	Error = list()

	for k in range(2,len(DATAX)+6):

		print("p{}(X)".format(k),file = OUT)

		A = np.zeros(k*k).reshape(k,k)
		B = np.zeros(k)

		for i in range(k):
			for j in range(k):
				for x in DATAX :
					A[i,j] = A[i,j] + x**(i+j)
		for i in range(k):
			for j in range(len(DATAX)):
				B[i] = B[i] + DATAY[j]*(DATAX[j]**i)

		x = np.linalg.solve(A,B)


		NAns = list()
		for i in range(len(DATAY)):
			ans = 0
			for j in range(k):
				ans = ans + x[j]*(DATAX[i]**j)
			NAns.append(ans)

		print("[ ",end = "",file = OUT)
		for z in x:
			print("{0:3.8f}".format(z),end = ", ",file = OUT)
		print(" ]",file = OUT)

		error = 0 
		flag = True
		for i in range(len(DATAY)):
			error = error + (NAns[i] - DATAY[i])**2

		print("Error : {0:3.8f}".format(error),file = OUT)

		# if len(Error) > 0:
		# 	if Error[-1]/error < 2.0:
		# 		print("The best choice is",format(k - 1) ,file = OUT)
		# 		flag = False
		print("#################################",file = OUT)

		Error.append(error)

		plt.cla()
		plt.clf()
		plt.title("LeastSquare" + str(k))

		ORI, = plt.plot(DATAX,DATAY,'b:')
		RES, = plt.plot(DATAX,NAns,'r:')
		plt.legend([RES,ORI],["Result","Origin"])

		y_ticks = np.arange(0.5,2.6,0.1)
		x_ticks = np.arange(0,10,1)

		plt.xticks(x_ticks)
		plt.yticks(y_ticks)
		plt.xlim((-1,10))
		plt.ylim((0.4,2.6))
		plt.savefig(str(k)+".png")

	MMIN = 10000.0
	temp = -1
	for E in range(len(Error)) :
		if Error[E] < MMIN :
			MMIN = Error[E]
			temp = E
	print("MIN Error is {:d} , Error = {:3.6f}".format(temp+2,Error[temp]),file=OUT)

DATAX = [0.00,0.20,0.48,0.61,0.8,1.01,1.12,1.27,1.48,1.72,1.97,2.25,2.52,2.78,2.94,3.25,3.39,3.71,4.02,4.13,4.24,4.33,4.64,4.87,5.06,5.17,5.44,5.53,5.77,5.88,6.19,6.42,6.70,6.91,7.17,7.36,7.49,7.60,7.92,8.15,8.41,8.61,8.73,9.0,9.2]
DATAY = [1.0000,1.2482,1.7019,1.8899,2.0800,2.1157,2.0514,1.8839,1.5201,1.0361,0.6630,0.5458,0.7697,1.1515,1.4096,1.7564,1.8162,1.7406,1.5357,1.4631,1.4105,1.3752,1.3337,1.3300,1.3022,1.2625,1.1111,1.0496,0.8930,0.8547,0.9213,1.1665,1.5988,1.9059,2.1186,2.0953,1.9652,1.8140,1.1951,0.7906,0.5518,0.5768,0.6775,1.0472,1.3796]

LeastSquare(DATAX,DATAY)

