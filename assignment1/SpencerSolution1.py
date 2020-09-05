import fileinput
# The mergeSortedArrays function will take in two arrays that are already sorted and produce an array that is the sorted, merged
# result of the two sorted arrays
def mergeSort(arrayInit, length): 
    # Convert each item in the array to an integer
    arrayInit = map(int, arrayInit)
    length = int(length)

    if length > 1:
        midpoint = length // 2
        leftArray = arrayInit[:midpoint]
        rightArray = arrayInit[midpoint:]

        mergeSort(leftArray, len(leftArray))
        mergeSort(RightArray, len(rightArray))
        
        i = j = k = 0
        while i < len(leftArray) and j < len(rightArray):

            if(leftArray[i] < rightArray[j]):
                arrayInit[k] = leftArray[i]
                i += 1
            else:
                arrayInit[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            arrayInit[k] = leftArray[i]
            i += 1 
            k += 1

        while j < len(right):
            arrayInit[k] = right[j]
            j += 1
            k += 1

# Main function to drive the code and take inputs
def main():
    hold = []
    test = ""
    length = ""
    arrayInit = []
    for line in fileinput.input():
        test += line
    hold = test.split('\n')
    length = hold.pop(0)
    arrayInit = hold[0].split()
    mergeSort(arrayInit, length)

if __name__ == '__main__':
    main() 