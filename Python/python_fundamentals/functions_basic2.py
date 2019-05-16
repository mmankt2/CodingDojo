#! /usr/bin/python3
def countdown(num):
  new_list = []
  for i in range(num,0,-1):
    new_list.append(i)
  return new_list

def print_return(list):
  print(list[0])
  return list[1]

def first_plus_length(list):
  length = len(list)
  first = int(list[0])
  return first + length

def vals_greater_than_second(list):
  compare_to = list[1]
  new_list=[]
  for i in list:
    if i > compare_to:
      new_list.append(i)
  return new_list

def length_and_value(size,value):
  i = 0
  list = []
  while i<size:
    list.append(value)
    i += 1
  return list
  
if __name__ == "__main__":
  #print(countdown(5))
  #y = print_return([4,5])
  #y = first_plus_length([2,3,4,5])
  #y = vals_greater_than_second([5,2,3,2,1,4])
  y = length_and_value(4,7)
  print(y)

