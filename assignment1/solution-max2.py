import fileinput
# The mergeSortedArrays function will take in two arrays that are already sorted and produce an array that is the sorted, merged
# result of the two sorted arrays

def makeSubArray(arrayInit, length):
    #arrayInit = list(map(int, arrayInit))
    arrayInit = [int(i) for i in arrayInit]
    #length = int(length)
    if length > 1:
        midpoint = length // 2
        leftArray = arrayInit[:midpoint+1]
        rightArray = arrayInit[midpoint+1:]
    #print(f"left arr {leftArray}, right arr {rightArray}")

    # print(f"midpoint {midpoint}")
    # print(f"left arr {leftArray}")
    # print(f"right arr {rightArray}")

        
    else:
        leftArray = arrayInit[0]
        rightArray = []
    return leftArray, rightArray

def mergeSortedArrays(left_arr, right_arr, out_arr): 

    # Convert each item in the array to an integer
    #array1 = list(map(int, left_arr))
    #array2 = list(map(int, right_arr))
    array1 = [int(i) for i in left_arr]
    array2 = [int(i) for i in right_arr]


    i = 0
    j = 0
    # Loop through each array and evaluate at each index which integer to insert into the output array,
    # if the length of either array becomes zero throughout the loop, append all remaining integers from
    # the other array to the output array
    while len(array1) > i and len(array2) > j:
        if(array1[i] < array2[j]):
            out_arr.append(array1[i])
            i += 1
            print(f"if 1 arr1 {array1}, arr2 {array2}, out {out_arr}")
        elif(array1[i] > array2[j]):
            out_arr.append(array2[j])
            j += 1
            print(f"if 2 arr1 {array1}, arr2 {array2}, out {out_arr}")
        elif(array1[i] == array2[j]):
            out_arr.append(array1[i])
            out_arr.append(array2[j])
            i += 1
            j += 1
            print(f"if 3 arr1 {array1}, arr2 {array2}, out {out_arr}")

    if(len(array1) == 0):
        for i in array2:
            out_arr.append(int(i))
    elif(len(array2) == 0):
        for i in array1:
            out_arr.append(int(i))

    # print(f"out arr {out_arr}")

    return out_arr

def mergeSort(orig_array, orig_size, sort_arr): 
    orig_size = int(orig_size)

    if orig_size > 1:    
        half1, half2 = makeSubArray(orig_array, orig_size)
        half1 = mergeSort(half1, len(half1), sort_arr)
        half2 = mergeSort(half2, len(half2), sort_arr)

        sort_arr = mergeSortedArrays(half1, half2, sort_arr)
    else:
        # Parse the array for output dictated by the assignment guidelines
        output = ""
        for x in sort_arr:
            output += str(x) + " "
        print(output.rstrip())


        #print(sort_arr)

    # Parse the array for output dictated by the assignment guidelines
    output = ""
    for x in sort_arr:
        output += str(x) + " "
    print(output.rstrip())


    #print(sort_arr)
    

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