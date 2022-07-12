# Example: Draw Classification Algorithm (Tree)
# -> Output: Image with Tree Algorithm steps
#
#------------------------------------------------------------------------
# This program ONLY visualizes the tree algorithms steps.
# Skip it, if you don't care about "internal code of algorithms".
#------------------------------------------------------------------------
#
# What's a "decision tree?".
#
# A tree is a model used in computer science.
# It starts at the root (top of tree), then takes step down based on
# questions/feature comparisons.
# Example (fruit classifier):
#
#              start
#                |
#          |-----+-----------|
#       [heavy?]         [not heavy?]
#          |                 |
#         melon              |
#                      [ red or orange? ]
#                            |
#                  [ red? ]--+---[ orange? ]
#                      |             |
#                    apple         orange
#
# This programs draws the tree and saves as a pdf.
#  
# Watch the video to see further explanation.
#  

from sklearn import tree
from sklearn.datasets import load_iris
import pydotplus
import graphviz
from sklearn.externals.six import StringIO

# 1. load dataset and train classifier
iris = load_iris()
classifier = tree.DecisionTreeClassifier()
classifier.fit(iris.data, iris.target)

# 2. visualize
dot_data = StringIO()
tree.export_graphviz(classifier, out_file=dot_data,
feature_names=iris.feature_names,
class_names=iris.target_names,
filled=True, rounded=True,
special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")