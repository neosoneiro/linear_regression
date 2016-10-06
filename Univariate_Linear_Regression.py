import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model,datasets

def get_data():
	data=pd.read_csv('restaurant.csv')
	population=[]
	profit=[]
	for x,y in zip(data['Population'],data['Profit']):
		population.append([float(x)])
		profit.append([float(y)])
	return population,profit
	
def predict_profit(population,profit):
    model=linear_model.LinearRegression()
    model.fit(population,profit)
    plt.scatter(population,profit,color='red')
    plt.plot(population,model.predict(population),color='blue',linewidth=2)
    print "Theta zero is "
    print model.intercept_
    print "Theta one is "
    print model.coef_
    plt.show()
    

population,profit=get_data()
predict_profit(population,profit)

