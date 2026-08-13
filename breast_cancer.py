#implement gaussianNB using the public dataset load_breast_cancer
from sklearn.datasets import load_breast_cancer
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

breast_cancer = load_breast_cancer()

X = breast_cancer.data
# print(breast_cancer.feature_names)

y = breast_cancer.target
# print(breast_cancer.target_names)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.2,random_state=42)

model = GaussianNB()

model.fit(X_train,y_train)

# y_prediction = model.predict(X_test)

# print(y_prediction)
# print(accuracy_score(y_test,y_prediction))
# print(confusion_matrix(y_test,y_prediction))
# print(classification_report(y_test,y_prediction))

sample = X_test[1].reshape(1,-1)
prediction = model.predict(sample)
print(prediction)
print(breast_cancer.target_names[prediction])
