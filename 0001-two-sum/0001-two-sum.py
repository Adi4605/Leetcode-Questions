class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i, num in enumerate(nums):
            calculated = target - num
            if calculated in seen:
                return [seen[calculated], i]
            seen[num]=i