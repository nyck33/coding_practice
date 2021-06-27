class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        LIS style
        if dict[s(i)]:
            update idx of dict
            seq_start = prev. idx of same letter
            seq_end = curr idx of repeated letter
            len of substr = seq_end - seq_start
            T(i) = len of substr

        s(i-1): T(i) = T(i-1) + 1
        else
        """
        # corner case
        if len(s) <= 0:
            return 0
        # row and col of zeros
        T = [0 for x in s]
        letters_d = {}

        # base case = 1
        T[0] = 1
        letters_d[s[0]] = 0

        for i in range(1, len(s)):
            curr_alpha = s[i]
            if curr_alpha in letters_d:
                # starts at next index can't include letter twice
                seq_start = letters_d[curr_alpha]
                # think of "abba"
                for alpha, idx in letters_d.items():
                    if idx < seq_start:
                        letters_d[alpha] = seq_start
                seq_len = i - seq_start
                T[i] = seq_len
                letters_d[curr_alpha] = i
            else:
                T[i] = T[i - 1] + 1
                letters_d[curr_alpha] = i

        return max(T)


if __name__ == "__main__":
    sol = Solution()

    s = "abcabcbb"
    s = "abba"

    print(sol.lengthOfLongestSubstring(s))


