'''
Team Members: Jacob Lantzman, Spencer Leahy, Maxwell Molden
'''

import fileinput

def makePairs(arr, size):
    pairs = []
    pair_count = 0
    for i in range(0, size):
        for j in range(0, size):
            pair = (arr[i], arr[j])
            pairs.append(pair)
    
    for i in range(0, size):
        for j in range(0, size):
            if (i < j) and (pairs[i] > pairs[j]):
                pair_count += 1
    return pair_count



    # match_count = 0
    # for i in range(0, size):
    #     for j in range(0, size):
    #         if (i < j) and (arr[i] > arr[j]):
    #             match_count += 1

    # return match_count


def main():
    # do whatever to make n = first line
    # do whatever to turn that second line into an array
    # so this is just skipping that for now, this is input 1

    # hold = []
    # test = ""
    # for line in fileinput.input():
    #     test += line
    # hold = test.split("\n")
    # length = hold[0].split()
    # array = hold[1].split()
    array = [2, 3, 1, 4, 5]
    length = 5

    mathces = makePairs(array, length)
    print(mathces)

    # output = ""
    # for x in array3:
    #     output += str(x) + " "
    # print(output.rstrip())

if __name__ == '__main__':
    main() 
