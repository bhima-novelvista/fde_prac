products = ["Jeans", "T-Shirt", "Jacket", "Sneakers", "Hat"]
print(len(products)) #length of the list

products.append("Socks") #adding an element to the list
print(products)


#Dictionary
products_dict = {} #empty dictionary
products_dict = {"Jeans": 2000, "T-Shirt": 1000}
print(products_dict)

order = {
    "order_id": "ORD123",
    "store": "Pune01",
    "product": "Jeans",
    "price": 2000,
}

print(order)

order["qty"] = 2

print(order)

order["price"] = 23.34
print(order)

orders = [
    {"order_id": "ORD123", "store": "Pune01", "product": "Jeans", "price": 2000},
    {"order_id": "ORD124", "store": "Pune02", "product": "T-Shirt", "price": 1000},
    {"order_id": "ORD125", "store": "Pune03", "product": "Jacket", "price": 3000},
]

print(orders[2])