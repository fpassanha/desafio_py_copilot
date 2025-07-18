# Vamos solicitar como entrada dois numeros e depois vamos realizar uma operacao matematica simples entre eles.
# O resultado da operacao sera impresso na tela.

def operacao_matematica():
    # Solicita ao usuario o primeiro numero
    num1 = float(input("Digite o primeiro numero: "))
    
    # Solicita ao usuario a operação desejada
    operacao = input("Digite a operação (+, -, *, /): ")

    # Solicita ao usuario o segundo numero
    num2 = float(input("Digite o segundo numero: "))
    
    # Realiza a operação escolhida
    if operacao == "+":
        resultado = num1 + num2
        op_nome = "adição"
    elif operacao == "-":
        resultado = num1 - num2
        op_nome = "subtração"
    elif operacao == "*":
        resultado = num1 * num2
        op_nome = "multiplicação"
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
            op_nome = "divisão"
        else:
            print("Erro: divisão por zero.")
            return
    else:
        print("Operação inválida.")
        return
    
    # Imprime o resultado na tela
    print(f"O resultado da {op_nome} entre {num1} e {num2} é: {resultado}")

# Chama a funcao para executar a operacao
operacao_matematica()
# resolucoes_code/ope_mat.py
# Fim do codigo
