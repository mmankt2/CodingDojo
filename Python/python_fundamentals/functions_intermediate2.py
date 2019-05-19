#! /usr/local/bin/python3.7
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
  for key_name in some_list:
    print(some_list[key_name])

def printInfo(some_dict):
  for thing in some_dict:
    print(len(some_dict[thing]),thing)
    for val in some_dict[thing]:
      print(val)

if __name__ == "__main__":
  students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
  iterateDictionary(students) 
  # should output: (it's okay if each key-value pair ends up on 2 separate lines;
  """ # bonus to get them to appear exactly as below!)
  first_name - Michael, last_name - Jordan
  first_name - John, last_name - Rosales
  first_name - Mark, last_name - Guillen
  first_name - KB, last_name - Tonel """

  #iterateDictionary2('first_name',students)
  #iterateDictionary2('last_name',students)

  dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
  }
  printInfo(dojo)