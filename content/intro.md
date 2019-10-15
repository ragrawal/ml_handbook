# Unboxing Machine Learning

## Objective
For professionals aspiring job in the technological sector, machine learning has become one of the most sought skills, and one can find many online courses, books, and blogs on the topic. While these resources are useful, I often struggle to develop an intuitive understanding of the concepts presented in these resources. Over the years I realized that are few core concepts related to machine learning and having a strong understanding of these concepts help in a big way. This book is an effort to help develop a strong intuitive understanding of these core concepts. 

Working towards developing the strong intuition, this book aims to start with an intuitive solution for a problem and show that as we try to make this intuitive solution robust and scalable, it leads to one of the established machine learning concepts. 


## Pre-requisites
This book is for readers who already have some experience in the field of machine learning and are trying to build a more cohesive understanding. In this book, I use Python code to convert ideas into prototypes and hence assumes that the reader is comfortable with Python programming. The prototype solutions further rely on python libraries such as pandas, numpy, scipy and sklearn and hence familiarity with these libraries is helpful. 


## Organization

### Chapter 1 and 2:

Fundamental to machine learning is the challenge of measuring and reporting quality of a model. This requires defining a metric that enables us to quantify the quality of a model. Depending on the output of the model, many different metrics exists to evaluate different kinds of models. Below table provides a broad classification of different types of machine learning problems and some of the metrics to evaluate them. 


Metric Group |Examples 
--------------|----------
Regression Related Metrics | Mean Absolute Error, Mean Squared Error, $R^2$
Classification Related Metrics | Precision, Recall, F1, AUC
Ranking Related Metrics | DCG, nDCG, RBO 
Clustering Related Metrics | 
Community Related Metrics | Modularity 

Currently this book covers regression and classification related metrics in chapter [1](01-RegressionMetrics.ipynb) and [2](02-ClassificationMetrics.ipynb), respectively. Eventually, I hope to add new chapters related to other types of machine learning problems.  

### Chapter 3:

Optimization is at the heart of machine learning, and one of the most commonly used optimization strategies is "Gradient descent." It is used in a wide variety of settings ranging from linear regression to deep learning. Chapter [3](03-GradientDescent.ipynb) aims to help understand the intuition behind gradient descent and some of its variants. 