# # Problem Description

# # Merge two sorted arrays of integers into a single sorted array.

# # Input

# # Two lines, each line describes a sorted array.  The first number in the line gives
# # `n`, the number of integers in the array, and the following `n` numbers give
# # the `n` integers in the array. All numbers are separated by space.

# # We can assume that 0 <= n <= 100000, and that each number in the arrays
# # are in the range of [-2147483648, 2147483647]. 

# # Your code should read the input from standard input (e.g. input()/raw_input() for Python and cin/scanf for C++).

# # Output

# One line, describing the merged sorted array,
# with the first integer being the total number of integers in the merged array,
# and the following integer give all numbers in the merged array. 

# Your code should write the output to standard output (e.g. print for Python and cout/printf for C++).

# # Requirement

# Your algorithm should run in linear time, i.e., you are not allowed
# to call any in-built sort function.

# Time limtation: 5 seconds.

# Memory limitation: 1.0GB.

# # Environment

# Your code will be running on Ubuntu 18.04.5.

# Now only accept C++ and Python2/Python3 code, g++ version 7.5.0 and Python versions are Python 2.7.17 and Python 3.6.9.

# # Examples

# An example (input-1.txt and output-1.txt) is provided.

# # Submission

# If you want to upload a single file, make sure the file is named as `solution.py` or `solution.cpp`.
# If you submit via GitHub, make sure your file is located in directory `assignment1/problem1/solution.py` or `assignment1/problem1/solution.cpp`.


def mergeSortedArrays(array1, array2): 
    array1Length = array1.pop(0)
    array2Length = array2.pop(0)

    for x in array1: 
        array1[array1.index(x)] = int(array1[x])
    for y in array2: 
        array2[array2.index(x)] = int(array2[x])

    x1 = 0
    x2 = 0
    x3 = 0
    loop = array1Length + array2Length
    array3 = []
    while loop > 0: 
        if(array1[x1] < array2[x2]):
            array3[x3] = array1[x1]
            x1 += 1
            x3 += 1
        if(array1[x1] > array2[x2]):
            array3[x3] = array2[x2]
            x2 += 1
            x3 += 1
        if(array1[x1] == array2[x2]):
            array3[x3] = array1[x1]
            x3 += 1
            array3[x3] = array2[x2]
            x1 += 1
            x2 += 1
            x3 += 1
        loop -= 1
        

def main():
    input1 = input("Enter the first sorted array: ")
    input2 = input("Enter the second sorted array: ")
    array1 = input1.split()
    array2 = input2.split()
    mergeSortedArrays(array1, array2)

if __name__ == '__main__':
    main()