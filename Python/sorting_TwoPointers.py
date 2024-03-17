class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def sorting_twoPointers(nums, target):
            sortedNums = sorted(enumerate(nums), key=lambda x: x[1])
            # Enumera cada número da table como [indíce, valor]

            left, right = 0, len(nums) - 1
            # Cria os "ponteiros"
            while left < right:
                actualSum = sortedNums[left][1] + sortedNums[right][1]
                # Faz a soma dos números e então verifica os mesmos

                if actualSum == target:
                    return [sortedNums[left][0], sortedNums[right][0]]
                elif actualSum < target:
                    left += 1
                else:
                    right -= 1
    return sorting_twoPointers(nums, target)
