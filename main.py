def sum1(n):
    final_sum = 0

    for x in range(n+1):
        final_sum += x

    return final_sum

# print(sum1(10))

def sum2(n):
    return (n*(n+1))/2

# print(sum2(10))

# O(1) Constant

def func_constant(values):
    print(values[0])

ex_list = [1, 2, 3]
# func_constant(ex_list)

# regardless the of list size, you will always get the same single answer

# O(n) Linear

def func_lin(ex_list):

    for val in ex_list:
        print(val)

# func_lin(ex_list)

# the number of values returned will scale linearly with n

# O(n^2) Quadratic

def func_quad(ex_list):
    for item_1 in ex_list:
        for item_2 in ex_list:
            print(item_1, item_2)

func_quad(ex_list)

# for a list of n items, we will perform n operations for every item in that list for a total of n * n actions

