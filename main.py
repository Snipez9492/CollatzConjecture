# print("First Commit")


def collatz_Conjecture(n):
    while n != 1:
        lst = []
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        lst.append(str(n))
        ans = " ".join(lst)
        print(ans)


num = int(input("Please enter a number: "))

print(collatz_Conjecture(num))

# n = 19

# while n != 1:
#     lst = []
#     if n % 2 == 0:
#         n = n / 2
#     else:
#         n = (3 * n) + 1
#     lst.append(str(n))
#     ans = " ".join(lst)
#     print(ans)
