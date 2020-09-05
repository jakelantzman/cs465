import fileinput
# The mergeSortedArrays function will take in two arrays that are already sorted and produce an array that is the sorted, merged
# result of the two sorted arrays

def makeSubArray(arrayInit, length):
    arrayInit = list(map(int, arrayInit))
    length = int(length)

    midpoint = length // 2
    leftArray = arrayInit[:midpoint]
    rightArray = arrayInit[midpoint+1:]

    # print(f"midpoint {midpoint}")
    # print(f"left arr {leftArray}")
    # print(f"right arr {rightArray}")

    return leftArray, rightArray

def mergeSortedArrays(left_arr, right_arr, out_arr): 

    # Convert each item in the array to an integer
    array1 = list(map(int, left_arr))
    array2 = list(map(int, right_arr))



    # Loop through each array and evaluate at each index which integer to insert into the output array,
    # if the length of either array becomes zero throughout the loop, append all remaining integers from
    # the other array to the output array
    while len(left_arr) != 0 and len(right_arr) != 0: 
        if(left_arr[0] < right_arr[0]):
            out_arr.append(left_arr[0])
        elif(left_arr[0] > right_arr[0]):
            out_arr.append(right_arr[0])
        elif(left_arr[0] == right_arr[0]):
            out_arr.append(left_arr[0])
            out_arr.append(right_arr[0])

    if(len(left_arr) == 0):
        for i in right_arr:
            out_arr.append(int(i))
    elif(len(right_arr) == 0):
        for i in left_arr:
            out_arr.append(int(i))

    # print(f"out arr {out_arr}")

    return out_arr

def mergeSort(orig_array, orig_size, sort_arr): 
    orig_size = int(orig_size)

    if orig_size > 1:    
        half1, half2 = makeSubArray(orig_array, orig_size)

        sort_arr = mergeSortedArrays(half1, half2, sort_arr)
    else:
        # Parse the array for output dictated by the assignment guidelines
        '''output = ""
        for x in orig_array:
            output += str(x) + " "
        print(output.rstrip())'''
        print(sort_arr)

    # Parse the array for output dictated by the assignment guidelines
    '''output = ""
    for x in orig_array:
        output += str(x) + " "
    print(output.rstrip())'''
    print(sort_arr)
    

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
    mergeSort(arrayInit, length, array3)

if __name__ == '__main__':
    main()
