while True:
    """
    Solicita ao usuário que escolha uma operação
    """
    operacao = input("""Informe uma das operações a seguir:
                     1 - Somar números
                     2 - Subtrair números
                     3 - Multiplicar números
                     4 - Dividir números
Operação: """)

    if operacao == "1":
        """
        No caso da operação ser soma, inicializa o resultado como 0
        """
        result = 0
        while True:
            """
            Solicita um número ao usuário ou 'P' para parar
            """
            n = input("Digite um número ou 'P' para parar: ")
            if n.upper() == "P":
                break
            """
            Adiciona o número ao resultado (convertido para inteiro)
            """
            result += int(n)
        """
        Imprime o resultado da soma
        """
        print("Resultado da soma:", result)
    elif operacao == "2":
        """
        No caso da operação ser subtração, inicializa o resultado como None
        """
        result = None
        while True:
            """
            Solicita um número ao usuário ou 'P' para parar
            """
            n = input("Digite um número ou 'P' para parar: ")
            if n.upper() == "P":
                break
            if result is None:
                """
                Se for o primeiro número, define o resultado como esse número
                """
                result = int(n)
            else:
                """
                Do contrário, subtrai o número do resultado
                """
                result -= int(n)
        """
        Imprime o resultado da subtração
        """
        print("Resultado da subtração:", result)
    elif operacao == "3":
        """
        No caso da operação ser multiplicação, inicializa o resultado como 1
        """
        result = 1
        while True:
            """
            Solicita um número ao usuário ou 'P' para parar
            """
            n = input("Digite um número ou 'P' para parar: ")
            if n.upper() == "P":
                break
            """
            Multiplica o número ao resultado
            """
            result *= int(n)
        """
        Imprime o resultado da multiplicação
        """
        print("Resultado da multiplicação:", result)
    elif operacao == "4":
        """
        Se a operação for divisão, inicializa o resultado como None
        """
        result = None
        while True:
            """
            Solicita um número ao usuário ou 'P' para parar
            """
            n = input("Digite um número ou 'P' para parar: ")
            if n.upper() == "P":
                break
            if result is None:
                """
                Se for o primeiro número, define o resultado como esse número
                """
                result = int(n)
            else:
                """
                Caso contrário, divide o resultado pelo número
                """
                result /= int(n)
        """
        Imprime o resultado da divisão
        """
        print("Resultado da divisão:", result)
    else:
        """
        Caso a operação for inválida, exibira uma mensagem de erro
        """
        print("Operação inválida. Escolha uma operação válida (1, 2, 3 ou 4).")