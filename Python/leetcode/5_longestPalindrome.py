class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        T(i,j) is the length of longest palindromic subsequence from S(i) to S(j)
        T(i,j) = T(i+1, j-1) + 2 if S(i) == S(j)
        else
        substring T(i,j) = 0
        subsequence:
        T(i,j) = max{T(i,j-1), T(i+1,j)}
        """
        n = len(s)
        # make grid n * n
        T = [[0 for x in range(n)] for i in range(n)]

        # fill diagonals with 1 for the substring of len 1
        for i in range(n):
            for j in range(n):
                if i == j:
                    T[i][j] = 1

        # iterate diagonals of T where j = i+1
        rows, cols = n, n
        col_num = 0
        col_start = 1
        while True:
            col_num = col_start  # start at T[0,1]
            for i in range(rows):
                if s[i] == s[col_num]:
                    T[i][col_num] = T[i + 1][col_num - 1] + 2
                else:
                    T[i][col_num] = 0
                col_num += 1
            col_start += 1
            if col_start >= n:
                break

        return T[n][n]


