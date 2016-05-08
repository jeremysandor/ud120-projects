#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# print(enron_data)
count = 0
poiCount = 0
quantifiedSalaryCount = 0
validEmailCount = 0
totalPaymentCount = 0
poiWithPaymentInfo = 0
for k, v in enron_data.iteritems():
  count += 1
  print(k)
  print(v)
  if type(v['salary']) is int:
    quantifiedSalaryCount += 1
  if type(v['total_payments']) is int:
    totalPaymentCount += 1
  if v['email_address'] != 'NaN':
    validEmailCount += 1
  if v['poi']:
    if type(v['total_payments']) is int:
      poiWithPaymentInfo += 1
    poiCount += 1
  featureCount = 0
  for key, val in v.iteritems():
    featureCount += 1
  # print('featureCount', featureCount)
# print('poiCount', poiCount)
print('total', count)
# print('quantifiedSalaryCount', quantifiedSalaryCount)
# print('validEmailCount', validEmailCount)
print('totalPaymentCount', totalPaymentCount)

totalPaymentPercent = totalPaymentCount / float(count)
print('totalPaymentPercent', totalPaymentPercent)

totalPoiPercent = poiWithPaymentInfo / float(poiCount)
print('totalPoiPercent', totalPoiPercent)


# jamesStockVal = enron_data["PRENTICE JAMES"]["total_stock_value"]
# print(jamesStockVal)

# kenTotalMoney = enron_data["LAY KENNETH L"]["total_payments"]
# jeffTotalMoney = enron_data["SKILLING JEFFREY K"]["total_payments"]
# drewTotalMoney = enron_data["FASTOW ANDREW S"]["total_payments"]
# print(kenTotalMoney, jeffTotalMoney, drewTotalMoney)

