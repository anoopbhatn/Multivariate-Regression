# To tranform the data into required format
import csv

f1=open("winequality-red.csv","r")

reader=csv.reader(f1,delimiter=';')

labels=[]
data_x=[]
data_y=[]

i=1
for row in reader:
	# Place all the labels in a list
	if i==1:
		labels=row
		i+=1
		continue
	
	# Place the values of the attributes in data_x list of lists
	data_x.append([float(row[j]) for j in range(len(row)-1)])

	# Place the y values in data_y list
	data_y.append(float(row[len(row)-1]))