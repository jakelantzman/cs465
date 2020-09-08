# import fileinput
# The mergeSortedArrays function will take in two arrays that are already sorted and produce an array that is the sorted, merged
# result of the two sorted arrays
def mergeSort(arrayInit, length): 
    # Convert each item in the array to an integer
    #arrayInit = map(int, arrayInit)
    
    length = int(length)

    if length > 1:
        
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

        mergeSort(leftArray, len(leftArray))
        mergeSort(rightArray, len(rightArray))
        
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

        while j < len(rightArray):
            arrayInit[k] = rightArray[j]
            j += 1
            k += 1
    return arrayInit
# Main function to drive the code and take inputs
def main():
   # hold = []
  #  test = ""
 #   length = ""
 #   array3 = []
#    for line in fileinput.input():
#        test += line
#    hold = test.split('\n')
#    length = hold.pop(0)
#    arrayInit = hold[0].split()
    input = [-4,3,1,-6,7]
    size = 5

    array3 = mergeSort(input, size)
    output = ""
    for x in array3:
        output += str(x) + " "
    print(output.rstrip())

if __name__ == '__main__':
    main() 