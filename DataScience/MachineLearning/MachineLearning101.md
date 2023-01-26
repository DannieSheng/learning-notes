## Notes taken from [Machine Learning-101](https://medium.com/machine-learning-101)

### Naive Bayes Classification
This classifier assumes the features are independent, and hence the word naive. 
It is powerful algorithm used for
* Real time Prediction
* Text classification/ Spam Filtering
* Recommendation System

### Support Vector Machine
* Kernel: transforming the problem
  * Linear
  * Polynomial
  * Exponential
* Regularization (C): how much you want to avoid misclassified each training example
  * Large C -> smaller-margin hyperplane, aims at classifying all samples correctly
  * Small C -> large-margin hyperplane, smooth decision surface
* Gamma: defines how far the influence of a single training example reaches
  * Low gamma values -> points far away from plausible separation line are considered in calculation for the separation line
  * High gamma values -> the points close to plausible line are considered in calculation
* Margin: A margin is a separation of line to the closest class points.
* 

