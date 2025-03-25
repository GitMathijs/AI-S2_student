#1.1.a

# for loops
def piramide(n):
    for i in range(1, n+1):
        print("*" * i)
    for i in reversed(range(1, n)):
        print("*" * i)

piramide(5)

# while loops reversed

def piramide_2(n):
    count = 1
    while (count <= n):
        print(" " * (n-count) + "*" * (count))
        count += 1
    count = n - 1
    while (count >= 1):
        print(" " * (n-count) + "*" * count)
        count -= 1

piramide_2(5)

#1.1.b

def eerste_verschil(a, b):
    for index in range(len(a)):
        if a[index] != b[index]:
            return index

print(eerste_verschil("Hallo", "Hallu"))

#1.1.c
# test commit