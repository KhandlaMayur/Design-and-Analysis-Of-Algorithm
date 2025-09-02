def knapsack(weights, profits, capacity):
    n = len(weights)
    # Create DP table (n+1) x (capacity+1)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                # Either take the item or leave it
                dp[i][w] = max(profits[i-1] + dp[i-1][w - weights[i-1]],
                               dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]
profits = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_profit = knapsack(weights, profits, capacity)
print("Maximum Profit:", max_profit)
