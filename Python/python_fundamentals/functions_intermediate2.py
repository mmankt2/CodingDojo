#! /usr/local/bin/python3.7

#2 iterate through a list of dictionaries
def iterateDictionary(some_list):
  #loop through each k:v pair
  #print the appropriate output
  for dict in some_list:
    output = []
    for key in dict:
      output.append("{} - {}".format(key, dict[key]))
    print("{}, {}".format(output[0],output[1]))
  pass

def iterateDictionary2(key_name, some_list):
  for dict in some_list:
    print(dict[key_name])

def printInfo(some_dict):
  for key in some_dict:
    print(len(some_dict[key]),key.upper())
    for val in some_dict[key]:
      print(val)

if __name__ == "__main__":
  x = [ [5,2,3], [10,8,9] ] 
  students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
  ]
  sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
  }
  z = [ {'x': 10, 'y': 20} ]
 #1.1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]. 
  x[1][0]=15
  #print(x)
 #1.2  Change the last_name of the first student from 'Jordan' to 'Bryant'
  students[0]['last_name'] = 'Bryant'
  #print(students)
  #1.3 In the sports_directory, change 'Messi' to 'Andres'
  sports_directory['soccer'][0] = 'Andres'
  #print(sports_directory)
#1.4 Change the value 20 in z to 30
  z[0]['y']=30
  #print(z)

  students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
  
  
  #2 Iterate Through a List of Dictionaries
  #iterateDictionary(students) 
  # should output: (it's okay if each key-value pair ends up on 2 separate lines;
  """ # bonus to get them to appear exactly as below!)
  first_name - Michael, last_name - Jordan
  first_name - John, last_name - Rosales
  first_name - Mark, last_name - Guillen
  first_name - KB, last_name - Tonel """

  #3 Get Values From a List of Dictionaries

  #iterateDictionary2('first_name',students)
  #iterateDictionary2('last_name',students)

  #4 Iterate Through a Dictionary with List Values
  dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
  }
  #printInfo(dojo)