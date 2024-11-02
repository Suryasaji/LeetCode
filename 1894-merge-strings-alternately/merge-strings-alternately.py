class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=[]
        m=max(len(word1),len(word2))
        while(m>0):
            if len(word1)>0:
                result.append(word1[0])
                word1=word1.replace(word1[0],'',1)
                
            if len(word2)>0:
                result.append(word2[0])
                word2=word2.replace(word2[0],'',1)
            m-=1

        return ''.join(result)



            
            
