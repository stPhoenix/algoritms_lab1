from random import randint
import time


def time_decorator(func):
    def wrapper(x, array):
        t1 = time.time()
        func(x, array)
        t2 = time.time()
        print("Time: %f"%(t2-t1))
    return wrapper

def generate_array(n):
    return [x for x in range(n)]

@time_decorator
def linear_search(x, array):
    for i in array:
        if i == x:
            return 1
    
    return -1

@time_decorator
def binary_search(x, array):
    low = 0
    high = len(array) - 1
    mid = 0

    while low <= high:
        mid = int((low+high)/2)
        if(x<array[mid]):
            high = mid - 1
        elif x>array[mid]:
            low = mid + 1
        else:
            return 1
    
    return -1




if __name__ == "__main__":
    testA = generate_array(30000000)
    print("TestA numbers generated")
   

    findA = testA[randint(0, len(testA)-1000)]


    print("Search for %s in array A of %s lenght"%(findA, len(testA)))
    print("Linear:")
    linear_search(findA, testA)

    print("Binary:")
    binary_search(findA, testA)

    del testA, findA

    testB = generate_array(300000000)
    findB = testB[randint(0, len(testB)-1000)]

    print("TestB numbers generated")

    print("Search for %s in array B of %s lenght"%(findB, len(testB)))
    print("Linear:")
    linear_search(findB, testB)

    print("Binary:")
    binary_search(findB, testB)

    del testB, findB