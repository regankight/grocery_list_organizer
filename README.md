# Grocery List Organizer 🛒  

## 📌 Overview  
A simple Python script that:  
✔ Uses **lists, sets, and dictionaries** to organize grocery items  
✔ Removes duplicate items automatically  
✔ Categorizes groceries by type  
✔ Calculates **total estimated cost**  

## 🔧 Features  
✅ Store groceries in a **list**  
✅ Track **prices** using a dictionary  
✅ Ensure **unique items** using a set  
✅ Print **organized shopping list with total cost**  

## 📜 Code Example  
```python
grocery_list = ["milk", "eggs", "bread", "eggs", "cheese"]
unique_groceries = set(grocery_list)
grocery_prices = {"milk": 2.99, "eggs": 3.50, "bread": 2.00, "cheese": 4.50}
total_cost = sum(grocery_prices[item] for item in unique_groceries)

print(f"Unique groceries: {unique_groceries}")
print(f"Total estimated cost: ${total_cost:.2f}")
