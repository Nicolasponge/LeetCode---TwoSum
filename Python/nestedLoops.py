class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def nestedLoops(nums, target):
          n = len(nums)
          for i in range(n):
            for j in range(i + 1, n):
              # Passa por cada um dos números e o próximo número, soma e verifica
              if nums[i] + nums[j] == target:
                return [i, j]
    return nestedLoops(nums, target)
