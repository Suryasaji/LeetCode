class Solution:
    def isValid(self, s: str) -> bool:
        dict1={'(':')','[':']','{':'}'}
        result=[]
        for i in s:
            if i in dict1.keys():
                
                result.append(i)
            elif len(result)==0 and i not in dict1.keys():
                return False
                
            elif  i == dict1[result[-1]]:
                result.pop()
            else:
                print(dict[result[-1]])
                return False
        if len(result)==0:
            return True
        else:
            return False