class Solution:
    def largestRectangleArea(self, heights) -> int:
        '''
        dp:
        Track height of block rectangle, how many bars it spans and value
        T(i) is the area of the largest rectangle for bars from 0...i
        Recurrence:
        T(i) = height if:
            height >= consecutive bars rectangle
            and height >= rectangle made with just the i-1 st bar (sudden changes)


        '''
        T = {"block_ht": [], "num_bars": [], "block_val": []}
        # base case
        T["block_ht"].append(heights[0])
        T["num_bars"].append(1)
        T["block_val"].append(heights[0])

        for i in range(1, len(heights)):
            ht = heights[i]
            # block with i-1
            prev_ht = heights[i-1]
            two_blk_area = min(ht,prev_ht) * 2
            # continuous block
            block_hts_arr = T["block_ht"]
            num_bars_arr = T["num_bars"]
            block_val_arr = T["block_val"]
            block_ht = block_hts_arr[-1]
            num_bars = num_bars_arr[-1]
            block_val = block_val_arr[-1]
            block_ht = min(ht,block_ht)


    def leftRightChecker(self, heights) -> int:
        n = len(heights)
        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            j = i - 1
            while j >= 0 and heights[j] >= heights[i]:
                j -= left[j]
            left[i] = i - j

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < len(heights) and heights[i] <= heights[j]:
                j += right[j]
            right[i] = j - i

        res = 0
        for i in range(n):
            res = max(res, heights[i] * (left[i] + right[i] - 1))

        return res


if __name__=="__main__":
    sol = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    print(sol.leftRightChecker(heights))