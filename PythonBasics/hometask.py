# Create a python script:
# 1. create list of 100 random numbers from 0 to 1000
# 2. sort list from min to max(without using sort())
# 3. calculate average for even and odd numbers
# 4. print both average result in console
# Each line of code should be commented with description.
# Commit script to git repository and provide link as home task result.
import random

# 1. Create list of 100 random numbers from 0 to 1000
# declare the empty list
randomList = []
# for each i in range from 0 to 100
# add an element at the end of the list using .append() and random.randint(range)
for i in range(0, 100):
    randomList.append(random.randint(0, 1000))
# print the randomList
# print(randomList)
# check the amount of elements in randomList using len() method
# print(len(randomList))

# 2. Sort list from min to max (without using sort())
# declare a new sorted list
sortedList = []
# use while to go through each element in an initial list
# find the minElement using min()
# add the minElement using append()
# remove the minElement using remove() to find new minValue
while randomList:
    minElement = min(randomList)
    sortedList.append(minElement)
    randomList.remove(minElement)
# print the sortedList
# print(sortedList)

# 3. Calculate average for even and odd numbers
# declare two lists for even and odd numbers
evenNumbersList = []
oddNumbersList = []
# for each element in the list goes through the list
# and if the modulo = 0, then it's even number, and we add it to evenNumbersList
# else it's odd number, and we add it to oddNumbersList
for currentElement in sortedList:
    if currentElement % 2 == 0:
        evenNumbersList.append(currentElement)
    else:
        oddNumbersList.append(currentElement)
# print lists
# print(evenNumbersList)
# print(len(evenNumbersList))
# print(oddNumbersList)
# print(len(oddNumbersList))
# declare two values for avg using sum(list)/len(list)
evenNumbersAvg = sum(evenNumbersList)/len(evenNumbersList)
oddNumbersAvg = sum(oddNumbersList)/len(oddNumbersList)
# print avg results and its round values
print(evenNumbersAvg, ' is round ', round(evenNumbersAvg))
print(oddNumbersAvg, ' is round ', round(oddNumbersAvg))
