# Algorithm Cheat Sheet 


### Linear Regression 

Linear models make a prediction assuming that there's a linear relationship between the features X and the value we want to find Y. That relationship is usually represented by the following equation Y =f(X)+ε. 

The Linear Regression algorithm tries to find the f(X). ε is the random error term.

---

#### scikit-learn 

```
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X, y)

# Evaluating the model 

# Getting the coefficients 
coeff_df = pd.DataFrame(lr.coef_,X.columns,columns=['Coefficient'])

# Making predictions
predictions = lm.predict(X_test)

# Evaluating performance 

from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

```
The hyper parameters are:

__fit_intercept:__ Whether or not to calculate the intercept for this model. True by default and usually there's no reason to not keep it like that.

__normalize:__ Defaults to false, leave it like that unless you know what you are doing. If True, the regressors X will be normalized before regression by subtracting the mean and dividing by the l2-norm.

Basically it's best to use the defaults.

### Gradient Descent



### Polynomial regression

### Regularized linear models 

### Logistic Regression

## Support Vector Machines 

### Linear SVM classifiers

### SVM Regression 

## Decision Tree

## Ensemble Learning

### Voting Classifiers

### Random Forest 

A Random Forest is a meta estimator which is an ensemble of Decision Trees trained on various subsets of the dataset, to improve it's accuracy and try to prevent overfitting. As an ensemble it uses the predictions of the generated trees and then makes a prediction based on their results

---

#### scikit-learn 

```

from sklearn.ensemble import RandomForestClassifier

random_forest = RandomForestClassifier(n_estimators=200)
random_forest.fit(x, y)

```
The hyper parameters are:

__n_estimators:__ The number of trees in the forest. Usually having more tree is better, still worth finding the number where it starts to converge.

__max_features:__ The number of features to consider when looking for the best split, this one should be tested with a wide range of values, since this is pretty much the most important hyperparameter. In Scikit-learn this parameter can be an integer, float(int(max_features * n_features) features are considered at each split) or a string with possible values: “auto”( max_features=sqrt(n_features)), “sqrt”(same as auto),“log2” (max_features=log2(n_features)) or `None` which means max_features=n_features.

__max_depth:__ The maximum depth of the tree. By default there's no limit and the three will grow as much as it needs but it's recommended to limit their growth if you are dealing with "noisy data".

[Full parameter description in the official docs](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)


#### Tensorflow

As of now the high level implementation is still under the contrib module, since everything in that module is subject to change at anytime I'll put the link to the official example. When it finally goes to the estimator module outside of the contrib module I'll update this.
[RandomForest MNIST - TF ](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/learn/random_forest_mnist.py)

#### Keras

Coming soon

### Adaboost

### Gradient Boosting 

### Stacking 

---

## Clustering

### K-means



