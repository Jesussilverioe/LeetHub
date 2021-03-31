class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval = 99999
        profit = 0
        for num in prices:
            minval = min(num,minval)
            compra = num - minval
            profit = max(profit, compra)
            
        return profit