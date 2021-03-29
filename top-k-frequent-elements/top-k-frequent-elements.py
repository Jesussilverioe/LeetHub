class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dic = dict()
        for n in nums:
            my_dic[n] = my_dic.get(n,0)+1
        my_dic = dict(sorted(my_dic.items(), key=lambda item: item[1], reverse=True))
        ans = []
        for i in range(k):
            ans.append(list(my_dic.keys())[i])
        return ans
            