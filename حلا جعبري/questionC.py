L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']

b_items = []

for item in L:
  if item.startswith("B"):
    b_items.append(item)

if b_items:
  print("Items starting with 'B':", b_items)
else:
  print("No items start with 'B' in the list.")
