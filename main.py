n=int(input("Enter a number of rows: "))
for c in range(n+1):
    for d in range(c):
        print("*", end=" ")
    print()
