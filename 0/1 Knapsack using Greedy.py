def knapsack_greedy_01(weights, profits, capacity):
    n = len(weights)

    # Calculate ratio = profit / weight
    ratio = [(profits[i] / weights[i], weights[i], profits[i]) for i in range(n)]
    ratio.sort(key=lambda x: x[0], reverse=True)

    total_profit = 0
    selected_items = []

    for r, wt, pf in ratio:
        if wt <= capacity:   
            selected_items.append((wt, pf))
            total_profit += pf
            capacity -= wt

    return total_profit, selected_items
weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 50

profit, items = knapsack_greedy_01(weights, profits, capacity)
print("Greedy 0/1 Knapsack Profit:", profit)
print("Selected items (weight, profit):", items)
