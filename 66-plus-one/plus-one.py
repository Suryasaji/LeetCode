class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1=''
    
        for i in digits:
            str1=str1+str(i)
        print(str1)
        num=int(str1)
        num=num+1
        digits=list(map(int,str(num)))
        return digits
