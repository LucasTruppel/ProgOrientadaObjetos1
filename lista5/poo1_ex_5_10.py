entrada = input().split()
conector1 = [int(i) for i in entrada]
entrada = input().split()
conector2 = [int(i) for i in entrada]
compativel = 'Y'
for j in range(0, 5):
    if conector1[j] == conector2[j]:
        compativel = 'N'
print(compativel)
