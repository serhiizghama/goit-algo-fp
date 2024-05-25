def greedy_algorithm_alternate(items_dict, budget_amount):
    sorted_items = sorted(
        items_dict.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item_name, item_info in sorted_items:
        if total_cost + item_info['cost'] <= budget_amount:
            total_cost += item_info['cost']
            total_calories += item_info['calories']
            selected_items.append(item_name)

    return {"selected_items": selected_items, "total_cost": total_cost, "total_calories": total_calories}


def dynamic_programming_alternate(items_dict, budget_amount):
    n = len(items_dict)
    dp = [[0] * (budget_amount + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name, item_info = list(items_dict.items())[i - 1]
        cost = item_info['cost']
        calories = item_info['calories']
        for j in range(1, budget_amount + 1):
            if cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)

    selected_items = []
    j = budget_amount
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_name, _ = list(items_dict.items())[i - 1]
            selected_items.append(item_name)
            j -= items_dict[item_name]['cost']

    return {"selected_items": selected_items, "total_cost": budget_amount - j, "total_calories": dp[n][budget_amount]}


items_dict = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget_amount = 100

print("Greedy Algorithm:")
print(greedy_algorithm_alternate(items_dict, budget_amount))
print("\nDynamic Programming:")
print(dynamic_programming_alternate(items_dict, budget_amount))
