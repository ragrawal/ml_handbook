# Unboxing Machine Learning

## Why "Unboxing Machine Learning"?

"Unboxing Machine Learning" is an attempt to provide an intuitive and visual explanation of some of the core concepts of machine learning.

For professionals in the software industry, knowing the fundamentals of machine learning is increasingly a necessity. But, for many, the greek letters and all the complicated mathematical jargon might present a significant barrier to entry.  Over the years, I realized that there are few core concepts at the heart of machine learning and are not necessarily that difficult to understand. Developing an intuitive and visual understanding of these concepts will help you unbox machine learning that often seems like black magic.

In this book, I try not to provide definitions of the above-referred core concepts but trying to show why these concepts are defined the way they are.  I want to expose the underlying reasoning that leads to the existing definition of these concepts. For instance, you might have heard about "F1" metric and might know that it is used for evaluating classification models. Most online resources will explain the "F1" metric as the harmonic mean of precision and recall. But in this book, I don't stop at that. I try to explain:

1. why use harmonic mean rather than arithmetic mean or geometric mean?
2. Why only precision and recall?
3. What exactly are precision and recall?
4. Why precision and recall are defined the way they are?

In this book, I use a problem-oriented approach to learning. I focus on a problem and then discuss different options to solve the problem. On our journey to solve a given problem, we will naturally stumble upon solutions that are already widely known in the field of machine learning. Thus the focus is on self-discovery only through our intuitions.


## Pre-requisites

I don't expect the reader to be math savvy, but having a programming experience might be necessary, especially for the later sections of the book. Further, I assume that you already have some level of familiarity with machine learning. For instance, you understand the difference between supervised and unsupervised machine learning, regression problem vs. classification problem, etc. 

## Organization

### Chapter 1 and 2:

Fundamental to machine learning is the challenge of measuring and reporting the quality of a model. This challenge is addressed by various by constructing different kinds of metrics. The need for different kinds of metrics mainly arises due to different types of problems. The below table provides a broad classification of different kinds of machine learning problems and some of the popular evaluation metrics


Metric Group |Examples 
--------------|----------
Regression Related Metrics | Mean Absolute Error, Mean Squared Error, $R^2$
Classification Related Metrics | Precision, Recall, F1, AUC
Ranking Related Metrics | DCG, nDCG, RBO 
Clustering Related Metrics | 
Community Related Metrics | Modularity 

Currently this book covers regression and classification related metrics in chapter [1](01-regressionmetrics) and [2](02-classificationmetrics), respectively. Eventually, I hope to add new chapters related to other types of machine learning problems.  

### Chapter 3 and 4:

Optimization is at the heart of machine learning, and one of the most commonly used optimization strategies is "Gradient descent." It is used in a wide variety of settings ranging from linear regression to deep learning. Chapter [3](03-gradientdescent) aims to help understand the intuition behind gradient descent. Chapter 4 takes the idea of gradient descent and shows how it can help learn the parameters of a function.


## About Me
Find more about me over [here](https://ragrawal.wordpress.com/)
