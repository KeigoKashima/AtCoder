N = int(input())
ai =[int(a) for a in input().split()]
# print(ai)
# ai.sort() #小さい順に並べ変える
ai.sort(reverse=True) #大きい順に並べ変える
# print(ai) 

A=0
B=0

i = 0
for a in ai:
    if(i==0):
        A+=a
        i = 1
    else:
        B+=a
        i = 0
div = A - B
print(div)