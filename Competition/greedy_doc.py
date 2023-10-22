def min_box_movement_cost(current_order, current_costs, required_order):
    n = len(current_order)
    dp = [[float('inf')] * n for _ in range(n)]

    # Initialize the base case
    for i in range(n):
        dp[i][0] = current_costs[i]  # Cost to move to the first box

    for j in range(1, n):
        for i in range(n):
            for k in range(n):
                if i != k:
                    # Calculate the cost of moving from box i to box k
                    cost_to_move = current_costs[k] + current_costs[i]
                    dp[k][j] = min(dp[k][j], dp[i][j - 1] + cost_to_move)

    min_cost = float('inf')
    for i in range(n):
        # Calculate the cost of moving from the last box to the required order
        cost_to_move = current_costs[i]
        min_cost = min(min_cost, dp[i][n - 1] + cost_to_move)

    return min_cost

n = int(input())
costs = list(map(int, input().split()))
order = list(input().split())
required_order = list(input().split())

box_costs = {order[i]: costs[i] for i in range(n)}
#print(box_costs)

# Test the function
box_order = order
print(min_box_movement_cost(box_order, costs, required_order))  # Output: 15