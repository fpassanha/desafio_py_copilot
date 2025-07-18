#Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. A saída será exibida em verde.

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    resultado = "par"
else:
    resultado = "ímpar"

# Código ANSI para cor verde
verde = "\033[32m"
reset = "\033[0m"

print(f"{verde}O número {numero} é {resultado}.{reset}")

