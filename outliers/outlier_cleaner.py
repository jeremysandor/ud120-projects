#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    length = len(predictions)
    tenPercent = int(length * .1)
    print('length', length)
    print('tenPercent', tenPercent)

    cleaned_data = []
    pre_cleaned_data = []
    ### your code goes here
    # print('predictions', predictions)
    # print('net_worths', net_worths)
    for index, elem in enumerate(predictions):
        # print('elem', elem)
        # print('index', index)
        # for item in enumerate(net_worths):
        #     item[index]
        residualError = elem[0] - net_worths[index][0]
        # print('residualError', residualError)
        pre_cleaned_data.append([ages[index][0], net_worths[index][0], residualError])

    sorted_data = sorted(pre_cleaned_data, key=lambda x: x[2], reverse=True)


    del sorted_data[0:tenPercent - 1]
    print('sorted_data', sorted_data)
    cleaned_data = sorted_data

    return cleaned_data

