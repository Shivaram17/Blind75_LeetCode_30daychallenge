def Merge(dict1, dict2):
    # create a new dictionary by merging the items of the two dictionaries using the union operator (|)
    # merged_dict = dict(dict1.items() | dict2.items())
    dict2.update(dict1)
    # for i in dict2:
        # dict1[i] = dict2[i]
    # return the merged dictionary
    return dict2

# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'a': 6, 'c': 4}

# merge the two dictionaries using the Merge() function
merged_dict = Merge(dict1, dict2)

# print the merged dictionary
print(merged_dict)
    
