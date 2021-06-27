import random
import sys
import os


def get_nth(n, arr):
    return arr[n-1]

def fib(n):
    arr = [0 for x in range(n)]
    arr[0] = 1
    arr[1] = 1
    for i in range(2,n):
        new = arr[i-2] + arr[i-1]
        arr[i] = new

    return arr[-1]

if __name__=="__main__":
    arr =[i for i in range(1,101)]
    n = 8
    num = fib(8)
    print(num)