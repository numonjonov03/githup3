n=int(input())
for i in range(2,n):
    while n%i==0:
        print(i)
        n=n//i
print(n)