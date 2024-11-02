class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result=sorted(list(set(nums)))
        
        for i in range(len(nums)):
            if i<len(result):
                nums[i]=result[i]
        k=len(result)
        return k