def run01():
 def las_vegas_sqrt(number, max_attempts=10000):
     if number < 0:
         return 'no answer'

     for u in range(max_attempts):
         guess = number / 10

         for u in range(10):
             guess = ((guess + number / guess)) / 2

         if abs(guess * guess - number) < 0.00000001:
             return guess

     return 'no answer'

 num1 = 2435679
 num2 = 454
 num3 = 25

 result1 = las_vegas_sqrt(num1)
 result2 = las_vegas_sqrt(num2)
 result3 = las_vegas_sqrt(num3)

 print(f"Square root of {num1}: {result1}")
 print(f"Square root of {num2}: {result2}")
 print(f"Square root of {num3}: {result3}")


def run02():
    def euclidean_distance(x, y):
        return (x - y) ** 2

    def dynamic_time_warping(seq1, seq2):
        n = len(seq1)
        m = len(seq2)

        # Create a matrix to store DTW values
        dtw_matrix = [[float('inf')] * (m + 1) for _ in range(n + 1)]

        # Initialize the first row and first column with large values
        for i in range(n + 1):
            dtw_matrix[i][0] = float('inf')
        for j in range(m + 1):
            dtw_matrix[0][j] = float('inf')

        dtw_matrix[0][0] = 0

        # Calculate DTW values
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                cost = euclidean_distance(seq1[i - 1], seq2[j - 1])
                dtw_matrix[i][j] = cost + min(dtw_matrix[i - 1][j], dtw_matrix[i][j - 1], dtw_matrix[i - 1][j - 1])

        # Traceback to find the optimal alignment path
        i, j = n, m
        alignment_path = []

        while i > 0 and j > 0:
            if i > 0 and j > 0:
                min_neighbor = min(dtw_matrix[i - 1][j], dtw_matrix[i][j - 1], dtw_matrix[i - 1][j - 1])
                if dtw_matrix[i - 1][j] == min_neighbor:
                    i -= 1
                elif dtw_matrix[i][j - 1] == min_neighbor:
                    j -= 1
                else:
                    i -= 1
                    j -= 1

                # Only add to alignment path if the values match
                if seq1[i - 1] == seq2[j - 1]:
                    alignment_path.append((i - 1, j - 1))  # Subtract 1 to get the indices in seq1 and seq2

        alignment_path.reverse()

        return dtw_matrix[n][m], alignment_path

    seq1 = [1,2,3,4,5]
    seq2 = [2,3,4,5,6]

    distance, alignment_path = dynamic_time_warping(seq1, seq2)

    print(f"DTW Distance: {distance}")
    print("Alignment Path:")
    for i, j in alignment_path:
        print(f"({seq1[i]}, {seq2[j]})")






def run03():
    #def random(seed):
        #a = 1664525
        #c = 1013904223
        #m = 2 ** 32
        #seed = (a * seed + c) % m
        #return seed / m

    #def las_vegas_sqrt(number, max_attempts=10000):
        #if number < 0:
            #return 'no answer'

        #seed = 123456
    from random import randint

    def las_vegas_sqrt(number, max_attempts=10000):
        if number < 0:
            return 'no answer'

        seed = randint(2,15)

        for u in range(max_attempts):
            guess = number / seed

            # Rest of your code...

            for u in range(10):
                guess = ((guess + number / guess)) / 2

            if abs(guess * guess - number) < 0.00000001:
                return guess

        return 'no answer'

    num1 = 243567
    num2 = 45
    num3 = 25

    result1 = las_vegas_sqrt(num1)
    result2 = las_vegas_sqrt(num2)
    result3 = las_vegas_sqrt(num3)

    print(f"Square root of {num1}: {result1}")
    print(f"Square root of {num2}: {result2}")
    print(f"Square root of {num3}: {result3}")

def run04():
    import matplotlib.pyplot as plt
    import math

    def euclidean_distance(x, y):
        return math.sqrt((x - y) ** 2)

    def dynamic_time_warping(seq1, seq2):
        n = len(seq1)
        m = len(seq2)

        # Create a matrix to store DTW values
        dtw_matrix = [[float('inf')] * (m + 1) for _ in range(n + 1)]

        # Initialize the first row and first column with large values
        for i in range(n + 1):
            dtw_matrix[i][0] = float('inf')
        for j in range(m + 1):
            dtw_matrix[0][j] = float('inf')

        dtw_matrix[0][0] = 0

        # Calculate DTW values
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                cost = euclidean_distance(seq1[i - 1], seq2[j - 1])
                dtw_matrix[i][j] = cost + min(dtw_matrix[i - 1][j], dtw_matrix[i][j - 1], dtw_matrix[i - 1][j - 1])

        # Traceback to find the optimal alignment path
        i, j = n, m
        alignment_path = []

        while i > 0 and j > 0:
            if i > 0 and j > 0:
                min_neighbor = min(dtw_matrix[i - 1][j], dtw_matrix[i][j - 1], dtw_matrix[i - 1][j - 1])
                if dtw_matrix[i - 1][j] == min_neighbor:
                    i -= 1
                elif dtw_matrix[i][j - 1] == min_neighbor:
                    j -= 1
                else:
                    i -= 1
                    j -= 1

                # Only add to the alignment path if the values match
                if seq1[i - 1] == seq2[j - 1]:
                    alignment_path.append((i - 1, j - 1))  # Subtract 1 to get the indices in seq1 and seq2

        alignment_path.reverse()

        # Plot the DTW alignment
        dtw_values = [dtw_matrix[i][j] for i, j in alignment_path]
        plt.plot(range(len(dtw_values)), dtw_values, marker='o', linestyle='-', color='b')
        plt.xlabel('Alignment Step')
        plt.ylabel('DTW Value')
        plt.title('DTW Alignment')
        plt.show()

        return dtw_matrix[n][m], alignment_path

    seq1 = [1, 2, 3, 4, 5,6,7,8,9]
    seq2 = [4,6,8,9,10,11,12,13,14]

    distance, alignment_path = dynamic_time_warping(seq1, seq2)

    print(f"DTW Distance: {distance}")
    print("Alignment Path:")
    for i, j in alignment_path:
        print(f"({seq1[i]}, {seq2[j]})")





