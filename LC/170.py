class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.nums={}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.nums[number]=self.nums.get(number,0)+1
        
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for x in self.nums:
            if value-x in self.nums and (value-x!=x or self.nums[x]>1):
                return True
        return False
        
# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)