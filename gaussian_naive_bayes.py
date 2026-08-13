from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, confusion_matrix , classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import numpy as np


iris = load_iris()

X = iris.data

y = iris.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# model creation and training
model = GaussianNB()

model.fit(X_train,y_train)

# prediction on test data/unseen data
y_prediction = model.predict(X_test)

print(y_prediction)

print(accuracy_score(y_test,y_prediction))

print(confusion_matrix(y_test,y_prediction))

print(classification_report(y_test,y_prediction))

sample = np.array([[5.1,3.5,1.4,0.2],
                   [5.3,4.5,2.5,1.8],
                   [3.1,4.5,6.8,3.2],
                   [5.2,4.8,6.9,7.9]])

sample_prediction = model.predict(sample)

print(sample_prediction)

print(iris.target_names[sample_prediction])
