'''
1	1	1	1	 1  1  1
1	2	3	4	 5	6  7
1	3	6  10	15 21 28	

T(i) = num 1's - num 0's from nums(1...i)
C(i) = num since prev idx where T(i) was the same

Recurrence:
T(0) = 0
For 1 <= 1 <=n
T(i) = T(i-1) + 1 if nums(i) = 1
T(i) =  T(i-1) -1 otherwise

C(1) = 0

For 1<= j <= n
For 1 <= k <= j-1
C(j) = (j-k) + C(k) if T(k) == T(j)

return max(C)


'''
class Solution3:
    def findMaxLength(self, nums):
        count = 0
        longest_seq = 0
        table = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1

            #each plus/minus is entered into table{} on first
            #appearance, all other lookups only calculate the len
            # from say -2 to -2 to update the longest seq.
            if count in table:
                longest_seq = max(longest_seq, index - table[count])
            else:
                table[count] = index

        return longest_seq


class Solution2:
    def findMaxLength(self, nums: list) -> int:
        '''
        T(i) = num 1's - num 0's from nums(1...i)
        C(i) = num since prev idx where T(i) was the same

        Recurrence:
        T(0) = 0
        For 1 <= 1 <=n
        T(i) = T(i-1) + 1 if nums(i) = 1
        T(i) =  T(i-1) -1 otherwise

        C(1) = 0

        For 1<= j <= n
        For 1 <= k <= j-1
        C(j) = (j-k) + C(k) if T(k) == T(j)

        return max(C)
        :param nums:
        :return:
        '''
        # one longer for base case
        T = [0 for x in range(len(nums)+1)]
        T[0] = 0 # base case
        nums = [0] + nums # needs 0 to match len of T
        for i in range(1, len(nums)):  #O(n)
            if nums[i] == 1:
                T[i] = T[i-1] + 1
            else:
                T[i] = T[i-1] - 1

        C = [0 for x in T]
        C[0] = 0
        for j in range(1, len(T)): #O(n)
            for k in range(j-1, -1, -1): #O(n)
                if T[k] == T[j]:
                    C[j] = (j-k) + C[k]
                    # find the nearest same and break
                    break
                else:
                    C[j] = 0

        return max(C)

class Solution:
    def findMaxLength(self, nums: list) -> int:
        '''
        T(i,j) is the max len of continu subarray for nums(i...j) with equal 0's and 1's
        Shift window, start diagonals as 0 and get to top right

        Recurrence Relation:
        Base Case of T(1) = 0  since either 0 or 1 cannot have equal 0's and 1's
        For w = 1 to n-1:
        For i = 1 to n-w:
        Let j = i+1
        T(i,j) = 0
        T(i,j) = T(i-1,j-1) + 2 if nums(i) != nums(j)
        T(i,j) = max{T(i+1,j), T(i,j-1)} otherwise
        '''
        T = [[0 for x in range(len(nums))] for y in range(len(nums))]
        n = len(nums)
        print(f'len:{n}')
        # window size start at width 1 to n-1
        for w in range(1, n):
            #start top row so 0 to second to last row
            for i in range(0, n - w):
                # j starts at 1, goes to last col
                j = i + w
                if nums[i] != nums[j]:
                    # from diag down left
                    T[i][j] = T[i + 1][j - 1] + 2
                else:
                    T[i][j] = max(T[i + 1][j], T[i][j - 1])

        for line in T:
            print(line)
        return T[0][n - 1]


    def counter(self,nums):
        '''
        keep a zero, one counter, whenever they equal, fill with new val
        else take T[i-1
        :param nums:
        :return:
        '''
        zeros = [0 for x in nums]
        ones = [0 for x in nums]
        T = [0 for x in nums]
        T[0] = 0
        for i in range(len(nums)):
            if i ==0:
                if nums[i] == 1:
                    ones[i] = 1
                else:
                    zeros[i] = 1
                T[i] = 0
                continue

            if nums[i] == 1:
                ones[i] = ones[i-1] + 1
                zeros[i] = zeros[i-1]
            else:
                zeros[i] = zeros[i-1] + 1
                ones[i] = ones[i-1]

            if ones[i] == zeros[i]:
                T[i] = ones[i] + zeros[i]
            else:
                T[i] = T[i-1]

        return max(T)


    def lis(self, nums):
        '''
        T(i) is max len of continu subarray to nums(i):
        T(1) = 0 since 0 or 1
        T(i) = T(i-1) +2 if nums(i-1) = nums(i)
        :param nums:
        :return:
        '''
        T = [0 for x in nums]
        T[0] = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                T[i] = T[i-1] + 2
            else:
                T[i] = T[i-1]

        return T[-1]


if __name__=="__main__":
    sol = Solution3()
    nums = [1]
    print(sol.findMaxLength(nums))
    #0
    nums = [0, 1]
    print(sol.findMaxLength(nums))
    #2
    nums = [0, 1, 0]
    print(sol.findMaxLength(nums))
    #2
    nums = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
    print(sol.findMaxLength(nums))
    #20
    nums = [1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,1,1,
            1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,
            0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,1,0,
            0,0,1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,1,0,
            0,1,0,1,1,1,0,0,1,0,1,1]

    print(sol.findMaxLength(nums))
    #print(sol.lis(nums))
    #print(sol.counter(nums))
    #94