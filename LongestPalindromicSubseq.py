def longestPalindrome(s: str) -> str:
    """
    reverse string to make R

    """
    r = ""
    for x in s[::-1]:
        r += x

    # keep track of len of longest
    len_long = 0
    # list of palindromes or maybe just one string
    palindrome = ""

    # matrix, rows = rev, cols = str
    mat = [[0 for j in range(len(s) + 1)] for i in range(len(r)+1)]
    #fill top row and left col with 0's
    for j in range(len(s)+1):
        mat[0][j] = 0
    for i in range(len(r)+1):
        mat[i][0] = 0

    for i in range(1, len(r)+1, 1):
        for j in range(1,len(s)+1, 1):
            if r[i-1] == s[j-1]:
                mat[i][j] = mat[i - 1][j - 1] + 1
            else: #todo: change how table filled for string not subsequence
                #mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])
                mat[i][j] = 0

    # search the last row for consecutive nums from 1...m
    # find max in last row to find length of longest palindrome
    high = 0
    for m in range(1, len(s)+1, 1):
        if mat[-1][m] > high:
            high = mat[-1][m]

    curr_count = 1
    for k in range(1, len(s)+1, 1):
        if mat[-1][k] == curr_count:
            palindrome += s[k-1]
            curr_count += 1 #look for letter 2 now
            if curr_count > high:
                break
        elif mat[-1][k] == curr_count-1: #repeated
            palindrome = ""
            palindrome += s[k-1]
        elif mat[-1][k] == curr_count and curr_count == high:
            break
        else:
            palindrome = ""
            curr_count = 1

    #print(long_rev, long_str)

    return palindrome


if __name__ == "__main__":
    s1 = "babad"
    s2 = "cbbd"
    s3 = "a"
    s4 = "ac"
    s5 = "aacabdkacaa" # want "aca" got "kacaa"
    #inputs = [s1, s2, s3, s4]
    inputs = [s5]
    for s in inputs:
        print(longestPalindrome(s))
