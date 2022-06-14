
from collections import defaultdict
from itertools import count

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # res = defaultdict(list)
    # print(ord("a"))
    # for s in strs:
    #     count = [0] *26
    #     for c in s:
    #         count[ord(c) - ord("a")] += 1
    #     res[tuple(count)].append(s)
    # return res.values()
    res = {}
    for s in strs:
        sortedword = ",".join(sorted(s)).replace(",","")
        print(sortedword)
        if sortedword in res:
            count+=1
        else:
            res.append(sorted)
    return res 

        

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))