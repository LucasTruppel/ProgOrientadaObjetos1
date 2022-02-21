lado_chocolate = int(input())
n = 0
while lado_chocolate >= 2:
    lado_chocolate = lado_chocolate / 2
    n = n + 1
quantidade_chocolate = 4 ** n
print(quantidade_chocolate)
