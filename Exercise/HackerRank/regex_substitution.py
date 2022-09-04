import re

n = int(input())
lines = []

for i in range(n):
    s = input()
    lines.append(s)
    
for line in lines:
    k = re.sub(r'( && )+', ' and ', line)
    k = re.sub(' ?\|\| ', ' or ', k)
    print(k)
    