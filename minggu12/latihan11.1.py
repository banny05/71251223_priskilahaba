dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(f"dictionary : {dictionary}")
print()
print(f"{'key':<10} {'value':<10} {'item'}")

item = 1
for key in dictionary:
    print(f"{key:<10} {dictionary[key]:<10} {item}")
    item += 1