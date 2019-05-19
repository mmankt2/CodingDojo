#! /usr/local/bin/python3.7
def selection_sort(myList):
  for j in range(len(myList)):
    minIndex = j
    for i in range(j,len(myList)):
      if myList[i] < myList[minIndex]:
        minIndex = i
    myList[minIndex], myList[j] = myList[j], myList[minIndex]
  return myList

print(selection_sort([8,5,2,6,3,4,9,1,7]))