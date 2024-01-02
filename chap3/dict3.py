# auth:eric.yu
# date: 2023/7/24 17:36

items=["fruits","books","others","person"]
prices=[96,56,87,60]
d = {item.upper():price for item,price in zip(items,prices)}
print(d)
