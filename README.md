# Sistema Bancário Simples v3

## Descrição
Este é um projeto de um sistema bancário simples desenvolvido em Python. A terceira versão deste sistema representa uma evolução significativa das versões anteriores, introduzindo modularização através de funções, sistema de cadastro de clientes e **sistema completo de contas correntes**. O sistema opera via terminal (console) e permite que os usuários realizem operações bancárias fundamentais com uma arquitetura mais organizada e escalável. Projeto proposto pelos professores da DIO.

## Funcionalidades da v3

### Operações Bancárias
- **Depositar**: Permite ao usuário adicionar um valor à sua conta. O sistema valida se o valor inserido é positivo e atualiza o extrato automaticamente.
- **Sacar**: Permite ao usuário retirar um valor da sua conta com validações aprimoradas:
  - Verificação de saldo suficiente
  - Limite máximo de R$ 500,00 por dia
  - Máximo de 3 saques diários
  - Controle de limite diário utilizado
- **Extrato**: Exibe todas as transações (depósitos e saques) realizadas na conta, finalizando com o saldo atual formatado em Real brasileiro.

### Gestão de Clientes
- **Cadastro de Cliente**: Funcionalidade que permite:
  - Cadastro de clientes com CPF, nome completo, data de nascimento e endereço
  - Validação de CPF único (não permite CPFs duplicados)
  - Armazenamento em estrutura de dados organizada

### 🆕 Sistema de Contas Correntes
- **Criação de Contas**: Nova funcionalidade que permite:
  - Criação de contas correntes vinculadas a clientes existentes
  - Numeração sequencial automática (começando em 1)
  - Agência fixa: "0001"
  - Vinculação por CPF do cliente
  - Saldo e extrato individuais para cada conta
  - Um cliente pode ter múltiplas contas
  - Uma conta pertence a apenas um cliente

### Melhorias Técnicas
- **Modularização**: Código organizado em funções específicas para cada operação
- **Argumentos Posicionais e Nomeados**: Implementação de boas práticas com `/` e `*` para controle de argumentos
- **Validações Aprimoradas**: Sistema robusto de validação de entrada com técnica de flag (cliente_encontrado)
- **Formatação**: Valores monetários exibidos no padrão brasileiro (vírgula como separador decimal)
- **Controle de Estado**: Gerenciamento adequado de múltiplas estruturas de dados

## Como Usar

### Pré-requisitos
- Ter o Python 3.x instalado em sua máquina

### Instalação
1. Clone este repositório para o seu ambiente local:
```bash
git clone https://github.com/yH4D3S/sistema-Bancario.git
```

2. Navegue até o diretório do projeto:
```bash
cd sistema-Bancario
```

### Execução
Para iniciar o sistema, execute o seguinte comando no seu terminal:

```bash
python bank_system_v3.py
```

Após a execução, um menu interativo será exibido no console com as seguintes opções:
- **[d]** Depositar
- **[s]** Sacar  
- **[e]** Extrato
- **[c]** Cadastro de Cliente
- **[cc]** Cadastrar Conta
- **[q]** Sair

## Fluxo de Uso Recomendado
1. **Primeiro**: Cadastre um cliente usando a opção [c]
2. **Segundo**: Crie uma conta para esse cliente usando a opção [cc]
3. **Depois**: Realize operações bancárias (depositar, sacar, extrato)

## Estrutura do Código

O projeto é composto pelo arquivo principal `bank_system_v3.py`, agora organizado em funções modulares:

### Funções Principais
- `depositar(saldo, extrato, /)`: Gerencia operações de depósito
- `sacar(*, saldo, extrato, limite, numero_saques, limite_usado)`: Gerencia operações de saque
- `mostrar_extrato(saldo, /, *, extrato)`: Exibe o extrato bancário
- `criar_cliente(clientes)`: Gerencia o cadastro de novos clientes
- `criar_conta(clientes, contas, numero_conta_atual)`: **NOVA** - Gerencia a criação de contas correntes

### Variáveis de Controle
- `saldo`: Armazena o valor atual da conta (versão global - em evolução)
- `limite`: Define o valor máximo diário para saques (R$ 500,00)
- `limite_usado`: Controla quanto do limite diário já foi utilizado
- `extrato`: String que acumula o histórico de transações (versão global - em evolução)
- `numero_saques`: Contador para o número de saques realizados no dia
- `LIMITE_SAQUES`: Constante que define o número máximo de saques diários (3)
- `clientes`: Lista que armazena os dados dos clientes cadastrados
- **`contas`**: **NOVA** - Lista que armazena as contas correntes criadas
- **`numero_conta_atual`**: **NOVA** - Controla a numeração sequencial das contas

### Estrutura de Dados

#### Cliente
```python
cliente = {
    "cpf": "12345678900",
    "nome": "Nome Completo",
    "endereco": "Rua X - 123 - Bairro - Cidade / UF",
    "data_nascimento": "01/01/1990"
}
```

#### Conta Corrente
```python
conta = {
    "cpf": "12345678900",           # Vincula ao cliente
    "numero da conta": 1,           # Sequencial automático
    "agência": "0001",              # Fixo
    "saldo": 0,                     # Inicia zerado
    "extrato": ""                   # Inicia vazio
}
```

## Novidades da v3

### 🆕 Sistema de Contas Correntes
- Criação de contas vinculadas a clientes existentes
- Numeração sequencial automática
- Saldo e extrato individuais por conta
- Validação de cliente existente antes da criação

### 🔧 Melhorias Técnicas Avançadas
- **Algoritmo de Busca**: Implementação de busca por CPF com técnica de flag
- **Controle de Estado**: Gerenciamento simultâneo de clientes e contas
- **Validação Robusta**: Sistema que previne criação de contas para clientes inexistentes
- **Numeração Automática**: Sistema de incremento automático para números de conta

### 🎯 Controles Implementados
- Prevenção de contas órfãs (sem cliente vinculado)
- Controle de numeração sequencial
- Validação de existência de cliente
- Retorno adequado de múltiplas variáveis modificadas

## Melhorias Pendentes (Próximas Versões)

### 🚧 Integrações Necessárias
- Adaptar funções `depositar()`, `sacar()` e `mostrar_extrato()` para trabalhar com contas específicas
- Implementar seleção de conta para operações
- Migrar de saldo/extrato globais para individuais por conta

### 🔮 Evoluções Futuras
- Sistema de login por conta
- Listagem de contas por cliente
- Transferências entre contas
- Histórico detalhado por conta

## Evolução do Projeto

- ✅ **v1**: Funcionalidades básicas em código linear
- ✅ **v2**: Modularização em funções + Sistema de cadastro de clientes
- ✅ **v3**: **Sistema completo de contas correntes** + Validações avançadas
- 🚧 **v4**: Integração completa conta-operações + Interface melhorada
- 🔮 **v5**: Implementação com orientação a objetos
- 🔮 **v6**: Persistência de dados com banco de dados

## Aprendizados Técnicos Implementados

### Conceitos Aplicados
- **Estruturas de Dados**: Listas e dicionários aninhados
- **Controle de Fluxo**: Loops, condicionais e flags
- **Modularização**: Funções com responsabilidades específicas
- **Validação de Dados**: Verificação de existência e integridade
- **Debugging**: Identificação e correção de problemas lógicos

### Técnicas de Programação
- Uso de flags para controle de estado (`cliente_encontrado`)
- Retorno múltiplo de valores em funções
- Busca em estruturas de dados complexas
- Incremento automático de contadores
- Validação de integridade referencial (CPF existe?)

## Contribuição
Contribuições são bem-vindas! Se você tiver sugestões para melhorar este projeto, sinta-se à vontade para:
1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## Licença
Este projeto é desenvolvido para fins educacionais como parte do curso da DIO.

## Autor
**Izaac "H4D3S" Emanoel**

- GitHub: [@yH4D3S](https://github.com/yH4D3S)
- Projeto DIO: Sistema Bancário Python

---
*Desenvolvido com 💻 e ☕ para aprendizado em Python*
*v3 - Agora com sistema completo de contas correntes!*
