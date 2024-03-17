class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def hashmap(nums, target):
            indexes = {}
            for i, num in enumerate(nums):
                complement = target - num
                # Verifica o que falta no número atual para chegar no objetivo
                # E então procura ele dentro da table, se tiver lá, retorna
                if complement in indexes:
                    return [indexes[complement], i]

                indexes[num] = i
    return hashmap(nums, target)
