smallest = None
print("Before:", smallest)
for itervar in [3, 42, 12, 9, 69, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)