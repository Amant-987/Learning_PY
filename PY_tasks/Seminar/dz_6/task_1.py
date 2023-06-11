first_el = int(input("Enter first element for progression: "))
diff_progr = int(input("Enter difference of progression: "))
quantity_el = int(input("Enter quantity of element for progression: "))

progression = [first_el + (i-1) * diff_progr for i in range(1, quantity_el + 1)]

print("Element of progression: ")
for elem in progression:
    print(elem)