import fileinput

# The castToInt() function will take in the numbers that were read into an array from the input file along with the length read from the input
# file; it then iterates over the array and changes the type of each element to int and the type of the length to int and returns both
def castToInt(starting_arr, starting_len):
    starting_len = int(starting_len)

    for i in range(starting_len):
        starting_arr[i] = int(starting_arr[i])

    return starting_arr, starting_len
    

# The mergeSortedArrays() function code from PA1 Problem one is used will take in two arrays that are already sorted and produce an array that is 
# the sorted, merged result of the two sorted arrays

# The mergeSort() function takes in the initial array and length as type int and follows the merge-sort algo to split the array in half, this is 
# done recursively until an array of size n has been split into n single-element arrays, these arrays are then recombined through comparisons
# into a final sorted array
def mergeSort(arrayInit, length): 

    if length > 1:
        
        # splitting the input array in half per the merge-sort algo
        leftArray = []
        rightArray = []
        midpoint = length // 2
        x = 0
        while x < midpoint:
            leftArray.append(arrayInit[x])
            x += 1

        while x < length:
            rightArray.append(arrayInit[x])
            x += 1

        # recursive call on each half of the array
        mergeSort(leftArray, len(leftArray))
        mergeSort(rightArray, len(rightArray))
        
        # counter variables to track the index of the two separate halves
        left_count = 0
        right_count = 0

        # counter variable track index of output array
        total_count = 0

        # This is the code from mergeSortedArrays()
        # Loop through each array and evaluate at each index which integer to insert into the output array,
        # if the length of either array becomes zero throughout the loop, append all remaining integers from
        # the other array to the output array
        while len(leftArray) > left_count and len(rightArray) > right_count:

            if(leftArray[left_count] < rightArray[right_count]):
                arrayInit[total_count] = leftArray[left_count]
                left_count += 1
            else:
                arrayInit[total_count] = rightArray[right_count]
                right_count += 1
            total_count += 1

        # check for any elements left in each of the two halves that were not appended yet
        while len(leftArray) > left_count:
            arrayInit[total_count] = leftArray[left_count]
            left_count += 1 
            total_count += 1

        while len(rightArray) > right_count:
            arrayInit[total_count] = rightArray[right_count]
            right_count += 1
            total_count += 1
    return arrayInit

# Main function to drive the code and take inputs
def main():
    hold = []
    test = ""
    length = ""
    array3 = []
    for line in fileinput.input():
       test += line
    hold = test.split('\n')
    length = hold.pop(0)
    arrayInit = hold[0].split()
    arrayInit, length = castToInt(arrayInit, length)
    array3 = mergeSort(arrayInit, length)

    # Parse the array for output dictated by the assignment guidelines
    output = ""
    for x in array3:
        output += str(x) + " "
    print(output.rstrip())

if __name__ == '__main__':
    main() 
