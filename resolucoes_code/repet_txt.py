# Solicita uma string e um número inteiro, e exibe uma tabela com cada repetição em uma coluna

texto = input("Digite uma string: ")
vezes = int(input("Digite um número inteiro: "))

# Monta a linha da tabela com cada dado em uma coluna
linha = "| " + " | ".join([texto] * vezes) + " |"

# Monta a linha de separação
separador = "+"+ "+".join(["-" * (len(texto) + 2)] * vezes) + "+"

# Exibe a tabela
print(separador)
print(linha)
print(separador)

