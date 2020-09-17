
def Check(arr, bot, top, x):
    if (top >= bot):
        mid = bot + (top - bot)//2
        if (x==arr[mid]):
            return mid
        elif (x > arr[mid]):
            return Check(arr, (mid + 1), top, x)
        else:
            return Check(arr, bot, (mid - 1), x)
    return -1

def Count(arr, n):
    counter = 0
    arr.sort()
    
    for i in range (0, n - 2):
        if (Check(arr, i + 1, n - 1, arr[i]) != -1):
            count += 1
    return counter


def main():
    # do whatever to make n = first line
    # do whatever to turn that second line into an array
    # so this is just skipping that for now, this is input 1
    n = 5
    Array1 = [2, 4, 1, 3, 5]

    output = Count(Array1, n)
    print(output)