nome_banco = "Banco CO - v.2.0".center(32,"-")
boas_vindas = "Seja Bem Vind@!".center(32)

menu = f"""
{nome_banco}
{boas_vindas}
Selecione uma das opções abaixo:

    -----Clientes-----
    [c] Novo Cliente
    [m] Listar Clientes
    -----Contas-----
    [n] Nova Conta
    [l] Listar Contas
    -----Operações-----
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> """

clientes = []
contas=[]
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def cliente_novo (clientes):
    cliente_cpf = valida_dado (valida_cpf, "Insira o CPF (somente números, 11 dígitos): ")
    valida_cliente = filtrar_cliente(cliente_cpf,clientes)

    if valida_cliente:
        print ("Cliente já cadastrado")
        input("Pressione Enter para voltar ao menu inicial...") 
        return
    cliente_nome = valida_dado (valida_nome, "Insira o nome do cliente: ")
    cliente_data_nascimento = valida_dado (valida_data_nascimento, "Insira a Data de Nascimento no formato DDMMAAAA: ")

    cliente_rua = input("Insira o logradouro: ").strip()
    cliente_nro = input("Insira o número da residência: ").strip()
    cliente_bairro = input("Insira o Bairro: ").strip()
    cliente_cidade = input("Insira a Cidade: ").strip()
    cliente_estado = input("Insira a sigla do Estado (XX): ").strip()

    if cliente_rua and cliente_nro and cliente_bairro and cliente_cidade and cliente_estado:
        endereco_completo = cliente_rua+", "+cliente_nro+" - "+cliente_bairro+" - "+cliente_cidade+"/"+cliente_estado
    else:
        endereco_completo = ""

    if cliente_cpf and cliente_data_nascimento and cliente_nome:
        clientes.append({"nome": cliente_nome,"data_nascimento": cliente_data_nascimento,"cpf": cliente_cpf, "endereco":endereco_completo, "senha":"123"})
        input("Cliente cadastrado com sucesso!\nPressione enter para retornar...")

def cliente_listar(clientes):
    if not clientes:
        print ("Nenhum cliente cadastrado")

    for cliente in clientes:
        cliente_data_nascimento = cliente["data_nascimento"][0:2]+"/"+cliente["data_nascimento"][2:4]+"/"+cliente["data_nascimento"][4:]
        print (f"""
CPF: {cliente["cpf"]}
Cliente: {cliente["nome"].capitalize()}
Data Nascimento: {cliente_data_nascimento}
Endereço: {cliente["endereco"]}
""")
    input("Pressione Enter para voltar ao menu inicial...") 

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def valida_cpf (cpf):
    cpf = cpf.strip()
    return cpf.isdigit() and len(cpf) == 11

def valida_nome (nome):
    nome = nome.strip()
    return nome.isalpha() and len(nome) >= 3

def valida_data_nascimento (dt_nas):
    data_nascimento = dt_nas.strip()
    return data_nascimento.isdigit() and len(data_nascimento) == 8

def valida_dado (funcao, texto, mensagem_erro="Entrada inválida. Por favor, tente novamente."):
    while True:
        dado = input(texto)
        if funcao(dado):
            return dado 
        else:
            print(mensagem_erro)

def conta_criar (contas, clientes):
    total_contas = len(contas)
    agencia = "1"
    nova_conta = total_contas+1
    nova_conta_formatada = f"{nova_conta:04d}"
    saldo = 0
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        cliente_cpf = input("Insira o CPF do cliente associado a conta: ")
        valida_cliente = filtrar_cliente(cliente_cpf,clientes)
 
        if valida_cliente:
            confirmacao = input(f"Você selecionou o cliente ({valida_cliente["nome"].capitalize()}).\nIsso está correto? (s/n): ").lower()
            if confirmacao == 's':
                contas.append({
                    "agencia": agencia.zfill(4),
                    "conta": nova_conta_formatada, 
                    "cliente": cliente_cpf, 
                    "saldo": saldo, 
                    "extrato": extrato, 
                    "limite_saque": limite, 
                    "numero_saques": numero_saques,
                    "limite_saques": LIMITE_SAQUES})
                break
        else :
            input ("Cliente não localizado.\nVerifique a lista de contas.\n\nPressione enter para retornar")
            break

def conta_listar(contas, clientes):
    if not contas:
        print ("Nenhuma conta cadastrada")
        input("Pressione Enter para voltar ao menu inicial...") 
        return
    
    for conta in contas:
        cliente_atralado_conta = filtrar_cliente(conta["cliente"],clientes)
        print (f"""
Agência: {conta["agencia"]}               
Conta: {conta["conta"]}
Cliente: {cliente_atralado_conta["nome"].capitalize()}
Saldo: R${conta["saldo"]:.2f}
""")
    input("Pressione Enter para voltar ao menu inicial...") 

def depositar (saldo, valor, extrato, cliente_conta, contas):
    conta_encontrada = False
    for conta_selecionada in contas:
        if conta_selecionada['conta'] == cliente_conta:
            conta_encontrada = True
            if valor > 0:
                conta_selecionada['saldo'] += valor
                saldo += valor
                conta_selecionada['extrato'] += f"Depósito: R$ {valor:.2f}\n"
                extrato += f"Depósito: R$ {valor:.2f}\n"
                input ("Depósito realizado com sucesso.\nPressione enter para retornar")
                return

            else:
                input("Operação falhou! O valor informado é inválido.\n\nPressione enter para retornar")

                break

    if not conta_encontrada:
        input("\n\nConta não cadastrada.\nPressione enter para retornar")

def saque (contas, /, *, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES, cliente_conta):
    conta_encontrada = False
    for conta_selecionada in contas:
        if conta_selecionada['conta'] == cliente_conta:
            conta_encontrada = True
            if valor > 0:
                excedeu_saldo = valor > conta_selecionada['saldo']
                excedeu_limite = valor > conta_selecionada['limite_saque']
                excedeu_saques = conta_selecionada['numero_saques'] >= conta_selecionada['limite_saques']

                if excedeu_saldo:
                    input("Operação falhou! Você não tem saldo suficiente.\nPressione enter para retornar")

                elif excedeu_limite:
                    input("Operação falhou! O valor do saque excede o limite por operação.\nPressione enter para retornar")

                elif excedeu_saques:
                    input("Operação falhou! Número máximo de saques excedido.\nPressione enter para retornar")

                else:
                    conta_selecionada['saldo'] -= valor
                    saldo -= valor
                    conta_selecionada['extrato'] += f"Saque: R$ {valor:.2f}\n"
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    conta_selecionada['numero_saques'] += 1
                    numero_saques += 1
                    input ("Saque realizado com sucesso.\nPressione enter para retornar")
                    return

            else:
                print("Operação falhou! O valor informado é inválido.")
                break
    if not conta_encontrada:
        input("\n\nConta não cadastrada.\nPressione enter para retornar")

def extrato_exibir (saldo, /,*, extrato, contas, cliente_conta):
    conta_encontrada = False
    print("\n================ EXTRATO ================")
    for conta_selecionada in contas:
        if conta_selecionada['conta'] == cliente_conta:
            conta_encontrada = True
            print("Não foram realizadas movimentações." if not conta_selecionada['extrato'] else conta_selecionada['extrato'])
            print(f"\nSaldo: R$ {conta_selecionada['saldo']:.2f}")
            print("==========================================")

            input("Pressione enter para retornar..")

    if not conta_encontrada:
        input("Não foram realizadas movimentações.\nPressione enter para retornar")


while True:
    opcao = input(menu)

    if opcao == "c":
        cliente_novo(clientes)

    elif opcao == "m":
        cliente_listar(clientes)

    elif opcao == "n":
        conta_criar (contas, clientes)

    elif opcao == "l":
        conta_listar (contas, clientes)

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        cliente_conta = input("Insira a conta na qual deseja depositar: ").zfill(4)

        depositar(saldo, valor, extrato, cliente_conta, contas)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        cliente_conta = input("Insira a conta na qual deseja sacar: ").zfill(4)
        saque (contas, saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, LIMITE_SAQUES = LIMITE_SAQUES, cliente_conta = cliente_conta)

    elif opcao == "e":
        cliente_conta = input("Insira a conta que você deseja ver o extrato: ").zfill(4)
        extrato_exibir (saldo, extrato=extrato, contas=contas, cliente_conta=cliente_conta)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")