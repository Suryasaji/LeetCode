class Solution:
    def romanToInt(self, s: str) -> int:
        dicts = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=0
        list1=list(s)
        while( True):
            if len(list1)==1:
                sum=sum+dicts[list1[0]]
                return sum
            elif dicts[list1[0]]<dicts[list1[1]]:
                sum=sum+(dicts[list1[1]]-dicts[list1[0]])
                list1.remove(list1[0])
                list1.remove(list1[0])
                if len(list1)==0:
                    return sum
            else:
                sum=sum+dicts[list1[0]]
                list1.remove(list1[0])
                

        