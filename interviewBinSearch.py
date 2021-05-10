'''
            elif len(sub) <= 2:
                # in btwn 2 elements
                if target > sub[mid] and target < sub[mid+1]:
                    return nums.index(nums[mid]) + 1
                #if less than left
                elif target < sub[mid]:
                    return nums.index(nums[mid]) - 1
                # if > right:
                else:
                    return nums.index(nums[mid+1]) + 1
'''
class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        '''
        binary search

        '''
        left = 0
        #0 indexing so len - 1
        right = len(nums)-1
        mid = self.find_mid(nums, right)
        sub = nums

        while True:
            if len(sub) <=1:
                if target > sub[mid]:
                    return nums.index(sub[mid]) + 1
                elif target < sub[mid]:
                    return nums.index(sub[mid])
                elif target == sub[mid]:
                    return nums.index(target)

            elif target == sub[mid]:
                return nums.index(target)

            elif target > sub[mid]:
                left = mid
                sub = sub[left:]
                mid = self.find_mid(sub, right)

            elif target < sub[mid]:
                right = mid
                # since mid != target, can remove
                sub = sub[left:right]
                mid = self.find_mid(sub, right)

    def find_mid(self, sub, right):
        #len is even, 4 -> 2 which is 1st of right subarray
        if len(sub) <= 1:
            return 0
        elif len(sub) % 2 == 0:
            return (len(sub) // 2)
        else:
            # odd len, ceil to give first of right subarray
            return (len(sub) // 2) + 1


if __name__=="__main__":
    sol = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    # 2
    print(sol.searchInsert(nums, target))

    nums = [1, 3, 5, 6]
    target = 2
    # 1
    print(sol.searchInsert(nums, target))

    nums = [1, 3, 5, 6]
    target = 7
    # 4
    print(sol.searchInsert(nums, target))

    nums = [1, 3, 5, 6]
    target = 0
    # 0
    print(sol.searchInsert(nums, target))

    nums = [1]
    target = 0
    # 0
    print(sol.searchInsert(nums, target))