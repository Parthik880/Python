def luck(d):
    return max((key for key,value in d.items() if key==value),default=None)
from collections import Counter
m=input("Enter the numbers: ")
f= list(map(int,m.split()))
n=Counter(f)
c= luck(n)

print(f"Your luck Number is : {c}")