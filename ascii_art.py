def ascii_art1(n):
    for i in range(n):
        for j in range(10):
            if i % 2 == 0:
                if j % 2 == 0:
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                if j % 2 == 0:
                    print(" ", end="")
                else:
                    print("*", end="")
        print()

def ascii_art2(n):
    stack = 0
    for i in range(n):
        for j in range(10):
            if j < stack:
                print(" ",end="")
            else:
                print("*",end="")
        print()
        stack += 1

def ascii_art3(n):
    fibo = [1, 1]
    for i in range(2, n):
        next_fibo = fibo[i-1] + fibo[i-2]
        fibo.append(next_fibo)

    for i in fibo:
        print("*" * i)

def ascii_art4(n):
    space = 0
    for i in range(n):
        for j in range(space):
            print(" ",end="")
        print("*" * 5)
        space += 1

def ascii_art5(n):
    for i in range(n):
        for j in range(1, n + 1):
            print(j, end=" ")
        print()

def ascii_art6(n):
    sum = 1
    for i in range(n):
        for j in range(1, n + 1):
            if j <= sum:
                print(j, end=" ")
        sum += 1
        print()

def ascii_art7(n):
    max = n
    for i in range(n):
        for j in range(1, n + 1):
            if j <= max:
                print(j, end=" ")
        max -= 1
        print()

def ascii_art8(n):
    num = 1
    for i in range(n):
        for j in range(1, n + 1):
            print(num, end=" ")
        num += 1
        print()

def ascii_art9(n):
    for i in range(1, n + 1):
        for j in range(n, 0, -1):
            if j <= i:
                print(i, end=" ")
            else :
                print(" ", end=" ")
        print()

def ascii_art10(n):
    for i in range(n):
        if i % 2 == 0:
            for j in range(1, n + 1):
                print(j, end=" ")
        else:
            for j in range(n, 0, -1):
                print(j, end=" ")
        print()

def ascii_art11(n):
    min = 1
    max = n
    for i in range(n):
        for j in range(n):
            if j % 2 == 0:
                print(min, end=" ")
            else:
                print(max, end=" ")
        print()
        min += 1
        max -= 1

# ascii_art1(5)
# ascii_art2(6)
# ascii_art3(7)
# ascii_art4(5)
# ascii_art5(7)
# ascii_art6(7)
# ascii_art7(7)
# ascii_art8(7)
# ascii_art9(7)
# ascii_art10(7)
ascii_art11(7)