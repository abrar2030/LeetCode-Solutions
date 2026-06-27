class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # Time Complexity: O(n)

        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i