#https://stackoverflow.com/questions/7420193/how-to-find-upper-envelopes-of-intersected-lines-in-onlogn


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

def MinMax(array):
    max_line = array.pop()
    min_line = array.pop(0)
    return array, max_line, min_line




def main():
    n = 7
    arraya = [-3, -1, -.05, 0.5, 0.5, 0, 1]
    a1 = -3
    a2 = -1
    a3 = -0.5
    a4 = 0.5
    a5 = 0.5
    a6 = 0
    a7 = 1
    arrayb = [10, 8, -1, 1, -2, -5, -5]
    b1 = 10
    b2 = 8
    b3 = -1
    b4 = 1
    b5 = -2
    b6 = -5
    b7 = -5
    arraylines = [[-3,10], [-1,8], [-.05,-1], [0.5,1], [0.5,-2], [0,-5], [1,-5]]
    sortedByA = mergeSort(arraylines, n)
    print (sortedByA)
    array3, max_line, min_line = MinMax(sortedByA)
    print (array3, max_line, min_line)

    
if __name__ == '__main__':
    main() 
