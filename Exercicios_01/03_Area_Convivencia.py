#Versão Original
raio = float(input("Informe o raio do círculo (em metros):"))
area = 3.14*(raio**2)
print(f"A área de convivência é de {area} metros")

#Versão com importação do π(pi)
from math import pi
raio = float(input("Informe o raio do círculo (em metros):"))
area = pi*(raio**2)
print(f"A área de convivência é de {area:.2f} metros")