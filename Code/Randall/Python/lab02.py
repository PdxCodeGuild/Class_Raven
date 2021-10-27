x = float(input("Enter a dollar amount: "))

t = x*100

q = t//25
t = t%25

d = t//10
t = t%10

n = t//5
t = t%5

p = t

print(f"{q} quarters, {d} dimes, {n} nickels, {p} pennies") 