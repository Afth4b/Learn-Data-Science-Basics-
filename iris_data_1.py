from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np


iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(y_pred)

print(y_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

print("confusion matrix:\n", confusion_matrix(y_test, y_pred))

print("classification report:\n", classification_report(y_test, y_pred))

sample = np.array([[5.1,3.5,1.4,0.2],[6.2, 3.4,5.4, 2.3],[5.9, 3.0, 5.1, 1.8]])

variable_prediction = model.predict(sample)

print("Prediction for sample : ",variable_prediction)

print(iris.target_names[variable_prediction])

