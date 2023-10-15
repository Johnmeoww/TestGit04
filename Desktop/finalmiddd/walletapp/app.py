#Variables (Midterm)
#Loop (Midterm)
#IF (Midterm)
#Function (Midterm)

#Data Structure
def run01():
###### LIST #########

# Creating an empty list
 empty_list = []

# Creating a list with elements
 my_list = [1, 2, 3, 4, 5]

# Lists can contain elements of different types
 mixed_list = [1, "hello", 3.14, True]

# Nested lists (lists within a list)
 nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements by index
 print(my_list[0])  # Output: 1
 print(my_list[2])  # Output: 3

# Negative indices can be used to access elements from the end
 print(my_list[-1])  # Output: 5

# Slicing a list
 subset = my_list[1:4]  # Creates a new list with elements at index 1, 2, and 3
 print(subset)  # Output: [2, 3, 4]

# Modifying elements
 my_list[2] = 99
 print(my_list)  # Output: [1, 2, 99, 4, 5]

# Adding elements to the end of the list
 my_list.append(6)
 print(my_list)  # Output: [1, 2, 99, 4, 5, 6]

# Removing elements by value
 my_list.remove(4)
 print(my_list)  # Output: [1, 2, 99, 5, 6]

# Removing elements by index
 del my_list[1]
 print(my_list)  # Output: [1, 99, 5, 6]

# Length of a list
 length = len(my_list)
 print(length)  # Output: 4


#### ARRAY #####
import numpy as np
def run02():

 # NumPy array
 my_array = np.array([1, 2, 3, 4, 5])

 # Adding a new element to the array (NumPy arrays are fixed size, so a new array is created)
 my_array = np.append(my_array, 6)

 # Modifying an element
 my_array[2] = 99

 # Removing an element by index (NumPy arrays are fixed size, so a new array is created)
 my_array = np.delete(my_array, 3)

 print("\nNumPy Array:")
 print(my_array)


##### Linked List (Midterm) #########
#def run03():
 # Linked List of String

class Node:
  def __init__(self, value=None):
   self.value = value
   self.next = None

class LinkedList:
  def __init__(self):
   self.first_node = None
   self.size = 0

  def append(self, node):
   if self.first_node is None:
    self.first_node = node
   else:
    current_node = self.first_node
    while not (current_node.next is None):
     current_node = current_node.next

    current_node.next = node
   self.size += 1

  def list(self):
   result = ''
   if self.first_node is None:
    result = 'Empty LinkedList'
   else:
    current_node = self.first_node
    while not (current_node.next is None):
     result = result + current_node.value + ', '
     current_node = current_node.next
    result = result + current_node.value
   return result

def run03():
  my_linked_list = LinkedList()
  node01 = Node('Raiden Shogun')
  node02 = Node('Venti')
  node03 = Node('Barbara')

  my_linked_list.append(node01)
  my_linked_list.append(node02)
  my_linked_list.append(node03)

  print(my_linked_list.list())
  print(my_linked_list.size)

######- Python Class #####
class Weapon:
   def __init__(self, name, weapon_type):
    self.__name = name
    self.__weapon_type = weapon_type
    self.__level = 1

   def getName(self):
    return self.__name

   def getWeapon_type(self):
    return self.__weapon_type


class Character:
 def __init__(self, name, vision, weapon_type):
  default_weapon = Weapon('None', 'None')

  self.__character_name = name
  self.__vision = vision
  self.__level = 1
  self.__weapon_type = weapon_type
  self.__weapon = default_weapon
  # constructor

 def levelup(self):
  self.__level += 1

 def display(self):
  print(self.__character_name + ' ' + self.__vision + ' Level:' + str(self.__level))

 def display2(self):
  return self.__character_name + ' ' + self.__vision + ' Level:' + str(self.__level)

 def display3(self):
  return self.__character_name + ' ' + self.__vision + ' Level:' + str(self.__level) + ' ' + self.getWeapon().getName()

 def setCharacterName(self, new_name):
  self.__character_name = new_name

 def setWeapon(self, weapon):
  # print (self.__weapon_type)
  # print (weapon.getWeapon_type())
  if self.__weapon_type == weapon.getWeapon_type():
   self.__weapon = weapon
   return True
  else:
   print(self.__character_name + ' cannot hold the ' + weapon.getName())
   return False

 def getWeapon(self):
  return self.__weapon


def run04():
 print('Python class')
 barbatos = Character('Venti', 'Anemo', 'Bow')
 # create instance 'barbatos' from class 'Character'
 amos_bow = Weapon('Amos Bow', 'Bow')
 barbatos.setWeapon(amos_bow)
 print(barbatos.display3())

 beelzebub = Character('Ei', 'Electro', 'Polearm')
 beelzebub.setWeapon(amos_bow)

 engulfing_lightning = Weapon('Engulfing Lightning', 'Polearm')
 beelzebub.setWeapon(engulfing_lightning)

 print(beelzebub.display3())



######## Built-in Queue #########
## Master 06 ####

from queue import Queue

def run05():
# Creating a FIFO queue
 my_queue = Queue()

# Enqueue (put) elements into the queue
 my_queue.put(1)
 my_queue.put(2)
 my_queue.put(3)

# Dequeue (get) elements from the queue
 item1 = my_queue.get()
 item2 = my_queue.get()
 item3 = my_queue.get()

 print("Dequeued items:", item1, item2, item3)


######### Built-in Stack ##########
from queue import LifoQueue
def run_stack():
 # Initializing
 stack = LifoQueue(maxsize=3)
 stack.put(12)  # Python built-in use "tut" for Push
 stack.put(22)
 stack.put(32)


 if stack.full():
  print("Full")
 else:
  print("Not full")

 print("Now, POP() the element out of Stack")

 print(stack.get())  # Python built-in use "Get" for Dequeue

 if stack.full():
  print("Full")
 else:
  print("Not full")

 print(stack.get())
 print(stack.get())

 if stack.empty():
  print("Empty")
 else:
  print("Not empty")

 print('Number of elements in a stack:' + str(stack.qsize()))


def run06():
 run_stack()


######## - Dictionary (Midterm) ##########

def run07():
# Empty dictionary
 empty_dict = {}

# Dictionary with key-value pairs
 my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Using the dict() constructor
 another_dict = dict(name='Alice', age=30, city='London')

# Accessing values using keys
 name_value = my_dict['name']
 age_value = my_dict['age']

# Modifying a value
 my_dict['age'] = 26

# Adding a new key-value pair
 my_dict['occupation'] = 'Engineer'

# Removing a key-value pair
 del my_dict['city']

# Using pop() to remove and return a value by key
 age_value = my_dict.pop('age')

# Get a list of all keys
 keys_list = my_dict.keys()

# Get a list of all values
 values_list = my_dict.values()

# Get a list of key-value pairs as tuples
 items_list = my_dict.items()

# Iterating over keys
 for key in my_dict:
    print(key, my_dict[key])

# Iterating over items (key-value pairs)
 for key, value in my_dict.items():
    print(key, value)

#https://github.com/omiejung01/MyPythonLesson/tree/master04
#Topic on Github
#<master01> Variable Scope
#<master03> FindMax and Running time analysis
#<master04> Recursion, List and String
#<master06> Queue and Stack
#<master07> Assignment 1 solution
#<master08> Class composition
#<master09> Python Class and Linked List
#<master12> Range and Date
#<master14> Midterm Solution
#<master16> Bubble Sort and Quicksort Algorithm
#<master23> Monte Carlo in business
#<master24> Different Probabilities, Time-in Time-out Threshold

#import walletapp.app as app
#if __name__ == '__main__':
    #app.run01()
    #app.run02()
    #app.run03()
    #app.run04()
    #app.run05()  #Queue
    #app.run06()  #Stack
    #app.run07()



