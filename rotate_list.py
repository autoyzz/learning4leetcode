class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            a = nums.pop()
            nums.insert(0,a)
            k -=1
        

a = Solution()
list1=[1,2,3,4,5,6,7]
b = 3
print(a.rotate(list1,b))