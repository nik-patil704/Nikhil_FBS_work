cost_price = int(input("Enter the cost price:"))
discount_percent = int(input("Enter the discount percent: "))

discount_amount = (cost_price - discount_percent) /100
selling_price = cost_price - discount_amount

print(f"selling price = {selling_price}")