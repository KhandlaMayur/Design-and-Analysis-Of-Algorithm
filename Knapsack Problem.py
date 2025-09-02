def fractional_knapsack(weights, profits, capacity):
    n = len(weights)

    ratio = [(profits[i] / weights[i], weights[i], profits[i]) for i in range(n)]

    ratio.sort(key=lambda x: x[0], reverse=True)
    
    gain = 0.0  

    for r, wt, profit in ratio:
        if wt <= capacity:
            # take whole item
            gain += profit
            capacity -= wt
        else:
            # take fractional part
            fraction = capacity / wt
            gain += profit * fraction
            break   # knapsack is full
    
    return gain

profits = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_profit = fractional_knapsack(weights, profits, capacity)
print("Maximum Profit:", max_profit)
