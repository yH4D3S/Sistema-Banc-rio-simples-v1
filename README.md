[README.md](https://github.com/user-attachments/files/22475802/README.md)
# Sistema Bancário Simples v2

## Descrição
Este é um projeto de um sistema bancário simples desenvolvido em Python. A segunda versão deste sistema representa uma evolução significativa da v1, introduzindo modularização através de funções e sistema de cadastro de clientes. O sistema opera via terminal (console) e permite que os usuários realizem operações bancárias fundamentais com uma arquitetura mais organizada e escalável. Projeto proposto pelos professores da DIO.

## Funcionalidades da v2

### Operações Bancárias
- **Depositar**: Permite ao usuário adicionar um valor à sua conta. O sistema valida se o valor inserido é positivo e atualiza o extrato automaticamente.
- **Sacar**: Permite ao usuário retirar um valor da sua conta com validações aprimoradas:
  - Verificação de saldo suficiente
  - Limite máximo de R$ 500,00 por dia
  - Máximo de 3 saques diários
  - Controle de limite diário utilizado
- **Extrato**: Exibe todas as transações (depósitos e saques) realizadas na conta, finalizando com o saldo atual formatado em Real brasileiro.

### Gestão de Clientes
- **Cadastro de Cliente**: Nova funcionalidade que permite:
  - Cadastro de clientes com CPF, nome completo, data de nascimento e endereço
  - Validação de CPF único (não permite CPFs duplicados)
  - Armazenamento em estrutura de dados organizada

### Melhorias Técnicas
- **Modularização**: Código organizado em funções específicas para cada operação
- **Argumentos Posicionais e Nomeados**: Implementação de boas práticas com `/` e `*` para controle de argumentos
- **Validações Aprimoradas**: Sistema robusto de validação de entrada
- **Formatação**: Valores monetários exibidos no padrão brasileiro (vírgula como separador decimal)

## Como Usar

### Pré-requisitos
- Ter o Python 3.x instalado em sua máquina

### Instalação
1. Clone este repositório para o seu ambiente local:
```bash
git clone https://github.com/yH4D3S/sistema-Bancario-simples-v2.git
```

2. Navegue até o diretório do projeto:
```bash
cd sistema-Bancario-simples-v2
```

### Execução
Para iniciar o sistema, execute o seguinte comando no seu terminal:

```bash
python bank_system_v2.py
```

Após a execução, um menu interativo será exibido no console com as seguintes opções:
- **[d]** Depositar
- **[s]** Sacar  
- **[e]** Extrato
- **[c]** Cadastro de Cliente
- **[q]** Sair

## Estrutura do Código

O projeto é composto pelo arquivo principal `bank_system_v2.py`, agora organizado em funções modulares:

### Funções Principais
- `depositar(saldo, extrato, /)`: Gerencia operações de depósito
- `sacar(*, saldo, extrato, limite, numero_saques, limite_usado)`: Gerencia operações de saque
- `mostrar_extrato(saldo, /, *, extrato)`: Exibe o extrato bancário
- `criar_cliente(clientes)`: Gerencia o cadastro de novos clientes

### Variáveis de Controle
- `saldo`: Armazena o valor atual da conta
- `limite`: Define o valor máximo diário para saques (R$ 500,00)
- `limite_usado`: Controla quanto do limite diário já foi utilizado
- `extrato`: String que acumula o histórico de transações
- `numero_saques`: Contador para o número de saques realizados no dia
- `LIMITE_SAQUES`: Constante que define o número máximo de saques diários (3)
- `clientes`: Lista que armazena os dados dos clientes cadastrados

## Novidades da v2

### 🆕 Sistema de Cadastro
- Cadastro completo de clientes com validação de CPF
- Prevenção de cadastros duplicados
- Estrutura de dados organizada para futuras expansões

### 🔧 Melhorias Técnicas
- **Modularização**: Código dividido em funções específicas
- **Argumentos Controlados**: Uso de `/` e `*` para melhor controle de parâmetros
- **Validações Robustas**: Sistema aprimorado de validação de entradas
- **Experiência do Usuário**: Mensagens mais claras e formatação brasileira

### 🎯 Controles Aprimorados
- Limite diário de saque com controle acumulativo
- Validações mais rigorosas para todas as operações
- Mensagens de erro mais específicas e informativas

## Evolução do Projeto

- ✅ **v1**: Funcionalidades básicas em código linear
- ✅ **v2**: Modularização em funções + Sistema de cadastro
- 🚧 **v3**: Múltiplas contas por cliente
- 🔮 **v4**: Implementação com orientação a objetos
- 🔮 **v5**: Persistência de dados com banco de dados

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
