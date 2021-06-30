class Solution:
    """
    def largestRectangle(self, heights) -> int:
        '''
        todo: time exceeded so need to store the prev_blk, its ht and num_blocks
         so if curr_ht <= prev_blk's ht can just do num_blks * curr_ht, compare and update max
        T(i,j) is largest rectangle for heights[j...i]

        Recurrence:
        T(i,j) = max(heights(i), for i = 0 to heights[i] * num_blocks
        before it at that height
        :param heights:
        :return:
        '''
        T = [0 for x in heights]
        # to save time at each bar record ht of largest rect,
        # num bars
        blk_info_d = {
            "rect_ht": [heights[0]],
            "num_bars": [1]
        }
        # prev_blk_ht = heights[0]
        # prev_blk_num_bars = 1
        # base case
        T[0] = heights[0]
        # iterate histogram bars
        for i in range(1, len(heights)):
            curr_ht = heights[i]
            # todo: check dict here to skip loop
            prev_rect_ht = blk_info_d["rect_ht"][-1]
            prev_rect_num_bars = blk_info_d["num_bars"][-1]

            # vars to be used at bottom
            best_rect_ht = 0
            best_num_bars = 0
            if curr_ht >= prev_rect_ht:
                # means can just add one bar of prev_rect_ht
                new_rect_area = (prev_rect_num_bars + 1) * \
                                    (prev_rect_ht)
                # in case of 1,2,3,4,5 need to update
                one_back_ht = heights[i-1]
                if curr_ht >= one_back_ht:
                    one_back_rect_area = 2 * (one_back_ht)

                if one_back_rect_area >= new_rect_area:
                    new_rect_area = one_back_rect_area
                    prev_rect_ht = one_back_ht
                    prev_rect_num_bars = 1

                if new_rect_area > curr_ht:
                    T[i] = new_rect_area
                    blk_info_d["rect_ht"].append(prev_rect_ht)
                    blk_info_d["num_bars"].append(prev_rect_num_bars+1)
                    continue

            # start at zero since don't know how high the rect is
            # going back
            prev_block_area = 0
            max_blk_area = curr_ht
            # iterate curr_ht down to 0 to find max block going back
            for k in range(curr_ht, -1, -1):
                # start with ht -> 0
                curr_blk_ht = k
                prev_block_area += curr_blk_ht
                count = 1
                while True:
                    prev_idx = i - count
                    if prev_idx < 0:
                        break
                    prev_ht = heights[prev_idx]
                    # prev_ht's min is curr_blk ht to be added
                    if prev_ht >= curr_blk_ht:
                        prev_block_area += curr_blk_ht
                    else:
                        break
                    count += 1
                if prev_block_area > max_blk_area:
                    max_blk_area = prev_block_area
                    # todo: update dict here
                    best_rect_ht = curr_blk_ht
                    best_num_bars = count #+ 1

                prev_block_area = 0

            T[i] = max(max_blk_area, curr_ht)
            if best_rect_ht==0 and best_num_bars==0:
                # means current bar > prev_rect_area
                blk_info_d["rect_ht"].append(curr_ht)
                blk_info_d["num_bars"].append(1)
            else:
                blk_info_d["rect_ht"].append(best_rect_ht)
                blk_info_d["num_bars"].append(best_num_bars)
        return max(T)
    """

    def largestRectangle_old(self, heights) -> int:
        '''
        todo: time exceeded so need table B[1...n] to track the highest
         continguous block ht for heights[1...i]

        T(i,j) is largest rectangle for heights[j...i]

        Recurrence:
        T(i,j) = max(heights(i), for i = 0 to heights[i] * num_blocks
        before it at that height
        :param heights:
        :return:
        '''
        # corner case all same
        if len(set(heights)) <= 1:
            return heights[0] * len(heights)

        T = [0 for x in heights]

        # base case
        # track max rectangle area
        T[0] = heights[0]


        # iterate histogram bars
        for i in range(1, len(heights)):
            curr_ht = heights[i]

            # start at zero since don't know how high the rect is
            # going back
            prev_block_area = 0
            max_blk_area = curr_ht
            # iterate curr_ht down to 0 to find max block going back
            for k in range(curr_ht, -1, -1):
                # start with ht -> 0
                curr_blk_ht = k
                prev_block_area += curr_blk_ht
                count = 1
                while True:
                    prev_idx = i - count
                    if prev_idx < 0:
                        break
                    prev_ht = heights[prev_idx]
                    # prev_ht's min is curr_blk ht to be added
                    if prev_ht >= curr_blk_ht:
                        prev_block_area += curr_blk_ht
                    else:
                        break
                    count += 1
                if prev_block_area > max_blk_area:
                    max_blk_area = prev_block_area

                prev_block_area = 0

            T[i] = max(max_blk_area, curr_ht)

        return max(T)

    def largestRectangle(self, heights) -> int:
        '''
        todo: time exceeded so need table B[1...n] to track the highest
         continguous block ht for heights[1...i]

        T(i,j) is largest rectangle for heights[j...i]

        Recurrence:
        T(i,j) = max(heights(i), for i = 0 to heights[i] * num_blocks
        before it at that height
        :param heights:
        :return:
        '''
        # corner case all same
        if len(set(heights)) <= 1:
            return heights[0] * len(heights)

        T = [0 for x in heights]
        # at each step track num blocks for which each ht can go back
        B = {}
        # base case
        # track max rectangle area
        T[0] = heights[0]
        # "first height extends for one block"
        # access dict and check if ht is existing in accessed previous key
        # if so can add 1 find rect area  if not, go lower in ht,
        # take max and compare to curr block ht
        B[0] = {i : 1 for i in range(heights[0]+1)}
        # set high of rect area to beat
        rect_area_hi = 0
        # iterate histogram bars
        for i in range(1, len(heights)):
            curr_ht = heights[i]
            rect_area_hi = curr_ht
            B[i] = {i: 1 for i in range(curr_ht + 1)}
            for ht, num_blks in B[i-1].items():
                if ht in B[i]:
                    B[i][ht] += num_blks
                    rect_area = B[i][ht] * ht
                    if rect_area > rect_area_hi:
                        rect_area_hi = rect_area
                # else means curr_bar lower than prev
            T[i] = rect_area_hi
        largest_rect = max(T)

        return largest_rect

    '''
    # iterate curr_ht down to 0 to find max block going back
    for k in range(curr_ht, -1, -1):
        # access ht second key from prev. idx first key
        if k in B[i - 1]:
            num_blks = B[i - 1][k]
            if k in B[i]:
                B[i][k] = num_blks+1
                rect_area = (num_blks + 1) * k
            else:
                B[i].update({k:num_blks+1})
                rect_area = (num_blks + 1) * k
            if rect_area > rect_area_hi:
                rect_area_hi = rect_area
        else:
            if k in B[i]:
                B[i][k] = 1
            else:
                B[i].update({k:1})
    T[i] = rect_area_hi
    '''

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

    #20
    heights = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    #print(sol.largestRectangle(heights))

    #9
    heights = [1,2,3,4,5]
    #print(sol.largestRectangle(heights))

    #3
    heights = [2,1,2]
    print(sol.largestRectangle(heights))

    # 2
    heights = [1, 1]
    print(sol.largestRectangle(heights))
    # 50000
    heights = [1 for x in range(50000)]
    print(sol.largestRectangle(heights))
    # 10
    heights = [2, 1, 5, 6, 2, 3]
    #print(sol.leftRightChecker(heights))
    print(sol.largestRectangle(heights))
    #4
    heights = [2,4]
    #print(sol.leftRightChecker(heights))
    print(sol.largestRectangle(heights))
    # 3
    heights = [2, 1, 2]
    #print(sol.leftRightChecker(heights))
    print(sol.largestRectangle(heights))


