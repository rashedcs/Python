n, k = map(int,input().split())
l = [int(n) for n in input().split()]

print(l)

i = 0
while i <= n - 1:
    if l[i] > 0:
        if l[i] >= l[k - 1]:
            i = i + 1
        else :
            break
    else :
        break
print(int(i))
