# 🛒 Grocery List Organizer
# Uses lists, sets, and dictionaries to organize groceries, remove duplicates, and calculate total cost.

# Sample grocery list (duplicates included)
grocery_list = ["milk", "eggs", "bread", "eggs", "cheese", "apples", "bread", "milk"]

# Convert list to a set to remove duplicates
unique_groceries = set(grocery_list)

# Dictionary to store item prices
grocery_prices = {
    "milk": 2.99,
    "eggs": 3.50,
    "bread": 2.00,
    "cheese": 4.50,
    "apples": 1.75,
    "bananas": 1.20  # Added an extra item to show flexibility
}

# Calculate total cost for items in the list (if price exists)
total_cost = sum(grocery_prices.get(item, 0) for item in unique_groceries)

# Display the unique grocery list and total cost
print("\n🛍️ Unique Grocery List:")
for item in sorted(unique_groceries):  # Sorted for better readability
    print(f"- {item}")

print(f"\n💰 Total Estimated Cost: ${total_cost:.2f}")

# Optional: Show which items had no price listed
unpriced_items = unique_groceries - grocery_prices.keys()
if unpriced_items:
    print("\n⚠️ The following items are missing prices:", unpriced_items)