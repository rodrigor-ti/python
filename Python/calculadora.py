# Calculadora simples usando eval() e input()defcalculadora():
    print("Bem-vindo à calculadora!")
    print("Digite uma expressão matemática para calcular ou 'sair' para terminar.")
    
    whileTrue:
        # Solicita ao usuário que insira uma expressão matemática
        expressao = input("Digite a expressão: ")
        
        # Verifica se o usuário quer sairif expressao.lower() == 'sair':
            print("Encerrando a calculadora. Até logo!")
            breaktry:
            # Avalia a expressão usando eval()
            resultado = eval(expressao)
            print(f"Resultado: {resultado}")
        
        except Exception as e:
            # Captura erros, caso a expressão seja inválidaprint(f"Erro na expressão: {e}")

# Executa a calculadora
calculadora()