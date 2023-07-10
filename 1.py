
f = 'geeksforgeeks'

for i in range(len(f)-1):
    e = len(f) - 1
    s = i + 1
    while s < e:
        if (f[i] == f[e]) and (i != e):
            print(f[i],f[i+1:e],e-i-1)
            break
        e -= 1

