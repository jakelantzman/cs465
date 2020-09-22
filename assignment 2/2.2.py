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

def get_top_intersection(l, top, lines):
    # Getting topmost intersection of line l with among all other lines
    max_y = -10000001
    right_line = lines[0]
    for line in lines:
        if l == line:
            continue
        if l[0] == line[0]:
            continue
        y = (l[0]*line[1] - l[1]*line[0]) / (l[0] - line[0])
        if y >= top:
            continue
        if y > max_y:
            max_y = y
            right_line = line
    return right_line, max_y


def get_bottom_intersection(l, bottom, lines):
    # Getting bottommost intersection of line l with among all other lines
    min_y = 10000001
    min_line = lines[0]
    for line in lines:
        if l == line:
            continue
        if l[0] == line[0]:
            continue
        y = (l[0]*line[1] - l[1]*line[0]) / (l[0] - line[0])
        if y <= bottom:
            continue
        if y < min_y:
            min_y = y
            min_line = line
    return min_line, min_y


def get_top_lines(left_line, right_line, min_top, max_top, lines):
    left_top, y1 = get_top_intersection(left_line, min_top, lines)
    right_top, y2 = get_top_intersection(right_line, max_top, lines)
    return left_top, y1, right_top, y2


def get_bottom_lines(left_line, right_line, min_top, max_top, lines):
    left_bottom, y1 = get_bottom_intersection(left_line, min_top, lines)
    right_bottom, y2 = get_bottom_intersection(right_line, max_top, lines)
    return left_bottom, y1, right_bottom, y2


def main():


    #---------------------------------------------------
    # this is where to put the input, 
    # and call it this
    #  \/ 
    #  \/
    inputlines = [[-3.4,-2.15], [3.74,-7.94], [-1.94,-1.82], [0.82,2.16], [0.43,-9.54], [0.62,7.27], [1.06,-6.12], [-4.99,3.86], [-0.22,0.66], [-3.55,6.51]]
    #sorts the lines by their a values from least to greatest 
    sortedByA = mergeSort(inputlines, len(inputlines))
    lines = sortedByA

    right_line = lines[-1]
    left_line = lines[0]

    # gets number of upper envelops
    no = 2
    upper_ctr = 2
    min_top = 10000001
    max_top = 10000001
    while True:
        new_left_line, min_top, new_right_line, max_top = get_top_lines(left_line, right_line, min_top, max_top, lines)
        if left_line == right_line:
            upper_ctr += 1
            break
        elif new_left_line == right_line and new_right_line == left_line:
            break
        else:
            upper_ctr += 2
        left_line = new_left_line
        right_line = new_right_line


    # gets number of lower envelops
    right_line = lines[0]
    left_line = lines[-1]
    no = 2
    lower_ctr = 2
    min_top = -10000001
    max_top = -10000001
    while True:
        new_left_line, min_top, new_right_line, max_top = get_bottom_lines(left_line, right_line, min_top, max_top, lines)
        if new_left_line == new_right_line:
            lower_ctr += 1
            break
        elif new_left_line == right_line and new_right_line == left_line:
            break
        else:
            lower_ctr += 2
        left_line = new_left_line
        right_line = new_right_line


    print(upper_ctr, lower_ctr)

if __name__ == '__main__':
    main() 