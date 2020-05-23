import random 
import math
import matplotlib.pyplot as plt


##########################################
#Method 1
def LaFun(dataX,dataY,Minx,Maxx,out):

	x = Minx
	tmpx = list()
	tmpy = list()
	while x <= Maxx:
		ans = 0
		for i in range(len(dataX)):
			tmp = 1
			for j in range(len(dataX)):
				if i == j :
					continue
				tmp = tmp * (x-dataX[j])/(dataX[i] - dataX[j])
			ans = ans + tmp * dataY[i]

		tmpx.append(x)
		tmpy.append(ans)
		x = x + 0.001

	plt.cla()
	plt.clf()
	plt.title("Lagrange")
	ORI, = plt.plot(dataX,dataY,'bo')
	RES, = plt.plot(tmpx,tmpy,'r:')
	plt.legend([RES,ORI],["Result","Origin"])

	plt.savefig(out+"-Lagrange.png")

##########################################
# Method 2

def NDD(dataX,dataY,Minx,Maxx,out):

	tmp = list()
	tmp.append(dataY)
	for i in range(1,len(dataX)):
		tmptable = list()
		for j in range(0,len(dataX) - i):
			numerator = tmp[i-1][j+1] - tmp[i-1][j]
			denominator = dataX[i+j]-dataX[j]
			tmptable.append(numerator/denominator)
		tmp.append(tmptable)

	x = Minx
	tmpx = list()
	tmpy = list()

	while x <= Maxx:
		ans = 0
		for i in range(len(tmp)):
			tft = tmp[i][0]
			for j in range(i):
				tft = tft * (x-dataX[j])
			ans = ans + tft
		tmpx.append(x)
		tmpy.append(ans)
		x = x+ 0.001

	plt.cla()
	plt.clf()
	plt.title("Newton")
	ORI, = plt.plot(dataX,dataY,'bo')
	RES, = plt.plot(tmpx,tmpy,'r:')
	plt.legend([RES,ORI],["Result","Origin"])

	plt.savefig(out+"-Newton.png")

##########################################
#Method 3

def GNFD(dataX,dataY,Minx,Maxx,out):
	
	tmp = list()
	tmp.append(dataY)
	for i in range(1,len(dataX)):
		tmptable = list()
		for j in range(0,len(dataX) - i):
			tmptable.append(tmp[i-1][j+1] - tmp[i-1][j])
		tmp.append(tmptable)

	h = dataX[1] - dataX[0]

	x = Minx
	tmpx = list()
	tmpy = list()

	while x <= Maxx:
		ans = 0
		for i in range(len(tmp)):
			tft = tmp[i][0]
			s = (x - dataX[0])/h
			for j in range(1,i+1):
				tft = tft * (s/j)
				s = s-1
			ans = ans + tft

		tmpx.append(x)
		tmpy.append(ans)
		x = x + 0.001

	plt.cla()
	plt.clf()
	plt.title("GNFD")
	ORI, = plt.plot(dataX,dataY,'bo')
	RES, = plt.plot(tmpx,tmpy,'r:')
	plt.legend([RES,ORI],["Result","Origin"])

	plt.savefig(out+"-GNFD.png")

##########################################
#Method4

def GNBD(dataX,dataY,Minx,Maxx,out):

	tmp = list()
	tmp.append(dataY)
	for i in range(1,len(dataX)):
		tmptable = list()
		for j in range(0,len(dataX) - i):
			tmptable.append(tmp[i-1][j+1] - tmp[i-1][j])
		tmp.append(tmptable)

	h = dataX[1] - dataX[0]

	x = Minx
	tmpx = list()
	tmpy = list()

	while x <= Maxx:
		ans = 0
		for i in range(len(tmp)):
			tft = tmp[i][-1]
			s = (x - dataX[-1])/h
			for j in range(1,i+1):
				tft = tft * (s/j)
				s = s+1
			ans = ans + tft

		tmpx.append(x)
		tmpy.append(ans)
		x = x + 0.001

	plt.cla()
	plt.clf()
	plt.title("GNBD")
	ORI, = plt.plot(dataX,dataY,'bo')
	RES, = plt.plot(tmpx,tmpy,'r:')
	plt.legend([RES,ORI],["Result","Origin"])

	plt.savefig(out+"-GNBD.png")

##########################################
#Main

DataSetX1 = [2.40, 2.75, 2.91, 3.33, 3.89, 3.94, 4.42, 4.65, 4.87, 5.00, 5.33, 5.96, 6.14, 6.53, 6.85, 7.14, 7.35, 7.67, 7.70, 8.10]
DataSetY1 = [-2.5065, -1.4261,  0.6374,  1.9569, -1.2967, 0.0134, -1.7892, -3.6020,  4.0695,  4.1644, -4.6471, -4.5018,  5.5824, -3.6274, -1.5766, 5.3962, -3.8348,  7.2730,  5.6132,  7.4893]

DataSetX2 = [2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.2, 4.5, 4.8, 5.1, 5.4, 5.7, 6.0, 6.3, 6.6, 6.9, 7.2, 7.5, 7.8, 8.1]
DataSetY2 = [-2.5065, -1.9135,  1.8316,  2.3425, -2.9735, -1.0456,  3.9669, -3.9166,  1.8038,  0.3963, -1.9792,  2.6447, -2.4312,  1.0453,  1.6986, -5.2736,  7.1707, -3.6987, -4.6149,  7.4893]

DataSetX3 = [2.456789,2.752698,2.912354,3.335684,3.895244,3.944587,4.425874,4.652589,4.875412,5.012549,5.336245,5.964582,6.145847,6.532168,6.852694,7.146842,7.359147,7.671812,7.752194,8.099999]
DataSetY3 = [3.71828,1.85747,1.63276,1.19944,0.986737,0.986322,1.137,1.31052,1.54791,1.72873,2.23763,3.31594,3.56486,3.91517,4.03606,4.05365,4.01884,3.87228,3.8112,3.42151]

LaFun(DataSetX1,DataSetX2,2.4,8.1,"DataSet1")
LaFun(DataSetX2,DataSetY2,2.4,8.1,"DataSet2")
LaFun(DataSetX3,DataSetY3,2.4,8.1,"DataSet3")

NDD(DataSetX1,DataSetX2,2.4,8.1,"DataSet1")
NDD(DataSetX2,DataSetY2,2.4,8.1,"DataSet2")
NDD(DataSetX3,DataSetY3,2.4,8.1,"DataSet3")

GNFD(DataSetX1,DataSetX2,2.4,8.1,"DataSet1")
GNFD(DataSetX2,DataSetY2,2.4,8.1,"DataSet2")
GNFD(DataSetX3,DataSetY3,2.4,8.1,"DataSet3")

GNBD(DataSetX1,DataSetX2,2.4,8.1,"DataSet1")
GNBD(DataSetX2,DataSetY2,2.4,8.1,"DataSet2")
GNBD(DataSetX3,DataSetY3,2.4,8.1,"DataSet3")