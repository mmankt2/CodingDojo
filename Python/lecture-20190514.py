
# Print Ints and Sum 0-255 
# Print integers from 0 to 255, and the sum so far.
def print_ints_and_sums():
    number=1
    sum=0
    while number <=255:
        sum = sum + number
        print(number)
        print(sum)
        number+=1

# Find and Print Max 
# Print the largest element in a given array. 
def find_max(array):
  max=array[0]
  for i in range (len(array)):
    if array[i]>max:
      max=array[i]
  print(max)

# Print Odds 1-255 
# Prints all odd integers from 1 to 255
def odds():
  for i in range (1,256,2):
    print(i)

# Array with Odds
# Create an array with odd integers from 1-255.
def oddsarray():
  array=[]
  for i in range(1,256,2):
    array.append(i)
  return array

# Iterate and Print Array 
# Print all values in a given array. 
def iterate_print_array(array):
  for i in array:
    print(i)

# Get and Print Average 
#analyze an arrays values and print the average
def get_print_avg(array):
  average=array[0]

# Greater than Y 
# Count and print the number of array values less than a given Y. 

# Max, Min, Average 
# Given an array, print max, min and average values. 

# Square the Values 
# Given an array, square each value in the array.  

# Zero Out Negative Numbers 
# Set negative array values to zero.  

# Shift Array Values
# Shift array values: drop the first and leave '0' at end.  

# Swap String for Array Negative Values
# Replace any negative array values with 'Dojo'. 
if __name__ == "__main__":  
    #makes sure that the codes won't run if someone else uses the code
    #so it makes the functions available to other people if they want, but
    #it won't run the things.
    #print_1_to_255()
    print_ints_and_sums()
    find_max([1,2,3,4,6,4,3])
    odds()
    print(oddsarray())
    iterate_print_array(["a","b","c"])



#dictionaries
x={}
x['newthing']=42
print(x['newthing'])
#dictionaries can be iterated
#if, else, elif
#True and False get capitalized
#can use 'is' 'not' and 'or' when comparing
#can do something cool:
x="Melissa" if 2+2=4 else "Paul" #this checks the statement 2+2=4
print(x)

#use PEP 8 for help with styling python code
#see docs.python.org/3/library for more information about python modules
