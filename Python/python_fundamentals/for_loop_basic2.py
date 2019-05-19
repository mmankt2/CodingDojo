#! /usr/bin/python3
#1 Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
        #Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(myList):
  for i in range(len(myList)):
    if myList[i]>0:
      myList[i]='big'
  return myList
  
#2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
   #     Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
   #     Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(myList):
  counter = 0
  for i in myList:
    if i > 0:
      counter +=1
  myList[-1]=counter
  return myList

#3Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
  #      Example: sum_total([1,2,3,4]) should return 10
  #      Example: sum_total([6,3,-2]) should return 7
def sum_total(myList):
  sum = 0
  for i in myList:
    sum += i
  return sum 

#4  Average - Create a function that takes a list and returns the average of all the values.
  #      Example: average([1,2,3,4]) should return 2.5
def average(myList):
  avg = 0
  for i in myList:
    avg += i
  avg = avg/len(myList)
  return avg

#5 Length - Create a function that takes a list and returns the length of the list.
  #      Example: length([37,2,1,-9]) should return 4
  #      Example: length([]) should return 0
def length(myList):
  return len(myList)

#6  Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
  #      Example: minimum([37,2,1,-9]) should return -9
  #      Example: minimum([]) should return False
def minimum(myList):
  if len(myList)<=0:
    return False
  return min(myList)

#7 Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
  #      Example: maximum([37,2,1,-9]) should return 37
  #      Example: maximum([]) should return False
def maximum(myList):
  if len(myList)<=0:
    return False
  return max(myList)

#8  Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
  #      Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(myList):
  mySum = sum(myList)
  myAvg = mySum/len(myList)
  myMin = min(myList)
  myMax = max(myList)
  return {'sumTotal':mySum, 'average':myAvg, 'minimum':myMin, 'maximum':myMax, 'length':len(myList)}

#9 Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
  #      Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(myList):
  steps = int(len(myList)/2)
  for i in range(steps):
    hold = myList[i]
    myList[i] = myList[len(myList)-1-i] 
    myList[len(myList)-1-i]=hold
  return myList

if __name__ == "__main__":
  #print(reverse_list([37,2,1,-9,0]))
  #print(ultimate_analysis([37,2,1,-9]))
  #print(maximum([37,2,1,-9]))
  #print(minimum([]))
  #print(length([37,2,1,-9]))
  #print(average([1,2,3,4]))
  #print(sum_total([1,2,3,4]))
  #print(count_positives([-1,1,1,1]))
  #print(biggie_size([-1,3,5,-5]))