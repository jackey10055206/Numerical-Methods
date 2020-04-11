import numpy as np
import random
import time

num = [2,3,5,10,50,100]

OUT = open("data.out","w")
TIME = open("time.out","w")

for N in num:

	tStart = time.time()

	print("* {}".format(N),file = OUT)

	A = np.zeros(N*N).reshape(N,N)
	B = np.zeros(N)

	for i in range(N):
		print("$",end="",file=OUT)
		for j in range(N):
			A[i,j] = random.randint(-10,10)
			if A[i][j] >= 0 and j != 0 :
				print("+",end="",file=OUT) 
			print("{}X_{{{}}}".format(A[i,j],j),end="",file=OUT)
		B[i] = random.randint(-10,10)
		print(" = {}$".format(B[i]),file=OUT)

	X = np.linalg.solve(A,B)

	for i in range(N):
		print("$X_{{{}}} = {:.6f}$".format(i,X[i]),file=OUT)
	
	# print("---------------",file = OUT)

	tEnd = time.time()
	print("{:>4d}".format(N),end=" : ",file=TIME)
	print("{:.6f}".format(tEnd - tStart),file=TIME)
	print(N)