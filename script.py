max=16

Nlist=[]
Tlist=[]
def N(i):
    total = 0
    for j in range(i):
        if(i&j==0):
            total += 1
    return total

def T(n):
    total=0
    for i in range(n):
        total += N(i)
    return total
T(max+1)

print("i  N(i)  T(n)")
for n in range(max+1):
    #print Nlist,Tlist
    print(str(n) + "  " + str(N(n)) + "  " + str(T(n)))
    

