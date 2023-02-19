import math
f = input()                #gets the function
x1 = int(input())          #start of measurement
x2 = int(input())          #end of measurement
n = abs((x2-x1)*1000)
r = 0
x = 0

for i in range(n):
    x1 = x1 + 0.001
    x = x1
    y = eval(f)
    s = 0.001 * y
    r = r + s
print(abs(r))             #area per x-axis



