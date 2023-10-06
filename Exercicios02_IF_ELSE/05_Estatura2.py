altura1 = float(input("Informe a estatura da primeira pessoa:"))
altura2 = float(input("Informe a estatura da segunda pessoa:"))
altura3 = float(input("Informe a estatura da terceira pessoa:"))

if (altura1 == altura2) or (altura1 == altura3) :
    print("Há, pelo menos, 2 pessoas com a mesma estatura")
elif altura1 > altura2 and altura1 > altura3:
    print(f"A maior altura é {altura1}")
elif altura2 > altura1 and altura2 > altura3:
    print(f"A maior altura é {altura2}")
elif altura3 > altura1 and altura3 > altura2:
    print(f"A maior altura é {altura3}")