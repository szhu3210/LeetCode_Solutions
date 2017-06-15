class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums=nums
        self.maxInd=len(nums)
        self.BIT=[0 for _ in range(self.maxInd+1)]
        for i,num in enumerate(nums):
            k=i+1
            while k<=self.maxInd:
                self.BIT[k]+=num
                k+=k&-k # last bit

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        val_change=val-self.nums[i]
        self.nums[i]=val
        k=i+1
        while k<=self.maxInd:
            self.BIT[k]+=val_change
            k+=k&-k

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        sumi, sumj = 0, 0
        k=j+1
        while k>0:
            sumj+=self.BIT[k]
            k-=k&-k
        k=i
        while k>0:
            sumi+=self.BIT[k]
            k-=k&-k
        return sumj-sumi

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)