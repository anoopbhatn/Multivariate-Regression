# Multivariate Regression

from datagen import labels,data_x,data_y
import numpy as np

def compute():
	# Generate X matrix
	X=[]
	for i in range(len(data_x)):
		X.append([1])

	for i in range(len(X)):
		X[i].extend(data_x[i])

	X=np.array(X)
	Xt=X.transpose()

	# Matrix multiplication of Xt and X
	xtx=np.dot(Xt,X)

	# Inverse of product
	xtxinv=np.linalg.inv(xtx)

	# Compute partial product inverse(Xt*X)*Xt
	pprod=np.dot(xtxinv,Xt)

	# Get y - transpose of data_y
	y=np.array(data_y)
	y=y.transpose()

	# Resultant array of w
	res=np.dot(pprod,y)

	return res

print 'Enter the values:'
x=map(float,raw_input().split(';'))

resw=compute()

result=resw[0]
for i in range(1,len(resw)):
	result+=x[i-1]*resw[i]

print 'Quality of wine in scale of 1-10 is : ',result

