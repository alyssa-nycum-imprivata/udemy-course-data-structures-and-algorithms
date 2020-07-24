import collections

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]

def finder(arr1,arr2):

    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return print(num1)

    return print("Arr2 isn't missing a number")


finder(arr1,arr2)


def finder2(arr1,arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return print(num)
        else:
            d[num] -= 1

finder2(arr1,arr2)


def finder3(arr1,arr2):

    arr1_sum = 0
    arr2_sum = 0

    for num in arr1:
        arr1_sum += num
    
    for num in arr2:
        arr2_sum += num

    missing_number = arr1_sum - arr2_sum

    print(missing_number)

finder3(arr1,arr2)


def finder4(arr1,arr2):
    result = 0

    for num in arr1+arr2:
        result^=num
        print(result)

    return print("FINAL", result)

finder4(arr1,arr2)
