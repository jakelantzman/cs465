import fileinput
# The mergeSortedArrays function will take in two arrays that are already sorted and produce an array that is the sorted, merged
# result of the two sorted arrays
def mergeSort(arrayInit, length, array3): 
    # Convert each item in the array to an integer
    arrayInit = map(int, arrayInit)
    length = int(length)

    if length > 0:
        midpoint = length // 2
        leftArray = arrayInit[:midpoint+1]
        rightArray = arrayInit[midpoint+1:]
        print("Left Array: {}".format(leftArray))
        print("Right Array: {}".format(rightArray))
        i = j = 0
        while i < len(leftArray) and j < len(rightArray):
            mergeSort(leftArray, len(leftArray), array3)
            mergeSort(rightArray, len(rightArray), array3)

            if(leftArray[i] < rightArray[j]):
                array3.append(leftArray[i])
                i += 1
                print(array3)

            elif(leftArray[i] > rightArray[j]):
                array3.append(rightArray[j])
                j += 1
                print(array3)

            elif(leftArray[i] == rightArray[j]):
                array3.append(leftArray[i])
                array3.append(rightArray[j])
                i += 1
                j += 1
                print(array3)

    # Parse the array for output dictated by the assignment guidelines
    # output = ""
    # for x in array3:
    #     output += str(x) + " "
    # print(output.rstrip())

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