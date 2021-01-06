import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import scipy
import sklearn 
from sklearn import linear_model
from pandas.plotting import scatter_matrix
from matplotlib import pyplot

from sklearn.preprocessing import PolynomialFeatures

# Training the model

data= pd.read_csv("powerproduction.csv")

poly3 = PolynomialFeatures(degree=3)

train_x = np.array(train[["speed"]])
train_y = np.array(train[["power"]])
train_x_poly3 = poly3.fit_transform(train_x)
clf3 = linear_model.LinearRegression()
train_y3_ = clf3.fit(train_x_poly3, train_y)

#The coefficients
print ('Coefficients: ', clf3.coef_)
print ('Intercept: ',clf3.intercept_)

# Plotting the best fit line
plt.scatter(train.speed, train.power,  color='blue')
XX = np.array(train[["speed"]])
yy = clf3.intercept_[0]+ clf3.coef_[0][1]*XX + clf3.coef_[0][2]*np.power(XX, 2) + clf3.coef_[0][3]*np.power(XX, 3)
plt.plot(XX, yy, '-r' )
plt.xlabel("Speed")
plt.ylabel("Power")

test_x_poly3 = poly3.fit_transform(test_x)
test_y3_ = clf3.predict(test_x_poly3)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y3_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y3_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y, test_y3_) )

# Predicting values:
# Function for predicting future values :
def get_rp(input_features,intercept,slope):
 predicted_v = input_features*slope + intercept + input_features*slope**2 + input_features*slope**3
 return predicted_v

# Predicting power:
wspeed = 0.325
epower = get_rp(wspeed,clf.intercept_[0],clf.coef_[0][0])
print ("Estimated Power :", epower)