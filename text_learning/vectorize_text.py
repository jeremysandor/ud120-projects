#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1
        # if temp_counter < 200:
        path = os.path.join('..', path[:-1])
        # print path
        email = open(path, "r")

        ### use parseOutText to extract the text from the opened email
        text = parseOutText(email)
        
        ### use str.replace() to remove any instances of the words
        ### ["sara", "shackleton", "chris", "germani"]
        # for personName in ["sara", "shackleton", "chris", "germani"]:
        #     text = text.replace(personName, '')
        # print('text', text)
        text = text.replace('sara', '')
        text = text.replace('shackleton', '')
        text = text.replace('chris', '')
        text = text.replace('germani', '')

        ### append the text to word_data
        word_data.append(text)

        ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
        print('name', name)
        if name == 'sara':
            from_data.append(0)
        else:
            from_data.append(1)

        email.close()

print('word_data', word_data)
print('from_data', from_data)

print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )





### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer

transformer = TfidfVectorizer(stop_words="english")
theFit = transformer.fit_transform(word_data)
print('theFit', theFit)
afterTransform = theFit.toarray()
print(afterTransform)

stopWords = transformer.get_stop_words()
# print('stopWords', len(stopWords))

featureNames = transformer.get_feature_names()
# print(featureNames[34597])
print('featureNames', len(featureNames))


# shove matrix gained from TfidfVectorizer into
# k-means clustering
# just wanted to experiment
from sklearn.cluster import MiniBatchKMeans
clf = MiniBatchKMeans(n_clusters=4, n_init=10, max_iter=300)
clf.fit(afterTransform)
pred = clf.predict(afterTransform)
print('PRED', pred)

order_centroids = clf.cluster_centers_.argsort()[:, ::-1]
print('order_centroids', order_centroids)

terms = transformer.get_feature_names()
for i in range(4):
    print("Cluster %d:" % i)
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind])
    print()










