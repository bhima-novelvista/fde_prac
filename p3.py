#branch st if elif else
x = 10
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
    
# loop statements
# for loop
for i in range(5):
    print(i)
    
l1 = ["Jeans", "T-Shirt", "Jacket", "Sneakers", "Hat"]
for item in l1:
    print(item)
    
#comparing  operators
# == => if a==b:
# != => if a!=b:
# > => if a>b:
# < => if a<b:
# >= => if a>=b:
# <= => if a<=b:    

orders = [
    {"order_id": "ORD123", "store": "Pune01", "product": "Jeans", "price": 2000},
    {"order_id": "ORD124", "store": "Pune02", "product": "T-Shirt", "price": 1000},
    {"order_id": "ORD125", "store": "Pune03", "product": "Jacket", "price": 3000},
]

for order in orders:
    print(order)
    print("==========")