class Solution:
    def climbStairs(self, n: int) -> int:
        """
                    0
                   / \
                  1   2
                 / \ / \
                2   3   4
               / \ / \ / \
              3   4   5   6
             / \ / \ /
            4   5   6
           / \
          5   6

        """
        tracker = [-1] * (n + 1)
        def backtrack(cur):
            if cur == n:
                return 1
            if cur > n:
                return 0
            if tracker[cur] != -1:
                return tracker[cur]
            
            curSol = backtrack(cur + 1) + backtrack(cur + 2)
            tracker[cur] = curSol
            return curSol

        return backtrack(0)