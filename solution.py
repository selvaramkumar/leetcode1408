class Solution:
    def stringMatching(self, words) :
        temp=[]
        temp2=[]
        words_sorted=words[::-1]
        for i in range(0,len(words)):
            for j in range(1,len(words)):
                if i !=j:
                    if words[i] in words[j] :
                        temp.append(words[i])
        for i in range(0,len(words_sorted)):
            for j in range(1,len(words_sorted)):
                if i !=j:
                    if words_sorted[i] in words_sorted[j] :
                        temp2.append(words_sorted[i])
        temp=temp+temp2
                
        return (list(set(temp)))
                
                
s=Solution()
a=["mass","as","hero","superhero"]
print(s.stringMatching(a))            
        