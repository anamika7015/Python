items = ["banana","apple","orange","mango","mango"]
unique_items = set()
for item in items :
    if item in unique_items:
        print("Duplicate item:",item)
        break
    unique_items.add(item)
