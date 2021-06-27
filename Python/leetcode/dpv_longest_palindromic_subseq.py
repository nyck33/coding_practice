
def longest(the_str):
    '''

    :param the_str:
    :return: length of longest palindromic subseq
    and the subseq from s(i..j)
    '''
    length = len(the_str)
    T = [[0 for x in range(length)] for y in range(length)]
    #subseq of 1 is a palindrome
    for i in range(length):
        T[i][i] = 1
    # shift window from size 2 to len of string
    strings = []
    for w in range(1, length):
        for i in range(length-w):
            j = i + w
            if the_str[i] == the_str[j]:
                T[i][j] = T[i+1][j-1] + 2
                strings.append(the_str[i:j+1])
            else:
                T[i][j] = max(T[i+1][j], T[i][j-1])

    # find the longest string
    longest = longest_str(strings)

    return T[0][length-1], longest

def longest_str(strings):
    longest = strings[0]
    len_longest = len(longest)

    for i in range(len(strings)):
        if len(strings[i]) > len_longest:
            longest = strings[i]
    return longest

if __name__=="__main__":
    the_str = 'abcbaf'
    length, chars = longest(the_str)
    print(f'len: {length}, chars: {chars}')
    the_str = 'abb'
    length, chars = longest(the_str)
    print(f'len: {length}, chars: {chars}')

