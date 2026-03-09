from fastapi import FastAPI

app= FastAPI()

# Product database (list of dictionaries)
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 599, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 120, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": False},
    {"id": 4, "name": "USB Cable", "price": 199, "category": "Electronics", "in_stock": True},

    # Q1 — Added products
    {"id": 5, "name": "Laptop Stand", "price": 899, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1499, "category": "Electronics", "in_stock": False},
]


# ------------------------------
# Base endpoint
# ------------------------------
@app.get("/")
def home():
    return {"message": "Welcome to My E-commerce Store API"}


# ------------------------------
# Q1 - Show all products
# ------------------------------
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }


# ------------------------------
# Q2 - Filter by category
# ------------------------------
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):

    filtered = [
        product for product in products
        if product["category"].lower() == category_name.lower()
    ]

    if not filtered:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "products": filtered,
        "count": len(filtered)
    }


# ------------------------------
# Q3 - Show only in-stock products
# ------------------------------
@app.get("/products/instock")
def get_instock_products():

    instock = [
        product for product in products
        if product["in_stock"] is True
    ]

    return {
        "in_stock_products": instock,
        "count": len(instock)
    }


# ------------------------------
# Q4 - Store summary
# ------------------------------
@app.get("/store/summary")
def store_summary():

    total_products = len(products)

    in_stock = len([
        p for p in products
        if p["in_stock"]
    ])

    out_of_stock = total_products - in_stock

    categories = list({
        p["category"] for p in products
    })

    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": in_stock,
        "out_of_stock": out_of_stock,
        "categories": categories
    }


# ------------------------------
# Q5 - Search products
# ------------------------------
@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    matches = [
        product for product in products
        if keyword.lower() in product["name"].lower()
    ]

    if not matches:
        return {"message": "No products matched your search"}

    return {
        "matched_products": matches,
        "count": len(matches)
    }


# ------------------------------
# BONUS - Cheapest & most expensive
# ------------------------------
@app.get("/products/deals")
def product_deals():

    cheapest = min(products, key=lambda x: x["price"])
    expensive = max(products, key=lambda x: x["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }