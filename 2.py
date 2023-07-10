
l =  ['abe','abef','abccc','abftg']

l.sort(key = lambda x: len(x))
k = l[0]
y = True
m = ''
for i in range(len(k)):
    for j in l:
        if k[i] != j[i]:    
            y = False
            break
        else:
            y = True
    if y: 
        m += k[i]

print(m)