def calcular_tensao(corrente, resistencia):
    return corrente * resistencia

def calcular_resistencia(tensao, corrente):
    return tensao / corrente

def calcular_corrente(tensao, resistencia):
    return tensao / resistencia

opcao = input("Escolha a grandeza que deseja calcular (T para Tensão, R para Resistência, C para Corrente): ").strip().upper()

if opcao == "T":
    corrente = float(input("Informe a corrente (em Amperes): "))
    resistencia = float(input("Informe a resistência (em Ohms): "))
    tensao = calcular_tensao(corrente, resistencia)
    print(f"A Tensão é {tensao} Volts.")
elif opcao == "R":
    tensao = float(input("Informe a tensão (em Volts): "))
    corrente = float(input("Informe a corrente (em Amperes): "))
    resistencia = calcular_resistencia(tensao, corrente)
    print(f"A Resistência é {resistencia} Ohms.")
elif opcao == "C":
    tensao = float(input("Informe a tensão (em Volts): "))
    resistencia = float(input("Informe a resistência (em Ohms): "))
    corrente = calcular_corrente(tensao, resistencia)
    print(f"A Corrente é {corrente} Amperes.")
else:
    print("Opção inválida. Por favor, escolha T, R ou C.")
