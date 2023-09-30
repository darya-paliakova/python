# 1. create a list of random number of dicts (from 2 to 10)
# - dict random numbers of keys should be letters,
# - dict values should be a number (0-100),
# - example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
# 2. get previously generated list of dicts and create one common dict:
# - if dicts have same key, we will take max value, and rename key with dict number with max value
# - if key is only in one dict - take it as is,
# - example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.
# Commit script to git repository and provide link as home task result.


# 1. Create a list of random number of dicts (from 2 to 10)
# import random to use random methods to generate the list
import random
import string

# declare new variable new list
newList = []

# generate random number of dicts (from 2 to 10) for the list
for elementList in range(random.randint(2,10)):
    newList.append(dict())

# for each dict in the list
# for each item in the dict set up random amount of items
# set up keys and values in the following format dict['keys'] = value
for dictionary in newList:
    for item in range(1, 5):
        dictionary[''.join(random.choices(string.ascii_letters))] = random.randint(1,100)
    print('The', newList.index(dictionary), 'item is', dictionary.items())

print(newList)

# 2. get previously generated list of dicts and create one common dict:
# - if dicts have same key, we will take max value, and rename key with dict number with max value
# - if key is only in one dict - take it as is,
# - example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

# declare intervalDict dictionary
# for each dictionary in the list
# for each key and value in dictionary.items
# return the value(s) for the specific key in the interval dictionary
intervalDict = {}
for dictionary in newList:
    for key, value in dictionary.items():
        intervalDict.setdefault(key, []).append(value)
print(intervalDict)

# declare the resultDict dictionary
# for each key and value in dictionary.items
# if the length of value is more than 1
# then the set up the corresponding name for keys and the max value as value
# else set up as it is
resultDict = {}
for key, value in intervalDict.items():
    if len(value) > 1:
        resultDict[key+'_'+str(value.index(max(value))+1)] = max(value)
    else:
        resultDict[key] = value[0]

print(resultDict)

