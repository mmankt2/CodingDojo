#! /usr/local/bin/python3.7
def randInt(minimum=0, maximum=100):
  import random
  if minimum > maximum:
    return "maximum value must be greater than minimum value"
  if maximum < 0:
    return "maximum value must be greater than 0"
  num = random.random()*(maximum-minimum)+minimum
  return round(num)

print(randInt(minimum=110))