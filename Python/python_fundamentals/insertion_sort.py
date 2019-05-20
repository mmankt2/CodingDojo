#! /usr/local/bin/python3.7

def insertion_sort(myList):
  for i in range(1,len(myList)):
    j = i -1
    minIndex = j
    while j >= 0:
      if myList[i] < myList[j]:
        minIndex = j
      j -= 1
    if myList[minIndex]>myList[i]:
      temp = myList[i]
      myList.pop(i)
      myList.insert(minIndex,temp)
  return myList  



print(insertion_sort([5,6,3,1,8,7,2,4]))