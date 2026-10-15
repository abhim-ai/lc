class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter_dict={}
        freq=[[] for i in range(len(nums)+1)]
        for n in nums:
             counter_dict[n]=1+counter_dict.get(n,0)
        for n,c in counter_dict.items():
            freq[c].append(n)
        
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
        
        