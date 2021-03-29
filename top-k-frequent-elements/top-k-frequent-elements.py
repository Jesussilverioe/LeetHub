class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dic = dict()
        for n in nums:
            my_dic[n] = my_dic.get(n,0)+1
        
        ls = heapq.nlargest(k,my_dic.items(), key=lambda i: i[1])
        ls = [k for k,val in ls]

        return ls