class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        map = {}
        
        for idx, num in enumerate(nums):
            test = target - num
            if test in map:
                return [map[test], idx]
            map[num] = idx

nums = [2,7,11,15]
target = 9

s = Solution()
result = s.twoSum(nums, target)
print(result)