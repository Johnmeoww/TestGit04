#Recursive
def run01():
 def iterative_factorial(n):
     fact = 1
     for i in range(2,n + 1):
         fact *= i
     return fact
 print(iterative_factorial(4))

#Recursiveeeeee
def run02():
 def recursive_factorial(n):
     if n == 1:
         return n
     else:
         temp = recursive_factorial(n-1)
         return temp * n
 print(recursive_factorial(4))

 #Recusive + purmutation
def run03():
 def permute(string, pocket=""):
     if len(string) == 0:
         print(pocket)
     else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)

 print(permute("ABC",""))

#Bubble sort
def run04():
 def bubble_sort(A):
     iterations = 0
     for i in range(len(A)):
         for j in range(len(A)-i-1):
            iterations += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
     return A, iterations
 A = [6,8,7,5,9,1]
 print(bubble_sort(A))


#Quick sort
def run05():
    import sorting
    import sorting.QuickSort as quicksort
    my_list = [10, 6, 2, 7, 1, 2, 9, 3, 5]

    # Create an instance of QuickSort
    sorter = quicksort.QuickSort()

    # Use the divide method (assuming this method exists in your QuickSort class)
    str_result = str(sorter.divide(my_list))

    # Print the result
    print(str_result)

#Dictionary Sort
def run06():   # sort by alphabet
 my_dict = {'banana': 3, 'apple': 2, 'orange': 5, 'grape': 1}

# Sorting by keys
 sorted_dict_by_keys = dict(sorted(my_dict.items()))

 print("Sorted by Keys:")
 print(sorted_dict_by_keys)

# Sorting by values ####
 sorted_dict_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))

 print("\nSorted by Values:")
 print(sorted_dict_by_values)


##from operator import itemgetter

 # Sorting by values using itemgetter
 ##sorted_dict_by_values = dict(sorted(my_dict.items(), key=itemgetter(1)))
 # Sorting by values in descending order
 ##sorted_dict_by_values_desc = dict(sorted(my_dict.items(), key=itemgetter(1), reverse=True))


#Monte Carlo simulation
import random
import math
def run07():

     count_square = 0
     count_circle = 0
     for num in range(0,1000000):
          x = random.randint(-100, 100)
          y = random.randint(-100, 100)

     print("x = " + str(x))
     print("y = " + str(y))

     if (x >= 0) and (y >= 0):
         count_square += 1
     if math.sqrt(pow(x, 2) + pow(y, 2)) < 10000:
         count_circle += 1

     pi = count_circle / count_square

     print("Pi value is" + str(pi))




#Regular Expression
import re
def run08():

  text = "The quick brown fox jumps over the lazy dog."
  pattern = re.compile(r'\b\w{3,5}\b')

# Search for the pattern in the text
  matches = pattern.findall(text)

# Print the matches
  print(matches)




# Euclidean Distance
import math
def run09():
 def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Example usage
 point1 = (1, 1)
 point2 = (5, 4)

 distance = euclidean_distance(point1, point2)
 print(f"The Euclidean distance between {point1} and {point2} is {distance:.2f}")




#Manhattan Distance
def run10():
 def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    distance = abs(x2 - x1) + abs(y2 - y1)
    return distance

# Example usage
 point1 = (1, 1)
 point2 = (5, 4)

 distance = manhattan_distance(point1, point2)
 print(f"The Manhattan distance between {point1} and {point2} is {distance}")





#Real world case study - Time-in, Time-out

import random
def run11():
# Different probabilities and Time-in Time-out Threshold
 def my_scenario():
    # scenario_a = 15%
    # scenario_b = 25%
    # scenario_c = 40%
    # scenario_d = 30%

    condition = random.randint(1, 20)

    if condition in [1, 2, 3]:
        return 'a'
    elif condition in [4, 5, 6, 7, 8]:
        return 'b'
    elif condition in [9, 10, 11, 12, 13, 14, 15, 16]:
        return 'c'
    else:
        return 'd'


 def random_with_prob():
    # generate result 10,000 time and count
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0

    for x in range(0, 10000):
        result = my_scenario()
        if result == 'a':
            count_a += 1
        elif result == 'b':
            count_b += 1
        elif result == 'c':
            count_c += 1
        else:
            count_d += 1

    print('a: ' + str(count_a))
    print('b: ' + str(count_b))
    print('c: ' + str(count_c))
    print('d: ' + str(count_d))


 def working_hour(time_in, time_out):
    #  Format xx:xx
    # 1 Time-in cut-off 15-minute after
    # 2 Time-out cut-off 15-minute before
    # 3 Error if time-out before or equal time-in

    in_hour = int(time_in[0:2])
    in_minute = int(time_in[3:5])
    if in_minute <= 15:
        in_minute = 15
    elif in_minute <= 30:
        in_minute = 30
    elif in_minute <= 45:
        in_minute = 45
    else:
        in_minute = 0
        in_hour += 1

    print(in_hour)
    print(in_minute)

    out_hour = int(time_out[0:2])
    out_minute = int(time_out[3:5])
    if out_minute <= 15:
        out_minute = 0
    elif out_minute <= 30:
        out_minute = 15
    elif out_minute <= 45:
        out_minute = 30
    else:
        out_minute = 45

    print(out_hour)
    print(out_minute)

    duration_minute = ((out_hour * 60) + out_minute) - ((in_hour * 60) + in_minute)

    if duration_minute <= 0:
        return 'Error!!'

    str_hour = str(duration_minute // 60) + ' hour(s)'
    if duration_minute < 60:
        str_hour = ''

    str_minute = str(duration_minute - (duration_minute // 60) * 60) + ' minute(s)'
    if duration_minute - (duration_minute // 60) == 0:
        str_minute = ''

    return str_hour + ' ' + str_minute


 def timein_timeout():
    print(working_hour('11:00', '17:45'))


 if __name__ == '__main__':
    random_with_prob()
    timein_timeout()



#Real world case study - Data Compression

import zlib
def run12():

 data = b"Good Morning Teacher"

# Compress data
 compressed_data = zlib.compress(data)

 print("Original size:", len(data))
 print("Compressed size:", len(compressed_data))

# Decompress data
 decompressed_data = zlib.decompress(compressed_data)

 print("Decompressed data:", decompressed_data.decode('utf-8'))

# Using gzip

 # Compress
#import gzip

#data = b"Hello, this is some data to compress."

#with gzip.open('compressed_data.gz', 'wb') as f:
    #f.write(data)

    # Decompress
#import gzip

#with gzip.open('compressed_data.gz', 'rb') as f:
    #decompressed_data = f.read()

#print("Decompressed data:", decompressed_data.decode('utf-8'))


### ADD MORE THAN ONE ALGORITHM ##

#1.
class AlgorithmOne:
    def __init__(self, input_data):
        self.input_data = input_data

    def run(self):
        # Implementation of algorithm one
        result = self.input_data * 2
        return result

class AlgorithmTwo:
    def __init__(self, input_data):
        self.input_data = input_data

    def run(self):
        # Implementation of algorithm two
        result = self.input_data ** 2
        return result

# Example usage
data = 5

algorithm_one_instance = AlgorithmOne(data)
algorithm_two_instance = AlgorithmTwo(data)

result_one = algorithm_one_instance.run()
result_two = algorithm_two_instance.run()

print("Result from Algorithm One:", result_one)
print("Result from Algorithm Two:", result_two)

#2.
def algorithm_one(input_data):
    # Implementation of algorithm one
    result = input_data * 2
    return result

def algorithm_two(input_data):
    # Implementation of algorithm two
    result = input_data ** 2
    return result

# Example usage
data = 5

result_one = algorithm_one(data)
result_two = algorithm_two(data)

print("Result from Algorithm One:", result_one)
print("Result from Algorithm Two:", result_two)



