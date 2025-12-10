# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least 
        twice in the array, and return false if every element is distinct.
        """
        
        # 1. Convert the list to a set. A set automatically removes all duplicates.
        unique_elements = set(nums)
        
        # 2. Compare the length of the original list with the length of the set.
        # If the length of the list is greater than the length of the set, 
        # it means some elements were removed (i.e., duplicates existed).
        return len(nums) > len(unique_elements)
 
