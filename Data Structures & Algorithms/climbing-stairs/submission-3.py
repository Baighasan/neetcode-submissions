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

        0, 1, 2, 3, 4, 5
        8  5  3  2  1  1
        """
        one, two = 1, 1
        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        
        return one
        