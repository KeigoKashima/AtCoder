IN = input().split()
N,A,B = [int(input) for input in IN]
SUM = 0
# print("N:"+str(N)+" A:"+str(A)+" B:"+str(B))
for n in range(N):
    n+=1
    sum_n = 0
    a4 = 0
    a3 = 0
    a2 = 0
    a1 = 0
    a0 = 0

    a4 = int(n/10000)
    a3 = int((n-10000*a4)/1000)
    a2 = int((n-10000*a4-1000*a3)/100)
    a1 = int((n-10000*a4-1000*a3-100*a2)/10)
    a0 = int((n-10000*a4-1000*a3-100*a2-10*a1))
    sum_n = a4+a3+a2+a1+a0
    if (sum_n>=A)and(sum_n<=B):
        SUM += n

print(SUM)