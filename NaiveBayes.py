from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = datasets.load_iris()

# Features and target
X = iris.data
y = iris.target

# Split dataset
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Naive Bayes classifier
classifier = GaussianNB()

# Train the model
classifier.fit(x_train, y_train)

# Predict test data
result = classifier.predict(x_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, result) * 100

# Display accuracy
print("Accuracy:", accuracy, "%")
print(f"Accuracy: {accuracy:.2f}%")

# Take new flower input
features = [[
    float(i) for i in input(
        f"Enter {iris.feature_names}: "
    ).split()
]]

# Predict new flower
result = classifier.predict(features)

print("Predicted flower:", iris.target_names[result][0])