"""shop_calculator"""
total_price = 0
items_num = int(input("Number of items: "))
while items_num <= 0:
    print("Invalid number of items!")
    items_num = int(input("Number of items: "))
for i in range(items_num):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > 100:
    total_price *= 0.9
print(f"Total price for {items_num} items is ${total_price:.2f}")

