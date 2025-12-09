class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Edge cases:
        # 1. Negative numbers are not palindromes.
        # 2. Numbers ending in 0 (except 0 itself) cannot be palindromes.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        
        # We only need to reverse the second half of the number.
        # The loop stops when revertedNumber is greater than or equal to x.
        while x > revertedNumber:
            # Get the last digit of x and append it to revertedNumber
            revertedNumber = revertedNumber * 10 + x % 10
            
            # Remove the last digit from x
            x //= 10

        # When the length is an even number, x and revertedNumber will be equal.
        # When the length is an odd number, the middle digit is in revertedNumber, 
        # so we get rid of it by revertedNumber // 10. 
        # For example, if input is 121, at the end of the loop x = 1, revertedNumber = 12.
        # 1 == 12 // 10 is True.
        return x == revertedNumber or x == revertedNumber // 10

"""
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
