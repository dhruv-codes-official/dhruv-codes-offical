class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # A dictionary to store the last seen index for each number.
        # Key: the number (int)
        # Value: its most recent index (int)
        last_seen = {} 
        
        for i in range(len(nums)):
            current_num = nums[i]
            
            # Check if the current number has been seen before
            if current_num in last_seen:
                # If it has, check the distance constraint: |i - last_seen[current_num]| <= k
                last_index = last_seen[current_num]
                
                if i - last_index <= k:
                    # The absolute difference between the current index (i) and 
                    # the last seen index (last_index) is at most k.
                    return True
            
            # Update the last seen index for the current number.
            # This ensures we always use the most recent occurrence for the distance check.
            last_seen[current_num] = i
            
        # If the loop finishes without finding any pair that satisfies the condition
        return False
