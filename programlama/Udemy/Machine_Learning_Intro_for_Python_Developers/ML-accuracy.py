# Example of Classification Algorithm Accuracy.
#
# How good is the Algorithm? Measure accuracy!
#
# How? Use dataset: 
#
# 1. Split into "training_set" and "test_set".
# 2. Use training_set to train, then predict with test_set
# 3. Compare algorithm predictions with real test_set values.
#
# Watch the video to see further explanation.
#

# Load required functionality from sklearn
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset (X = features, Y = classes)
iris = load_iris()
X = iris.data
y = iris.target

# 1. Split into "training_set" and "test_set". 
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.5)

# 2. Use training_set to train, then predict with test_set
clf = tree.DecisionTreeClassifier()
clf.fit(X_train, Y_train)
predictions = clf.predict(X_test)

# 3. Compare algorithm predictions with real test_set values
print(accuracy_score(Y_test, predictions))
