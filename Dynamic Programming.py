# solves problems by breaking them down into simpler subproblems
# and storing the results of subproblems to avoid redundant computations.

# ... but so deoes recursion, divide and conquer, memoization, etc.
# What makes dynamic programming unique is its focus on overlapping subproblems
# and optimal substructure properties.
# Example: Fibonacci sequence using dynamic programming
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

# DP must have:
# 1. Overlapping subproblems - the same subproblems are solved multiple times. 
# 2. Optimal substructure - solutions to subproblems must contribute to the solution of the overall problem.

# common misinterepretation: "Dynamic programming is just recursion with memoization."
# Recurrence based => DP. Example:
# f(i) = max(f(i-1)+array[i], array[i])
# The above has no overlapping subproblems, so it is not DP.
# f(n) does not depend on f(n-2), f(n-3), etc. hence does not compute subproblems many times.
# However, it has optimal substructure, as the solution to f(n) depends on the solution to f(n-1).

# Common dynamic programming problems:
# 1. Fibonacci Sequence
# 2. Knapsack Problem
# 3. Longest Common Subsequence
# 4. Coin Change Problem
# 5. Edit Distance
# 6. Matrix Chain Multiplication
# 7. Rod Cutting Problem
# 8. Partition Problem
# 9. Traveling Salesman Problem
# 10. Optimal Binary Search Tree
# 11. Egg Dropping Problem
# 12. Subset Sum Problem    
# 13. Longest Increasing Subsequence
# 14. Word Break Problem
# 15. Palindrome Partitioning
# 16. Catalan Numbers
# 17. Bellman-Ford Algorithm
# 18. Floyd-Warshall Algorithm
# 19. Viterbi Algorithm 
# 20. LRU Cache Implementation

# 1. Fibonacci Sequence
# f(n) = f(n-1) + f(n-2)
def fibonacci_dp(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
print(fibonacci_dp(10))  # Output: 55
# Definition: Fibonacci numbers are a sequence where each number is the sum of the two preceding ones, starting from 0 and 1.
# explanation: This function computes the nth Fibonacci number using a bottom-up dynamic programming approach.
# It initializes a list dp where dp[i] will hold the ith Fibonacci number.
# It iteratively fills this list using the relation f(n) = f(n-1) + f(n-2).
# The time complexity is O(n) and the space complexity is also O(n).
