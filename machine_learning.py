import pandas as pd
import numpy as np
import random

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

import matplotlib.pyplot as plt

import datetime
#====================================================================================================
panda_dataframe = pd.DataFrame.from_csv('data.csv')

ios_all_ratings = []

for element in panda_dataframe['ios_all_ratings']:
	ios_all_ratings.append(element)

#training data
#============================================================

x_array = list(range(1, 1447))
xs = np.asarray(x_array)
X = xs[:, np.newaxis]
ys = np.asarray(ios_all_ratings)
#============================================================








#test data
#============================================================
#2016-08-31
#first_datatime = 1591

#2016-09-31
#second_datatime = 1735

#2016-10-31
#third_datatime = 1879

xs_test = list(range(1, 1880))
#============================================================








#mean model (really bad lol)
#============================================================

mean_model = [np.mean(ys) for _ in xs_test]

#============================================================






#linear model (really bad again)
#============================================================


model1 = LinearRegression()
model1.fit(X, ys)
linear_model = [model1.predict(x) for x in xs_test]

#============================================================







#pipeline model (pretty good but too exponential)
#============================================================

model2 = make_pipeline(PolynomialFeatures(7), Ridge())
model2.fit(X, ys)
pipeline_model = [model2.predict(x) for x in xs_test]

#============================================================

#plot
plt.scatter(xs, ys, color='navy', marker='o', label='Observations')
plt.ylim([100000, 200000])
plt.plot(xs_test, mean_model, color='blue', linewidth=2, label='Mean model')
plt.plot(xs_test, linear_model, color='red', linewidth=2, label='Linear model')
plt.plot(xs_test, pipeline_model, color='purple', linewidth=2, label='Pipeline model')

plt.grid(True)
plt.legend()
plt.show()



