from sklearn import tree

clf = tree.ExtraTreeRegressor()

# __all__ = ["DecisionTreeClassifier", "DecisionTreeRegressor",
#            "ExtraTreeClassifier", "ExtraTreeRegressor", "export_graphviz"]

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
#      'female', 'male', 'male']

Y = [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1]

clf = clf.fit(X,Y)
prediction = clf.predict([[190,70,42]])
print prediction[0]