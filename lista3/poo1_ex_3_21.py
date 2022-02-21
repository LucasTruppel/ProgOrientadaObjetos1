quantidade_testes = int(input())
for teste in range(1, quantidade_testes + 1):
    faces = []
    faces = faces + [int(input())]
    faces_meio = input().split()
    faces = faces + [int(i) for i in faces_meio]
    faces = faces + [int(input())]
    if sorted(faces) == [1, 2, 3, 4, 5, 6]:
        if (faces[0] + faces[5] == 7) and (faces[1] + faces[3] == 7) and (faces[2] + faces[4] == 7):
            print('SIM')
        else:
            print('NAO')
    else:
        print('NAO')
