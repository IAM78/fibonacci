n=int (input("n::"))

fib=[0,1]

for k in range(2,n+1):

    fib.append(fib[k-1]+fib[k-2])

print(fib)