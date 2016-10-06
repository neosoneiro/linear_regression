import numpy as np
import pandas as pd
from sklearn import datasets,linear_model

def get_data():
	data=pd.read_csv('Pokemon.csv')
	x_parameter=[]
	y_parameter=[]
	for x1,y1 in zip(data['HP'],data['Attack']):
		x_parameter.append([int(x1)])
		y_parameter.append([int(y1)])
	return x_parameter,y_parameter

def predict_power(x_parameter,y_parameter):
	a1=linear_model.LinearRegression()
	a1.fit(x_parameter,y_parameter)
	b1=a1.predict(110)
	print b1

x_parameter,y_parameter=get_data()
#print x_parameter,y_parameter
predict_power(x_parameter,y_parameter)	



