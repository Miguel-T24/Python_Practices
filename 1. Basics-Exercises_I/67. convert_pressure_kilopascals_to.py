# 67. Write python proram to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.

kilopascal = float(input("Enter kilopascal pressure: "))
psi = kilopascal / 6.89475729
mmHg = kilopascal * 760 / 101.325
atmosphere = kilopascal / 101.325

print("PSI {:.2f}\nmmHg {:.2f}\nAtmosphere {:.2f}".format(psi,mmHg, atmosphere))

