class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy,sell=0,0
        # index=prices.index(min(prices))
        # buy=prices[index]
        # prices=prices[index:]
        # if prices!=[]:
        #     sell=max(prices)
        # else:
        #     return 0
        # return sell-buy

        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit