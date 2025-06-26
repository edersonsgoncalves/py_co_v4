# Banco CO - Sistema Bancário v2.0
Bem-vindo ao repositório do Banco CO - v2.0, uma aplicação de sistema bancário simples desenvolvida em Python com funcionalidades de gerenciamento de clientes, contas, depósito, saque e extrato. Este projeto é um exercício proposto pela **DIO.me** e representa uma evolução em relação à sua primeira versão (https://github.com/edersonsgoncalves/py_co), incorporando o conceito de funções e escopo para uma organização de código mais eficiente, modular e organizada além de acrescentar novas funcionalidades.

## 🚀 **Funcionalidades**
O sistema oferece um menu interativo com as seguintes operações:

- **Gerenciamento de Clientes:**
    - **Novo Cliente `[c]`**: Permite o cadastro de novos clientes com CPF (com validação de 11 dígitos numéricos), nome (apenas letras) e data de nascimento (DDMMAAAA). Inclui validação para CPF duplicado e coleta de endereço completo.
        
    - **Listar Clientes `[m]`**: Exibe todos os clientes cadastrados com suas informações formatadas.
        
- **Gerenciamento de Contas:**
    - **Nova Conta `[n]`**: Permite criar uma nova conta bancária, associando-a a um cliente existente (buscado pelo CPF). Cada conta recebe um número de agência padrão (`0001`) e um número de conta sequencial. As contas são independentes e possuem seus próprios saldo, extrato e limites.
        
    - **Listar Contas `[l]`**: Apresenta uma lista de todas as contas criadas, incluindo a agência, o número da conta, o nome do cliente associado e o saldo atual.
        
- **Operações Bancárias:**
    - **Depositar `[d]`**: Permite ao usuário depositar valores em uma conta específica. O sistema valida se o valor é positivo e atualiza o saldo e o extrato da conta selecionada.
        
    - **Sacar `[s]`**: Permite ao usuário sacar valores de uma conta específica, com as seguintes validações:
        
        - Verifica se há **saldo suficiente** na conta.
        - Verifica se o valor do saque excede o **limite por operação (R$ 500)**.
        - Verifica se o **limite diário de 3 saques** por conta foi atingido.
            
    - **Extrato `[e]`**: Exibe o histórico detalhado de todas as transações (depósitos e saques) realizadas em uma conta específica, além do saldo atual da conta.
        
- **Sair `[q]`**: Encerra o sistema bancário.

## 💼 **Regras de Negócio Implementadas**
Este sistema simula algumas regras de negócio essenciais para operações bancárias:

- **Saldo Inicial da Conta**: Cada nova conta inicia com saldo zero.
- **Limite de Saque por Operação**: Cada saque individual não pode exceder R$ 500.
- **Limite Diário de Saques**: Cada conta pode realizar no máximo 3 saques por dia.
- **Valores Positivos**: Depósitos e saques devem ser de valores estritamente positivos.
- **Saldo Suficiente**: Não é possível sacar um valor maior do que o saldo disponível na conta.
- **CPF Único para Cliente**: Um CPF não pode ser cadastrado mais de uma vez como cliente.
- **Associação de Conta**: Contas são criadas e associadas a um cliente já existente.

## 🛠️ **Como Usar**
Para executar este sistema bancário em seu ambiente local, siga os passos abaixo:

### 1. Pré-requisitos
   - Certifique-se de ter o **Python 3** (ou versão superior) instalado em sua máquina. Você pode baixá-lo em [python.org](https://www.python.org/).
        
### 2. Obtenha o Código
   - **Clone o Repositório:** Abra seu terminal ou prompt de comando e clone o repositório principal:
        
        ```
        git clone https://github.com/edersonsgoncalves/py_co_v2
        cd py_co_v2
        ```
        
### 3. Execute o Script Python
   - Com o terminal aberto no diretório `py_co_v2`, execute o seguinte comando:

        ```
        python py_co_v2.py
        ```
        
### 4. Interaja com o Menu
   - O sistema exibirá o menu principal. Digite a letra correspondente à opção desejada e pressione `Enter`. As instruções aparecerão na tela para guiar você pelas operações.

## 💡 **Observações de Desenvolvimento**
- Este projeto foi concebido para fins **didáticos**, focado na aplicação de conceitos de programação em Python, e **não deve ser utilizado para transações financeiras reais**.
- Todas as informações (clientes, contas, saldos, extratos) são **voláteis** e armazenadas em memória RAM. Os dados **não são persistidos** após o fechamento do programa.
- A **validação de entrada** de dados (CPF, nome, data, valores de depósito/saque) foi pensada para assegurar uma qualidade mínima dos dados inseridos pelo usuário. Contudo, não é feita validação da veracidade do dado, ou seja, no CPF, números como 11111111111 serão aceitos.
- A principal evolução desta versão é a adoção de uma estrutura com **funções bem definidas e a exploração do escopo de variáveis**, permitindo o gerenciamento independente de múltiplos clientes e suas respectivas contas, um grande avanço em relação à versão 1.

## 🤝 **Como Contribuir**
Contribuições são bem-vindas! Se você deseja aprimorar este projeto ou praticar suas habilidades em Python, considere:
- Abrir "Issues" para relatar bugs ou sugerir novas funcionalidades.
- Fazer um "Fork" do projeto e enviar "Pull Requests" com suas implementações, como:
    - Implementar persistência de dados (salvar/carregar dados de arquivos como CSV, JSON ou banco de dados).
    - Adicionar funcionalidades de atualização ou exclusão de clientes/contas.
    - Melhorar a interface do usuário ou adicionar mais validações.
    - Refatorar o código para uma abordagem orientada a objetos.

## **Licença**
Este projeto está sob a licença **MIT**.
