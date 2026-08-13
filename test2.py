from sklearn.datasets import load_iris

iris = load_iris()

print(iris.data[:5])

print("\n\n")

print(iris.target[:5])

print(iris.target_names)
print(len(iris.target_names))


print(iris.feature_names)
print(len(iris.feature_names))

print(len(iris.data))