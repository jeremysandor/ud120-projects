#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# speed up tests:
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

# my hypothesis is that this does not work because of
# SVM not dealing with large data sets well
# something about cubic nature of the data?
# turns out, setting kernel='rbf' takes a long time vs linear
# number if iterations for rbf is  22041
# number if iterations for linear is  3455
# for this dataset
# we can train on partial data to speed this up - but accuracy will be affected
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
# large c value means more training points correct, but more complex
clf = SVC(C=10000, kernel='rbf', verbose=True)
print 'clf', clf
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print('pred', pred)

chrisCount = 0
for elem in pred:
  if elem == 1:
    chrisCount += 1

print 'chrisCount', chrisCount

# print 'elem10', pred[10]
# print 'elem26', pred[26]
# print 'elem100', pred[50]


accuracy = accuracy_score(pred, labels_test)
print accuracy

import matplotlib.pyplot as plt

# plt.plot(features_test, labels_test)
# # plt.ylabel('some numbers')
# plt.show()





#########################################################
### your code goes here ###

#########################################################


