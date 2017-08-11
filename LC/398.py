class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        c = 0
        for i, num in enumerate(self.nums):
            if num != target:
                continue
            c += 1
            n = random.randint(1, c)
            if c==n:
                res = i
        return res