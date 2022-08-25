budget = int(input())

in_budget = True
while in_budget:
    current_purchase = input()
    if current_purchase == "End":
        break
    amount = int(current_purchase)
    budget -= amount
    if budget >= 0:
        continue
    in_budget = False
    break

if in_budget:
    print("You bought everything needed.")
else:
    print("You went in overdraft!")
