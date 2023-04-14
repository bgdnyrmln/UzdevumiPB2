"""10.16. Uzrakstīt programmu, kas lietotājam liek ievadīt virknes garumu n un tās locekļus - veselus skaitļus - un parāda uz ekrāna šādu informāciju: 
1) pats masīvs; 
2) paziņojums par to, kādu skaitļu masīvā ir vairāk - pozitīvu vai negatīvu; 
3) paziņojums par to, kādu skaitļu masīvā ir vairāk - divciparu vai trīsciparu; 
4) paziņojums par to, kādu skaitļu masīvā ir vairāk - lielāku vai mazāku par pēdējo masīva elementu."""

m = []
x = int(input("Ievadiet masiva garumu = "))
poz = 0
dc = 0
tc = 0
mp = 0
for i in range(x):
    m.append(int(input("Ievadiet " + str(i) + " elemetna nozimi = ")))
    if m[i] > 0:
        poz += 1
    if m[i]/10 > 1 and m[i]/10 < 10:
        dc += 1
    if m[i]/-10 > 1 and m[i]/-10 < 10:
        dc += 1
    if m[i]/100 > 1 and m[i]/100 < 10:
        tc += 1
    if m[i]/-100 > 1 and m[i]/-100 < 10:
        tc += 1
for i in range(x):
    print(m[i], end = "\t")
for i in range(x):
    if m[i] < m[x-1]:
        mp += 1
print()
if poz > x/2:
    print("Vairakie elementi ir pozitivi")
else:
    print("Vairakie elementi ir negativi")
if dc > tc:
    print("Vairak ir divciparu elementu neka trisciparu")
elif tc > dc:
    print("Vairak ir trisciparu elementu neka divciparu")
else:
    print("Trisciparu skaitlu ir tik pat daudz cik divciparu")
if mp < x/2:
    print("Vairak ir elementu kas ir lielaki par pedejo elementu")
else:
    print("Vairak ir elementu kas ir mazaki par pedejo elementu")