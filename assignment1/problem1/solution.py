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


import fileinput
# The mergeSortedArrays function will take in two arrays that are already sorted and produce an array that is the sorted, merged
# result of the two sorted arrays
def mergeSortedArrays(array1, array2): 

    # Extract the array length from the first integer of each array
    array1Length = int(array1.pop(0))
    array2Length = int(array2.pop(0))

    # Convert each item in the array to an integer
    array1 = map(int, array1)
    array2 = map(int, array2)

    # Initialize the loop variable and the output array, in this case the output array is called array3
    array3 = []

    # Loop through each array and evaluate at each index which integer to insert into the output array,
    # if the length of either array becomes zero throughout the loop, append all remaining integers from
    # the other array to the output array
    while len(array1) != 0 and len(array2) != 0: 
        if(array1[0] < array2[0]):
            array3.append(array1[0])
            array1.pop(0)
        elif(array1[0] > array2[0]):
            array3.append(array2[0])
            array2.pop(0)
        elif(array1[0] == array2[0]):
            array3.append(array1[0])
            array3.append(array2[0])
            array1.pop(0)
            array2.pop(0)

    if(len(array1) == 0):
        for i in array2:
            array3.append(int(i))
    elif(len(array2) == 0):
        for i in array1:
            array3.append(int(i))
    
    # Insert the final sorted array length into the beginning of the array
    array3.insert(0, len(array3))

    # Parse the array for output dictated by the assignment guidelines
    output = ""
    for x in array3:
        output += str(x) + " "
    print(output.rstrip())

# Main function to drive the code and take inputs
def main():
    hold = []
    test = ""
    array1 = []
    array2 = []
    for line in fileinput.input():
        test += line
    hold = test.split('\n')
    array1 = hold[0].split()
    array2 = hold[1].split()
    mergeSortedArrays(array1, array2)

if __name__ == '__main__':
    main()
