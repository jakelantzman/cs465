import fileinput

def makePairs(arr, size):
    pairs = []
    pair_count = 0
    values =[]
    for i in range(0, size):
        for j in range(i + 1, size):  #changed 0 to 1
            pair = [arr[i], arr[j]]
            pairs.append(pair)

    for i in range (len(pairs)):
        if (pairs[i][0] > pairs[i][1]):
            pair = [pairs[i][0], pairs[i][1]]
            values.append(pair)
            pair_count += 1
    return pair_count


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
    array = [1, 5, -3, 4, -6, -2, 0, 3]
    length = 8

    mathces = makePairs(array, length)
    print(mathces)

    # output = ""
    # for x in array3:
    #     output += str(x) + " "
    # print(output.rstrip())

if __name__ == '__main__':
    main() 