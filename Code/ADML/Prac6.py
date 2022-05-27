# IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
test=pd.read_csv("./california_housing_test.csv")
train=pd.read_csv("./california_housing_train.csv")
train.head()

test.tail()

print(train.info())
print(test.info())

n_train = train.shape[0]
n_test = test.shape[0]
y = train['median_house_value'].values
data = pd.concat((train, test)).reset_index(drop = True)
data.drop(['longitude','latitude'], axis=1, inplace = True)

#VISUALISING THE DATA
#Visualise the data
plt.figure()
sns.heatmap(data.corr(), cmap='coolwarm')
plt.show()
sns.lmplot(x='median_income', y='median_house_value', data=train)
sns.lmplot(x='housing_median_age', y='median_house_value', data=train)

sns.pairplot(train, palette='rainbow')

#FEATURE ENGINEERING
#Feature engineering is the process of using domain knowledge to extract features from raw data via data mining techniques.
#Select appropriate features
data = data[['total_rooms', 'total_bedrooms', 'housing_median_age','median_income', 'population', 'households']]
data.info()

data['total_rooms'] = data['total_rooms'].fillna(data['total_rooms'].mean())
data['total_bedrooms'] = data['total_bedrooms'].fillna(data['total_bedrooms'].mean())
data['housing_median_age'] = data['housing_median_age'].fillna(data['housing_median_age'].mean())
data['median_income'] = data['median_income'].fillna(data['median_income'].mean())
data['population'] = data['population'].fillna(data['population'].mean())
data['households'] = data['households'].fillna(data['households'].mean())

train = data[:n_train]
test = data[n_train:]
#FITTING THE MODEL
#Split the dataset into training and testing data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(train, y, test_size = 0.2)
y_train = y_train.reshape(-1,1)
y_test = y_test.reshape(-1,1)
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)
y_train = sc_y.fit_transform(y_train)
y_test = sc_y.fit_transform(y_test)
# Fit the model over the training data
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
y_pred = y_pred.reshape(1,-1)
y_pred = sc_y.inverse_transform(y_pred)
y_pred

df = pd.DataFrame({'Real Values':sc_y.inverse_transform(y_test.reshape(1,-1)).ravel(),'Predicted Values':y_pred.ravel()})
df
