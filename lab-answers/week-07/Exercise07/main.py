"""
Write a function groupProductsByCategory(jsonStr) that takes as input a JSON string representing a list of products. Each product in the list contains a category field. 
The function should return a new JSON string in which the products are grouped based on their respective categories.
"""

import json

def groupProductsByCategory(jsonStr):
    products = json.loads(jsonStr)
    
    grouped = {}

    for product in products:
        category = product['category']

        product_without_category = {k: v for k, v in product.items() if k != 'category'}

        if category not in grouped:
            grouped[category] = []
        grouped[category].append(product_without_category)
    
    return json.dumps(grouped)

print(groupProductsByCategory('''
[
  {"id" : 1, "name": "Apple", "category": "Fruits"},
  {"id" : 2,"name": "Carrot", "category": "Vegetables"},
  {"id" : 3,"name": "Banana", "category": "Fruits"}
]
'''))
print(groupProductsByCategory('''
[
  {"name": "Orange", "category": "Fruits"},
  {"name": "Apple", "category": "Fruits"},
  {"name": "Grapes", "category": "Fruits"}
]
'''))
print(groupProductsByCategory('''
[
  {"name": "Milk", "category": "Dairy"},
  {"name": "Bread", "category": "Bakery"},
  {"name": "Rice", "category": "Grains"}
]
'''))
print(groupProductsByCategory('''
[
    {"id": 1, "name": "iPhone", "category": "Electronics", "price": 1200},
    {"id": 2, "name": "MacBook", "category": "Electronics", "price": 2000},
    {"id": 3, "name": "Banana", "category": "Food", "price": 2},
    {"id": 4, "name": "Bread", "category": "Food", "price": 3},
    {"id": 5, "name": "T-shirt", "category": "Clothing", "price": 25}
]
'''))
print(groupProductsByCategory('''
[
]
'''))
print(groupProductsByCategory('''
[
  {"name": "Cheddar", "category": "Dairy Products"},
  {"name": "Brie", "category": "Dairy Products"},
  {"name": "Baguette", "category": "Baked Goods"}
]
'''))
print(groupProductsByCategory('''
[
  {"name": "Laptop", "category": "Electronics", "price": 1000},
  {"name": "Phone", "category": "Electronics", "price": 799},
  {"name": "Shirt", "category": "Clothing", "price": 29.99}
]
'''))