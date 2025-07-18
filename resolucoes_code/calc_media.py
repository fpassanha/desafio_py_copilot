# Agora vamos calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

# Solicita as três notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Verifica se foi aprovado ou não
if media >= 7:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

# Exibe o resultado
print(f"Média: {media:.2f} - {resultado}")