def fibonacci(n,fib_arr,i):
    '''
    The nth fibonacci is in index n - 1
    :param n:
    :return:
    T(i) is the ith fibonacci number: T(0) = 0 and T(1) = 1
    T(i) = T(i-2) + T(i-1) if i >=2 else 0,1

    '''
    #fib_arr = [0, 1]
    i = 0
    if n is 1:
        return fib_arr[0]
    elif n is 2:
        return fib_arr[1]
    else:
        i = 2
        while i < n:
            fib_arr.append(fib_arr[i-2] + fib_arr[i-1])
            if i > 2:
                i += 1
            if i == (n-1):
                return fib_arr[n-1]

    return fib_arr[n-1]

if __name__=="__main__":
    print(fibonacci(20))