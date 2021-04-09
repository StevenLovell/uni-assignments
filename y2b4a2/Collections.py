'''There are many different type of collections. This example will show lists, tuples, dictionaries and strings.
This example will also show a try and except debug block'''

# In python the index starts from 0
List = ['a', 'b', 'c', 'd', 'e'];    #A list can be changed at will.
List.append ('f');  #.append is a method that works with the list operations. It will add f to the end of the list
List.pop()  # Pop will remove either a given index or the item at -1. This is an example of a filo stack.
print (len(List))   #Aswell as methods operations also have functions. This function will print the length of the list.
for letter in List: #This for loop will print the list and it's index number, by iterating through the list.
    print(List.index(letter),letter)

Tuple = (1,2,3)   #A tuple is immutable.
print(Tuple*2)
'''This will multiply the tuple by 2. 
Rather than it being 2,4,6 it will instead be 1,2,3,1,2,3'''

Dictionary = {'Animal':'Lion', 'Name':'Bob', 'Age':6, 'Home':'Africa', 'Family':'Felidae'}
# A dictionary pairs keys with a value. While the value can change the key can't
print(Dictionary)               #This will print the Dictionary.
Dictionary.update (Age=7)     #This will change Bob's age from 6 to 7.
Dictionary['Name']='Hungry Bob'; #This is another way to change a dictionary key.
del Dictionary ['Home']         #This will delete Hungry Bob's home.
print(Dictionary.get('Age'))    #This will print Hungry Bobs New age.
print(Dictionary.get('Legs'))   #This will print None, due to their being no Legs key.
print(Dictionary)               #This will print the entire dictionary with the updated information.


String = 'A string is also a sequence'  #Since Python 3 all strings are stored as Unicode by default.
try:
    Print (String) #This would give an error due to the capital P in print. Python is case sensitive.
except NameError:   #Because I used the try and except command this enables the code to still run.
    print('Name Error')  #Instead of crashing, python wil now print the error code for the user.

List.
Tuple.
Set = {1,2,3}
Set.
