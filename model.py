import numpy as np
import pandas as pd

import seaborn as sns
import sys
import scipy
import sklearn 
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures

# Training the model

data= pd.read_csv("powerproduction.csv")
# Let’s select some features to explore more :
data = data[["speed","power"]]

# Generating training and testing data from our data:
# We are using 80% data for training.
train = data[:(int((len(data)*0.8)))]
test = data[(int((len(data)*0.8))):]

poly3 = PolynomialFeatures(degree=3)

train_x = np.array(train[["speed"]])
train_y = np.array(train[["power"]])
train_x_poly3 = poly3.fit_transform(train_x)

clf3 = linear_model.LinearRegression()
train_y3_ = clf3.fit(train_x_poly3, train_y)

#The coefficients
print ('Coefficients: ', clf3.coef_)
print ('Intercept: ',clf3.intercept_)

test_x = np.array(test[["speed"]])
test_y = np.array(test[["power"]])


test_x_poly3 = poly3.fit_transform(test_x)
test_y3_ = clf3.predict(test_x_poly3)


# Predicting values:
def prev(XX):
 predicted_v = clf3.intercept_[0]+ clf3.coef_[0][1]*XX + clf3.coef_[0][2]*np.power(XX, 2) + clf3.coef_[0][3]*np.power(XX, 3)
 return predicted_v
 
# Predicting power:
wspeed = np.random.rand()
epower = prev(wspeed)
print(f'For a random speed: {wspeed}, the power predicted is: {epower}.')
