# Example: Price predictor, given Pizza Diameter.
# A Regression Algorithm predicts _continous values_ (like price)
#
#------------------------------------------------------------
# In "ML-regression1.py" you can see there's a correlation
# between X and Y.
#------------------------------------------------------------
#
# Steps:  
# 1. Algorithm is trained on data.
# 2. Algorithm predicts price, given a new diameter
#
# Watch the video to see further explanation.

# Load LinearRegression algorithm
from sklearn.linear_model import LinearRegression

# Training Data: diameter
X = [[4], [8], [12], [16], [18]]
# Training Data: price
y = [[4], [8], [10], [12], [15]]

# 1. Algorithm is trained on data (X,y).
model = LinearRegression()
model.fit(X,y)

# 2. Algorithm predicts price, given a new diameter
diameter = 13
prediction = model.predict([[diameter]])
print('Price prediction: $%.2f' % prediction)

