n = 0
for i in range(1,11):
    for j in range(1,21):
        for k in range(1,41):
            l=40-i-j-k
            if l>0:
                if (10*i+5*j+k*2+l)==100:
                    if (i+j+k+l)==40:
                        n+=1
print(n)