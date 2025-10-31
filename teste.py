usuario = []

def cadastrar_usuario(cpf):
    if len(cpf) != 11:
        print("Número de CPF inválido! O CPF deve conter 11 dígitos")
    elif cpf in usuario:
        print("Usuário já cadastrado.")
    else:
        novo_usuario = [cpf, nome, data_nascimento, logradouro, numero, bairro, cidade, sigla_do_estado]
    usuario.append(novo_usuario)
    return usuario([novo_usuario])
    
opcoes = {"1": cadastrar_usuario}

print("""Olá! Seja bem vindo(a)
Selecione a opção desejada:
[1] Cadastrar usuário
[2] Cadastrar conta
[3] Saque
[4] Depósito
[5] Extrato\n""")

opcao_selecionada = input()
opcoes[opcao_selecionada]()

print("Por favor, preencha os dados para o cadastro:\n")
cpf = input("CPF (somente números): \n")
nome = input("Nome completo: \n")
data_nascimento = input("Data de nascimento (DD/MM/AAAA): \n")
logrado = input("Logradouro: \n")
numero= input("Número: \n")
bairro = input("Bairro: \n")
cidade = input("Cidade: \n")
sigla_do_estado = input("Sigla do estado (UF): \n")

cadastrar_usuario(cpf).novo_usuario(cpf = cpf, nome = nome, data_nascimento = data_nascimento, logrado = logrado, numero = numero, 
                  bairro = bairro, cidade = cidade, sigla_do_estado = sigla_do_estado)


# Exemplo de como chamar a função
# novo_usuario = cadastrar_usuario()
# print("\nUsuário Cadastrado:", novo_usuario)
