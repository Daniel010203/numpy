def calculator():
    print("Calculadora Simples")
    print("Operações disponíveis: +, -, *, /")
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        operador = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
        
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.")
                return
            resultado = num1 / num2
        else:
            print("Operação inválida.")
            return
        
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Erro: entrada inválida. Certifique-se de digitar números válidos.")

# Executar a calculadora
calculator()