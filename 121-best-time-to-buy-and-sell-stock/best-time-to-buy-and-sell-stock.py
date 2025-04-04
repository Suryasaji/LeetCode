class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cp=prices[0]
        profit=0
        for i in range(len(prices)):
            if prices[i]<cp:
                cp=prices[i]
            if (prices[i]-cp)>profit:
                profit = prices[i]-cp
        return profit

        