def menu():
    menu = input("""\n
    ================ MENU ================
    [1] Cadastrar usuário
    [2] Criar conta
    [3] Sacar
    [4] Depositar
    [5] Extrato
    [6] Listar contas
    [0] Sair\n
    => """)

    return menu

def cadastrar_usuario(usuarios):
    print("Por favor, preencha os dados para o cadastro:\n")
    cpf = input("Digite os números do seu CPF (sem ponto e/ou traço): \n")
    usuario = validar_usuario(cpf, usuarios)
    if usuario:
        print("\nUsuário já cadastrado!\n")
        return


    nome = input("Nome completo: \n")  
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): \n")
    endereco = input("Infome seu endereço contendo (rua/avenida, número, bairro, cidade e sigla do estado: \n")
    usuario = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
        }
    usuarios.append(usuario)
    print("\nUsuário cadastrado com sucesso!\n")
    
def validar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if len(cpf) != 11:
            print("\nCPF inválido! O CPF deve conter 11 dígitos.\n")
        
        elif usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário:\n")
    usuario = validar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!\n")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
    print("\nUsuário não encontrado, por favor realize o cadastro.\n")    

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor > saldo:
        print("\nOperação falhou! Saldo insuficiente.\n")
    elif valor > limite:
        print("\nOperação falhou! O valor do saque excede o limite.\n")
    elif numero_saques >= LIMITE_SAQUES:
        print("\nOperação falhou! Número máximo de saques excedido.\n")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!\n")
    else:
        print("\nOperação falhou! O valor informado é inválido.\n")
    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("\nDepósito realizado com sucesso!\n")
    else:
        print("\nOperação falhou! O valor informado é inválido.\n")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================\n")

def sair():
    print("Obrigado por utilizar nossos serviços.")

def main():
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            cadastrar_usuario(usuarios)
        
        elif opcao == "2":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta: 
                contas.append(conta)

        elif opcao == "3":
            valor = float(input("Informe o valor do saque: \n"))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques
            )

        elif opcao == "4":
            valor = float(input("Informe o valor do depósito: \n"))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "5":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            sair()
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()



# Exemplo de como chamar a função
# novo_usuario = cadastrar_usuario()
# print("\nUsuário Cadastrado:", novo_usuario)
