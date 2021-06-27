class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        '''
        find the position of str[0] in goal, slice [pos:]
        concatenate slice + [;pos] and check == s
        '''
        if s == '' and goal == '':
            return True
        if s == '' and goal != '':
            return False
        if s != '' and goal == '':
            return False
        if s == goal:
            return True
        if len(s) != len(goal):
            return False
        i = 1
        s_start = s[0]
        substr1, substr2 = '', ''
        front1, fron2 = '', ''
        back1, back2 = '', ''
        while True:
            front1 = s[i:]
            front2 = s[:i]
            new_front = front1 + front2
            if new_front == goal:
                return True
            back1 = s[:-i]
            back2 = s[-i:]
            new_back = back1 + back2
            if new_back == goal:
                return True
            i += 1
            if i >= len(s):
                break
        return False

        while True:
            curr = goal[i]
            if curr == s_start:
                substr1 = goal[i:]
                substr2 = goal[:i]
                break
            i += 1
            if i >= len(s):
                return False

        new_str = substr1 + substr2

        if new_str == s:
            return True

        return False

if __name__=="__main__":
    sol = Solution()
    s = "bbbacddceeb"
    goal = "ceebbbbacdd"
    # true
    print(sol.rotateString(s, goal))