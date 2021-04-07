class Solution:
    def maxPoints(self, points):
        '''
        for pts[1...n]
        start at pt 1 then work out slopes to n
        next iter pt 2, start at pt 2 and work out slopes to n
        since pt 1 -> pt 2 was already considered
        pt 3 start at pt 3
        todo: not accounting for slope 0 lines parallel to each other
        (1,0), (3,0), (5,0): -2/0 #0 denom means horizontal -> 0
        (1,1)(3,1)(5,1): -2/0
        todo: account for vertical lines  parallel to each other
        (1,0), (1,3), (1,5): 0/-2 0 numer means vertical -> -1
        todo: account for parallel lines diagonal (same slope)
        this should be ok
        '''
        highest = float('-inf')

        slopes = []
        for i in range(len(points)):
            if i == len(points)-1:
                break
            start_pt = points[i]
            start_x = start_pt[0]
            start_y = start_pt[1]
            curr_slopes = []
            for j in range(i + 1, len(points)):
                dst_pt = points[j]
                dst_x = dst_pt[0]
                dst_y = dst_pt[1]
                slope = (dst_x - start_x) / (dst_y - start_y)
                curr_slopes.append(slope)
            slopes.append(curr_slopes)
        # count same slopes in each subarray for start pt i
        # counts = {}
        for k in range(len(slopes)):
            curr_slopes = slopes[k]
            counts = {}
            for m in range(len(curr_slopes)):
                slope = curr_slopes[m]
                if slope in counts:
                    counts[slope] += 1
                else:
                    counts[slope] = 1
            high = max(counts.values())
            if high > highest:
                highest = high

        return highest+1


if __name__=="__main__":
    sol = Solution()
    points = [[1, 1], [2, 2], [3, 3]]
    print(sol.maxPoints(points))
    #Output: 3

