from sklearn import tree

labels = [0,0,1,0,1,1,0,0]
features = [[2,2],[2,2],[3,4],[2,2],[4,4],[4,4],[3,2],[2,2]]

algorithm = tree.DecisionTreeClassifier()       
algorithm = algorithm.fit(features, labels)

newData = [[3,4]]
print(algorithm.predict(newData))
