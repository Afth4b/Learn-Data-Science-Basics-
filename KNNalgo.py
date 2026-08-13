# Then you are implementing A in an algorithm, so you have to specify the Number of neighbors. So for that, you have to import the library neighbors from sklearn into
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

classifier = KNeighborsClassifier(n_neighbors=3)

classifier.fit(X_train, y_train)

pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test,pred)

print("Accuracy : ",accuracy)

sample = np.array([[5.1,3.5,1.4,0.2]])

var_pred = classifier.predict(sample)

print("predicted class is : ",var_pred)

print(iris.target_names[var_pred])

slength = float(input("Enter sepal length : "))
swidth = float(input("Enter sepal width : "))
plength = float(input("Enter petal length : "))
pwidth = float(input("Enter petal width : "))

sample = np.array([[slength,swidth,plength,pwidth]])

var_pred = classifier.predict(sample)

print("predicted class is : ",var_pred)
print("Species is : ",iris.target_names[var_pred])