#1-5 不同的三个数字组合

total = 0 
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and j != k and i != k:
                print(i,j,k)
                total = total + 1
print(total)