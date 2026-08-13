Then you are implementing A in an algorithm, so you have to specify the number of neighbors. So for that, you# implement gaussiannb using the public dataset load_breast_cancer from sklearn.datasets
import numpy as np

from sklearn.datasets import load_breast_cancer

from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

cancer = load_breast_cancer()

X = cancer.data

y = cancer.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Predicted values : ", y_pred)

print("Actual values : ", y_test)

print("Accuracy : ", accuracy_score(y_test, y_pred))

print("Confusion Matrix : \n", confusion_matrix(y_test, y_pred))

print("Classification Report : \n", classification_report(y_test, y_pred))

sample = X_test[0].reshape(1,-1)

prediction = model.predict(sample)

print("predicted classes : ", cancer.target_names[prediction])

