class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        sum = 0
        i =1
        while i < n:
            a = prices[i]-prices[i-1]
            if a >0:
                sum +=a
            i +=1
        return sum

a = Solution()
list1=[7,1,5,3,6,4]
print(a.maxProfit(list1))