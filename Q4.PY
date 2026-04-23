a = int(input('enter first side:'))
b = int(input('Enter second side:'))
c = int(input('Enter third side:'))

if a > 0 and b > 0 and c > 0 and (a + b > c)and (a + c > b) and (b + c > a):
    print("The tringle is valid")
else:
    print("The tringle is not valid")
