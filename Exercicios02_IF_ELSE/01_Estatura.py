altura1 = float(input("Informe a altura da primeira pessoa:"))
altura2 = float(input("Informe a altura da segunda pessoa:"))
altura3 = float(input("Informe a altura da terceira pessoa:"))
if altura1 > altura2 and altura1 > altura3:
    print(altura1)
    if altura2 > altura3:
        print(altura2)
        print(altura3)
    else:
        print(altura3)
        print(altura2)
elif altura2 > altura1 and altura2 > altura3:
    print(altura2)
    if altura1 > altura3:
        print(altura1)
        print(altura3)
    else:
        print(altura3)
        print(altura1)
elif altura3 > altura1 and altura3 > altura2:
    print(altura3)
    if altura1 > altura2:
        print(altura1)
        print(altura2)
    else:
        print(altura2)
        print(altura1)
else:
    print(altura1)
    print(altura2)
    print(altura3)