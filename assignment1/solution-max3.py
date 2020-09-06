'''
Team Members: Maxwell Molden, Jacob Lantzman, Spencer Leahy
'''

import fileinput

# The castToInt() function will take in the numbers that were read into an array from the input file along with the length read from the input
# file; it then iterates over the array and changes the type of each element to int and the type of the length to int and returns both
def castToInt(starting_arr, starting_len):
    starting_len = int(starting_len)

    for i in range(starting_len):
        starting_arr[i] = int(starting_arr[i])

    return starting_arr, starting_len

# The mergeSortedArrays() function will take in two arrays that are already sorted and produce an array that is the sorted, merged
# result of the two sorted arrays
def mergeSortedArrays(left_arr, right_arr): 
    out_arr = []

    # counter variables to track the index of the elements for comparisions and append()
    left_count = 0
    right_count = 0

    # Loop through each array and evaluate at each index which integer to insert into the output array,
    # if the length of either array becomes zero throughout the loop, append all remaining integers from
    # the other array to the output array
    while len(left_arr) > left_count and len(right_arr) > right_count:
        if(left_arr[left_count] < right_arr[right_count]):
            out_arr.append(left_arr[left_count])
            left_count += 1

        elif(left_arr[left_count] > right_arr[right_count]):
            out_arr.append(right_arr[right_count])
            right_count += 1

        elif(left_arr[left_count] == right_arr[right_count]):
            out_arr.append(left_arr[left_count])
            out_arr.append(right_arr[right_count])
            left_count += 1
            right_count += 1

    if len(left_arr) == left_count:
        for i in right_arr[right_count:]:
            out_arr.append(int(i))

    elif len(right_arr) == right_count:
        for i in left_arr[left_count:]:
            out_arr.append(int(i))

    return out_arr

# the mergeSort() function takes in an array along with its size, and the (initially empty) resultant array. It follows the merge-sort algorithm
# to split an array of n elements into n single-element-arrays and recombines them using the mergeSortedArrays() funciton.  mergeSort() is called
# recursively in order to continue splitting the arrays into smaller arrays.  If the array length to start is <= 1, the array is already sorted
# and will be returned
def mergeSort(orig_array, orig_size, sort_arr): 
    if orig_size > 1:
        # splitting the arrays as close to in half as possible, done recursively
        midpoint = orig_size // 2
        leftArray = orig_array[:midpoint]
        rightArray = orig_array[midpoint:]

        left_len = len(leftArray)
        right_len = len(rightArray)

        mergeSort(leftArray, left_len, sort_arr)
        mergeSort(rightArray, right_len, sort_arr)

        sort_arr = mergeSortedArrays(leftArray, rightArray)

    else:
        return sort_arr

    return sort_arr
    

# Main function to drive the code and take inputs
def main():
    hold = []
    test = ""
    length = ""
    array3 = []
    arrayInit = []
    for line in fileinput.input():
        test += line
    hold = test.split('\n')
    length = hold.pop(0)
    arrayInit = hold[0].split()
    arrayInit, length = castToInt(arrayInit, length)
    array3 = mergeSort(arrayInit, length, array3)

    # Parse the array for output dictated by the assignment guidelines
    output = ""
    for x in array3:
        output += str(x) + " "
    print(output.rstrip())


if __name__ == '__main__':
    main()
