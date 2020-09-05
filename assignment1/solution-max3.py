'''
Team Members: Maxwell Molden, Jacob Lantzman, Spencer Leahy
'''

import fileinput
# The mergeSortedArrays function will take in two arrays that are already sorted and produce an array that is the sorted, merged
# result of the two sorted arrays

def castToInt(starting_arr, starting_len):
    starting_len = int(starting_len)

    for i in range(starting_len):
        starting_arr[i] = int(starting_arr[i])

    return starting_arr, starting_len


def mergeSortedArrays(left_arr, right_arr): 
    out_arr = []

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

    # print(f"out arr {out_arr}")

    return out_arr

def mergeSort(orig_array, orig_size, sort_arr): 
    orig_size = int(orig_size)

    if orig_size > 1:
        midpoint = orig_size // 2
        leftArray = orig_array[:midpoint]
        rightArray = orig_array[midpoint:]

        # print(f"left before: {leftArray}")
        # print(f"rigth before: {rightArray}")
        # print(f"type left: {type(leftArray)}")
        # print(f"type right: {type(rightArray)}")

        left_len = len(leftArray)
        right_len = len(rightArray)

        # print(f"left len: {left_len}")
        # print(f"rigth len: {right_len}")

        leftArray, rightArray = mergeSort(leftArray, left_len, sort_arr), mergeSort(rightArray, right_len, sort_arr)

        sort_arr = mergeSortedArrays(leftArray, rightArray)
    else:
        return sort_arr


        #print(sort_arr)

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
