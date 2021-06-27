class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [f'{i}' for i in range(1, n + 1)]
        print(arr)
        # calc which group. there are n groups with (n-1)! members
        num_members = 1
        for i in range(1,n):
            num_members *= i

        # skip this many groups
        # looking for the (group_num + member_num) th
        skip_before = k // num_members
        kth = k % num_members
        if kth == 0:
            #last member of last skip_before grp
            skip_before -= 1
        # skip groups after group_num +1st group
        skip_after = skip_before +2
        # skip this many members
        member_num = 0
        if k % num_members == 0:
            member_num = num_members -1
        else:
            member_num = (k % num_members) -1

        res_perms = self.permute(arr, skip_before, skip_after)
        #print(f'len: {len(res_perms)}\n{res_perms}')
        #return res_perms[k-1]
        return res_perms[member_num]

    def permute(self, arr, skip_before=None, skip_after=None):
        out = []
        if len(arr) == 1:
            return arr
        else:
            for i, let in enumerate(arr):
                if skip_before is not None and skip_after is not None:
                    if int(let) <= skip_before or int(let) >= skip_after:
                        continue
                for perm in self.permute(arr[:i] + arr[i + 1:]):
                    temp = [let + perm]
                    out += temp

        return out

if __name__=="__main__":
    sol = Solution()
    n=3
    k=3
    #213
    #print(sol.getPermutation(n,k))
    n=6
    k=718
    #654231
    #print(sol.getPermutation(n,k))
    n=9
    k=135401
    #439157826
    #print(sol.getPermutation(n,k))
    n = 2
    k = 1
    print(sol.getPermutation(n,k))
    # 12