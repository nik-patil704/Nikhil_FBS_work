a = int(input("Entrr first side:"))
b = int(input("Enter second side:"))
c = int(input("Enter third side:"))

if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):

    if a == b == c:
        print("The tringle is equilateral")
    elif a == b == c:
        print("The tringle is Isosceles")
    else:
        print("The tringle is scalene")
else:
    print("Invalid tringle")