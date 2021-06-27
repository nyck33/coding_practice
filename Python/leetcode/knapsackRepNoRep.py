
def repetition(values, weights, capacity):
    #make table
    values = [0] + values
    weights = [0] + weights
    T = [[0 for x in range(capacity+1)] for y in range(len(weights))]

    for i in range(1, len(weights)):
        for w in range(1, capacity+1):
            if w >= weights[i]:
                T[i][w] = max(T[i-1][w], T[i][w-weights[i]] + values[i])
            else:
                T[i][w] = T[i-1][w]

    return T[len(values)-1][capacity]

if __name__=="__main__":
    values = [5, 7]
    weights = [3, 4]
    W = 10
    print(repetition(values, weights, W))
