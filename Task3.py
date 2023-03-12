import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('internship_train.csv')
data1 = pd.read_csv('internship_hidden_test.csv')
y = data['target']
X = data.drop('target', inplace=False, axis = 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=0)
X.shape
regression = LinearRegression()
regression.fit(X_train, y_train)
data1['target'] = regression.predict(data1)
data1.to_csv('predictions.csv', index=False)
