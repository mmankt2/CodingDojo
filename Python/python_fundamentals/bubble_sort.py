#! /usr/local/bin/python3.7

def bubble_sort(myList):
  for j in range(len(myList)):
    for i in range(len(myList)-1):
      counter = 0
      if myList[i] > myList[i+1]:
        myList[i], myList[i+1] = myList[i+1], myList[i]
        counter = 1
        #print(myList)
      if i == (len(myList)-1) and counter == 0:
        #print(myList)
        return myList
  return myList
      

y = bubble_sort([5,3,6,1,8,7,2,4])
print(y)