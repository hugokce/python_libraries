# Example of Classification Algorithm
# Real World Data: "Iris Flower Dataset"
#
# Data =
#  Classes: "Setosa" (0), "Versicolour" (1) and "Virginica" (2)
#  Features: "Petal length", "Petal width", "Sepal length", "Sepal width"
#
# Task = "Predict Flower [0,1 or 2], Given 4 new features".
#
# Watch the video to see further explanation.

# Load Classification Algorithm
from sklearn import tree

# Import Example Dataset "Iris Flowers"
from sklearn.datasets import load_iris

# Load Example Dataset "Iris Flowers"
iris = load_iris()

# Load Classification Algorithm 
classifier = tree.DecisionTreeClassifier()

# Train algorithm with Example Dataset "Iris"
classifier.fit(iris.data, iris.target)

# Measurements (petal length, petal width, sepal length, sepal width)
newData = [[6.4, 3.1, 4.4, 1.2]]

# Predict (which flower?)
print( classifier.predict(newData) )
