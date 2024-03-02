t = int(input())

for z in range(t):
    st = input()
    a = 0
    b = 0
    for i in range(5):
        if st[i] == "A":
            a += 1
        else:
            b += 1
        
        if a > 2:
            print("A")
            break
        elif b > 2:
            print("B")
            break