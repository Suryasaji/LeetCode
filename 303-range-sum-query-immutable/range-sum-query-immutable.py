class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.p = [0]
        sum1=0
        for i in range(0,len(nums)):
            sum1+= nums[i]
            self.p.append(sum1)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.p[right+1] - self.p[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)