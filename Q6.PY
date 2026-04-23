basic = int(input("Enter basic salary: "))

# Calculating allowances
da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

# Total salary
total_salary = basic + da + ta + hra

print("DA =", da)
print("TA =", ta)
print("HRA =", hra)
print("Total Salary =", total_salary)