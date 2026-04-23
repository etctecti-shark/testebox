def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não permitida!"
    return a / b

def main():
    print("=== Calculadora Básica ===")
    print("Operações disponíveis:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Sair")

    while True:
        print("\n" + "="*30)

        try:
            escolha = input("Escolha uma operação (1-5): ")

            if escolha == '5':
                print("Obrigado por usar a calculadora! Até logo!")
                break

            if escolha in ('1', '2', '3', '4'):
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if escolha == '1':
                    resultado = adicionar(num1, num2)
                    print(f"{num1} + {num2} = {resultado}")
                elif escolha == '2':
                    resultado = subtrair(num1, num2)
                    print(f"{num1} - {num2} = {resultado}")
                elif escolha == '3':
                    resultado = multiplicar(num1, num2)
                    print(f"{num1} * {num2} = {resultado}")
                elif escolha == '4':
                    resultado = dividir(num1, num2)
                    print(f"{num1} / {num2} = {resultado}")
            else:
                print("Opção inválida! Por favor, escolha um número entre 1 e 5.")

        except ValueError:
            print("Erro: Por favor, digite números válidos!")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()