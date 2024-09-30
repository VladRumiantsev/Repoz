a = int(input("Enter the first number a: "))
b = int(input("Enter the second number b: "))
c = int(input("Enter the third number c: "))
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print("Sorted output (a,b,c):", a, b, c)