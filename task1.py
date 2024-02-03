import pulp as plp

prob = plp.LpProblem("Beverage Production", plp.LpMaximize)

lemonade = plp.LpVariable("Lemonade", 0, None, plp.LpInteger)
fruit_juice = plp.LpVariable("FruitJuice", 0, None, plp.LpInteger)

prob += lemonade + fruit_juice, "TotalProduction"

prob += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
prob += 1 * lemonade + 0 * fruit_juice <= 50, "Sugar"
prob += 1 * lemonade + 0 * fruit_juice <= 30, "LemonJuice"
prob += 0 * lemonade + 2 * fruit_juice <= 40, "FruitPuree"

prob.solve()


print(f"Status: {plp.LpStatus[prob.status]}")
print(f"Lemonade: {plp.value(lemonade)} units")
print(f"Fruit Juice: {plp.value(fruit_juice)} units")
print(f"Total Production: {plp.value(prob.objective)} units")
