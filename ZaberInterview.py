'''
pos 1: 0,1,2
pos 2: 0 to 9
pos 3: 0 to 5
pos 4: 0 to 9

{0,1,2} any position
{3,4,5} pos 2,3,4
{6,7,8,9} pos 2,4
Try putting digits in all positions and count valid times
h1h2 m1m2
arr = [A, B, C, D]
arr1 = [A, B, D, C]
arr3 = [A, C, B, D]
arr4 = [A, C, D, B]
arr5 = [A, D, B, C]
arr6 = [A, D, C, B]

arr7 = [B, A, C, D]
arr8 = [B, A, D, C]
arr9 = [B, C, A, D]
arr10 = [B, C, D, A]
arr11 = [B, D, A, C]
arr12 = [B, D, C, A]

arr13 = [C, A, B, D]
arr14 = [C, A, D, B]
arr15 = [C, B, A, D]
arr16 = [C, B, D, A]
arr17 = [C, D, A, B]
arr18 = [C, D, B, A]

arr19 = [D, A, B, C]
arr20 = [D, A, C, B]
arr21 = [D, B, A, C]
arr22 = [D, B, C, A]
arr23 = [D, C, A, B]
arr24 = [D, C, B, A]

big_arr = [arr, arr1, arr3, arr4, arr5, arr6, arr7,
           arr8, arr9, arr10, arr11, arr12, arr13, arr14, arr15,
           arr16, arr17, arr18, arr19, arr20, arr21, arr22, arr23, arr24]
'''
import random


def permute(arr, k=0):
    permuted_arr = []
    if k == len(arr):
        #print(arr)
        permuted_arr.append(arr)
    else:
        for i in range(k, len(arr)):
            arr[k], arr[i] = arr[i], arr[k]
            permute(arr, k+1)
            arr[k], arr[i] = arr[i], arr[k]
    return permuted_arr

def solution(A, B, C, D):
    # write your code in Python 3.6
    valid_times = []
    big_arr = permute([A,B,C,D])

    for i in range(len(big_arr)):
        curr = big_arr[i]
        # check if valid time
        h1 = curr[0]
        h2 = curr[1]
        m1 = curr[2]
        m2 = curr[3]

        hours = str(h1) + str(h2)
        hours_int = int(hours)
        minutes = str(m1) + str(m2)
        min_int = int(minutes)

        if hours_int < 24 and min_int < 60:
            valid_time = hours + minutes
            valid_times.append(valid_time)

    # count unique valid times
    valid_set = set(valid_times)
    valid_count = len(valid_set)

    return valid_set, valid_count


if __name__=="__main__":
    for i in range(100):
        A = random.randint(0, 9)
        B = random.randint(0, 9)
        C = random.randint(0, 9)
        D = random.randint(0, 9)
        valid_set, valid_count = solution(A,B,C,D)
        print(f'count: {valid_count}\nset: {valid_set}')
