class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        flag = 0

        
        for i in nums:
            if i ==0:
                flag +=1
        for i in nums:
            if i ==0 and flag !=0:
                nums.pop(nums.index(i))
                nums.append(0)
                flag -=1
        print(nums)

a = Solution()
a.moveZeroes([1,1,2,3,10,0,0,0,0,0,8,9])
