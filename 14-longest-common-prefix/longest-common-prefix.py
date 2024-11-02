class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs =sorted(strs,key=len)
        result=[]
        k=0
        count=0
        for i in strs[0]:
            for j in range(1,len(strs)):
                print(strs[j][k])
                if strs[j][k]==i:
                    count+=1
                else:
                    return ''.join(result)
            if count==len(strs)-1:
                result.append(i)
            count=0
            k+=1
        return ''.join(result)
        