# _*_coding:utf_8_*_
# Given a 32-bit signed integer,reverse digits of an integer
# another solution: use str()=>int()


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x1 = abs(x)
        if x == 0:
            return 0
        operator = x / x1
        l = []
        while x1 // 10 != 0:
            a = x1 % 10
            l.append(a)
            x1 = x1 // 10
        l.append(x1)
        sum = 0
        n = len(l)
        for i in l:
            sum = sum + i * pow(10, (n - 1))
            n = n - 1
        sum = sum * operator
        if (sum < -pow(2, 31) or sum > pow(2, 31) - 1):
            return 0
        else:
            return int(sum)


b = Solution()
c = b.reverse(-5567)
print(c)
