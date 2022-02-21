nota1, nota2, nota3, nota4 = input().split()
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)
media_sem_round = (nota1*2 + nota2*3 + nota3*4 + nota4) / 10
media = round(media_sem_round, 1)
if media >= 7:
    print('Media: %.1f' % media)
    print('Aluno aprovado.')
elif media >= 5:
    print('Media: %.1f' % media)
    print('Aluno em exame.')
    nota_exame = float(input())
    print('Nota do exame: %.1f' % nota_exame)
    media_final = (media_sem_round + nota_exame) / 2
    media_final = round(media_final, 1)
    if media_final >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f' % media_final)
else:
    print('Media: %.1f' % media)
    print('Aluno reprovado.')
