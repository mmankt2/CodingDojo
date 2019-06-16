#!/usr/bin/python3
class MathDojo:
  def __init__(self):
    self.result = 0
  def add(self, num, *nums):
    self.result += num
    for x in nums:
      self.result += x
    return self
  def subtract(self, num, *nums):
    self.result -= num
    for x in nums:
      self.result -= x
    return self

md = MathDojo()

x = md.add(2).add(2).add(2).result
print(x) #print 6
md.result = 0

x = md.add(1,2,3).result
print(x) #print 6
md.result = 0

x = md.add(1,2,3,4).result
print(x) #print 10
md.result = 0

x = md.subtract(1).result
print(x) #print -1
md.result = 0

x = md.subtract(1,2).result
print(x) #print -3
md.result = 0

x = md.add(2).add(2,5,1).subtract(3,2).result
print(x) #print 5
