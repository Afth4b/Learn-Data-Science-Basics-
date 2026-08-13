import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

diabetes = load_diabetes()

print(diabetes.data.shape)
print(diabetes.target.shape)
print(diabetes.feature_names)

X = diabetes.data
y = diabetes.target

# Convert continuous target into two classes
# 0 = Below median
# 1 = Above or equal to median

median = np.median(y)
y = np.where(y >= median, 1, 0)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

classifier = KNeighborsClassifier(n_neighbors=3)

classifier.fit(X_train, y_train)

pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print("Accuracy : ", accuracy)

# Test using an existing value from the dataset
sample = X[10].reshape(1, -1)

prediction = classifier.predict(sample)

print("Predicted class : ", prediction[0])

if prediction[0] == 0:
    print("Result : Below median")
else:
    print("Result : Above or equal to median")