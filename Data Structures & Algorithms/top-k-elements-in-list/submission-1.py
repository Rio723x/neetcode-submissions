class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        ans=[]
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for key , values in freq.items():
            ans.append([values,key])
        ans.sort()
        res=[]
        for j in range(len(ans)-1, len(ans)-k -1, -1):
            res.append(ans[j][1])
        return res