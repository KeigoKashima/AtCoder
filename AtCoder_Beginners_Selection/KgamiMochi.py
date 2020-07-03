N = int(input())
d = []
for i in range(N):
    d.append(int(input()))

DAN = 1
d.sort()

for i in range(len(d)-1):
    if d[i] < d[i+1]:
        DAN+=1

print(DAN)