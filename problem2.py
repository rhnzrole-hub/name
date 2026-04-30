def find_top_seller(products: dict, sales: dict) -> str:
    summa = {item: products[item] * sales[item] for item in products}

    max_product = max(summa, key=summa.get)
    
    return max_product


print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10,   "Banan": 5,    "Uzum": 8}
))