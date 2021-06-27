'''
yuckdonalds([1,2,3,4,5,6], [5,5,5,5,5,5], 5
T = [0,
want 1 and 6 open


'''

def yuckdonalds(m, p, k):
    # Start from 0 for convenience
    # is the maximum profit at each location, initialize to be the profit at each location
    T = [ 0 for p_ in p ]
    for i in range(len(m)):
        T[i] = p[i]
        for j in range(i-1): #todo, this should be i
            #print(f"j:{j}")
            if (m[i] - m[j]) >= k:
                T[i] = max(T[i], p[i] + T[j])

        # Final maximum profit is the maximum when there is a restaurant at i and maximum profit
        # when there is no restaurant at position i, given recursively by T[i-1]
        #print("")
        T[i] = max(T[i], T[i-1])

    return T[len(m)-1]


def find_total_profit(locations, profits, k=5):
    '''

    :param locations: must be k miles apart
    :param profits: from each location
    :return: total profit

    '''
    # need one more idx for idx 0
    T = [0 for x in locations]

    for i in range(len(locations)):
        # initialize to profit at i
        T[i] = profits[i]
        #iterate fwd to find max with restaurant at i
        for j in range(i-1, -1, -1):
        #for j in range(i-1):
            #print(f'j:{j}')
            if (locations[i] - locations[j]) >= k:
                # T[i] is updated >= 1 times? or none
                # max of having a restaurant at i
                T[i] = max(T[i], profits[i] + T[j])
        # now see if having no restaurant at i is better
        #print("")
        T[i] = max(T[i], T[i-1])

    return T[-1]

def cum_best(miles, p, k):
    pass

if __name__=="__main__":
    locations =[1,2,3,4,5,6]
    profits = [5,5,5,5,5,5]
    k = 5
    print(find_total_profit(locations, profits, k))

    m = [ 0, 5, 6, 11, 14, 20, 22, 28 ]
    p = [ 30, 10, 40, 1, 15, 5, 23, 17 ]
    k = 5
    print(find_total_profit(m,p,k))
    #print('m=%s p=%s k=%s' % (m, p, k))

    p_ = yuckdonalds(m, p, k)
    print('Maximum total profit = %d' % p_)

    m = [ 1, 10, 16, 21, 22, 35, 38 ]
    p = [ 30, 9, 13, 25, 23, 3, 10 ]
    k = 10
    print(find_total_profit(m,p,k))

    #print('m=%s p=%s k=%s' % (m, p, k))
    p_ = yuckdonalds(m, p, k)
    print('Maximum total profit = %d' % p_)

    # Greedy approach (which assumes a restaurant at location i) will fail this case (correct
    # answer is 400)
    m = [ 10, 20, 25, 30, 40 ];
    p = [ 100, 100, 101, 100, 100 ];
    k = 10;
    print(find_total_profit(m,p,k))

    #print('m=%s p=%s k=%s' % (m, p, k))
    p_ = yuckdonalds(m, p, k)
    print('Maximum total profit = %d' % p_)

    # Corner case, the return should be 42 and not 41
    m = [ 0, 4, 8 ];
    p = [ 10, 42, 31 ];
    k = 5;
    print(find_total_profit(m,p,k))

    #print('m=%s p=%s k=%s' % (m, p, k))
    p_ = yuckdonalds(m, p, k)
    print('Maximum total profit = %d' % p_)

    m =[0, 5, 10, 15, 20]
    p = [5,5,5,5,5]
    k=5
    print(find_total_profit(m,p,k))
    p_ = yuckdonalds(m, p, k)
    print('Maximum total profit = %d' % p_)

