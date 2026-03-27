##2. take input 5 sub 
sub1 = int(input('Enter marks of sub1:'))
sub2 = int(input('Enter marks of sub2:'))
sub3 = int(input('Enter marks of sub3:'))
sub4 = int(input('enter marks of sub4:'))
sub5 = int(input('Enter marks of sub5:'))
# print(type(sub1))

#total marks 
total = sub1+ sub2+ sub3+ sub4+ sub5

#percentage calculation 
percentage =( total / 500) *100

# display result
print("total marks =", total)
print("percentage =", percentage)
