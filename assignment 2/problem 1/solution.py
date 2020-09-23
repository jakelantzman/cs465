'''
Team Members: Jacob Lantzman, Spencer Leahy, Maxwell Molden
'''

import fileinput
import itertools

def makePairs(arr, size):
    pairs = [(arr[j], arr[i]) for j in range(size) for i in range(size)]
    count = [(arr[j], arr[i]) for j in range(size) for i in range(size) if (i < j) and (pairs[i] > pairs[j])]

    return len(count)

def main():
    # do whatever to make n = first line
    # do whatever to turn that second line into an array
    # so this is just skipping that for now, this is input 1

    hold = []
    test = ""
    for line in fileinput.input():
        test += line
    hold = test.split("\n")
    length = hold[0].split()
    array = hold[1].split()
    length = int(length[0])
    array = list(map(int, array))

    matches = makePairs(array, length)
    print(matches)

if __name__ == '__main__':
    main()