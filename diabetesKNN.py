# Write a Python program to predict diabetes using KNN Regression

import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

diabetes = load_diabetes()

print(diabetes.data.shape)
print(diabetes.target.shape)
print(diabetes.feature_names)

X = diabetes.data
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

regressor = KNeighborsRegressor(n_neighbors=3)

regressor.fit(X_train, y_train)

pred = regressor.predict(X_test)

r2 = r2_score(y_test, pred)

print("R2 score : ",r2)

sample = np.array([[0.34562,1.74664,0.6343688,-0.63442,0.12433,]])