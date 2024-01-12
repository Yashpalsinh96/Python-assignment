def find_customers_without_computer(N, S):
    occupied = set()
    customers_without_computer = 0

    for letter in S:
        if letter not in occupied:
            occupied.add(letter)
        else:
            occupied.remove(letter)

    customers_without_computer = len(occupied)

    return customers_without_computer

N1 = 3
S1 = "GACCBDDBAGEE"
result1 = find_customers_without_computer(N1, S1)
print("Example 1:", result1)  


N2 = 1
S2 = "ABCBAC"
result2 = find_customers_without_computer(N2, S2)
print("Example 2:", result2)