Cv, Ce, Cs, Fv, Fe, Fs = input().split()
Cv = int(Cv)
Ce = int(Ce)
Cs = int(Cs)
Fv = int(Fv)
Fe = int(Fe)
Fs = int(Fs)
Pc = 3*Cv + Ce
Pf = 3*Fv + Fe
if Pc > Pf:
    print('C')
elif Pf > Pc:
    print('F')
else:
    if Cs > Fs:
        print('C')
    elif Fs > Cs:
        print('F')
    else:
        print('=')
