numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
fr = {}
for n in numbers:
    if n in fr:
        fr[n]+=1
    else:
        fr[n] = 1

print(fr)        