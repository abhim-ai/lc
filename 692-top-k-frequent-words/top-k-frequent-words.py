from collections import Counter
import heapq 
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counter_dict=Counter(words)
        freq=[]
        for w,c in counter_dict.items():
            freq.append((-c,w))
        heapq.heapify(freq)

        res=[]
        while len(res)<k:
            neg_cnt,word=heapq.heappop(freq)
            res.append(word)
        return res

        