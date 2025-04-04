class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leng =len(nums)
        result=[]
        k=0
        for i in range(leng):
            k=i+1
            for j in range(k,leng):
                if nums[i]+nums[j]==target:
                    result.append(index(i))
                    result.append(index(j))
            
        return result