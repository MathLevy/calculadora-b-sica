def calcular(numero1, numero2, operador):
    if operador == '+':
        return numero1 + numero2
    elif operador == '-':
        return numero1 - numero2
    elif operador == '*':
        if (numero1 == -0) or (numero2 == -0):
            return 0
        else:
            return numero1 * numero2
    elif operador == '/':
        if (numero1 != 0) and (numero2 != 0):
            return numero1 / numero2
        else:
            return "Erro: divisão por zero!"
    else:
        return "Operador inválido!"


print("\nDigite o seu cálculo abaixo para obter o resultado. Exemplo: 10 + 50, em seguida aperte a tecla enter.\n")


def main():
    entrada = input()
    partes = entrada.split()
    numero1 = float(partes[0])
    operador = partes[1]
    numero2 = float(partes[2])

    resultado = calcular(numero1, numero2, operador)
    print("-----------")
    print("=", resultado)


if __name__ == "__main__":
    main()

print("\nFIM DO CÁLCULO\n")
