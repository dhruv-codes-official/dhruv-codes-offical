class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        """
        Calculates the maximum wealth among all customers.

        Args:
            accounts: An m x n integer grid where accounts[i][j] is 
                      the amount of money the i-th customer has in the j-th bank.

        Returns:
            The maximum wealth among all customers.
        """
        max_wealth = 0
        
        # Iterate over each customer's list of accounts
        for customer_accounts in accounts:
            # Calculate the total wealth for the current customer
            current_wealth = sum(customer_accounts)
            
            # Update the maximum wealth if the current customer is wealthier
            if current_wealth > max_wealth:
                max_wealth = current_wealth
                
        return max_wealth

# Alternative one-liner using list comprehension and the max function:
class SolutionOneLiner:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(sum(customer_accounts) for customer_accounts in accounts)


# Test Case :
"""
Input : accounts = [[1,2,3],[3,2,1]]
Explanation :
Customer_1 : at index(0) has wealth 1+2+3 = (6)
Customer_2 : at index(1) has wealth 1+2+3 = (6)

Output:
max(6,6) = 6
"""
