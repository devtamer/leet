from itertools import count
import re

class topKFrequent:
    def __init__(self) -> None:
        pass
    def solution1(self, nums, k):
        temp = {}
        for i, num in enumerate(nums):
            temp[num] = temp.get(num, 0)+1
        res = []
        for i in range(k):
            maxx = max(temp ,key=temp.get)
            res.append(maxx)
            del temp[maxx]
        return res

    def solution2(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums)+ 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return(res)

# working
obj = topKFrequent()
nums, k = [1,1,1,2,2,2,2,2,3], 2
print(obj.solution1(nums, k))
print(obj.solution2([1,1,1,2,2,2,2,2,3,5], 2))
