
def vypocet_bmi(kg, vyska_cm):
    vyska_m = vyska_cm / 100

    bmi = vaha / (vyska_m ** 2)

    return bmi

print('BMI')
vaha=float(input('Váha v kg:'))
vyska=float(input('Výška v cm:'))

bmi=vypocet_bmi(vaha, vyska)

print('Vaše bmi je: %f' %bmi)

if bmi < 18.5:
    print('Podváha')
elif 18.5 <= bmi < 24.9:
    print('Normální váha')
elif 25 < bmi <= 29.9:
    print('Nadváha')
else:
    print('Obezita')