#! /usr/bin/python3

#1 Basic - Print all integers from 0 to 150.

def print_ints():
  int = 0
  while int < 151:
    print(int)
    int += 1

#2 Multiples of Five - Print all the multiples of 5 from 5 to 1,000
def print_multiples():
  fives = 5
  while fives < 1001:
    print(fives)
    fives += 5

#3 Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def counting():
  for i in range(1,100):
    if i%10==0:
      print("Coding Dojo")
    elif i%5==0:
      print("Coding")
    else:
      print(i)

#4 Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def huge():
  sum = 0
  for i in range(1,500000,2):
    sum = sum + i
  print(sum)

#5 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

def count_down():
  i = 2018
  while i > 0:
    print(i)
    i = i - 4

#6 Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def flexible_counter():
  lowNum = 2
  highNum = 9
  mult = 3
  for i in range(lowNum,highNum+1):
    if i%3==0:
      print(i)

if __name__ == "__main__":
  #print_ints()
  #print_multiples()
  #counting()
  #huge()
  #count_down()
  flexible_counter()
