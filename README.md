# Sistema Bancário Simples v1

## Descrição

Este é um projeto de um sistema bancário simples desenvolvido em Python. A primeira versão deste sistema opera via terminal (console) e permite que os usuários realizem as operações bancárias mais fundamentais, como depósito, saque e extrato. O sistema foi projetado para ser intuitivo e fácil de usar, com foco na lógica de programação e na manipulação de estruturas de dados em Python. Projeto proposto pelos professores da Dio.

## Funcionalidades da v1

  * **Depositar:** Permite ao usuário adicionar um valor à sua conta. O sistema valida se o valor inserido é positivo.
  * **Sacar:** Permite ao usuário retirar um valor da sua conta. O sistema verifica se o valor do saque é válido e se há saldo suficiente. Há um limite de 3 saques diários.
  * **Extrato:** Exibe todas as transações (depósitos e saques) realizadas na conta, finalizando com o saldo atual.
  * **Sair:** Encerra a aplicação.

## Como Usar

### Pré-requisitos

  * Ter o [Python](https://www.python.org/downloads/) 3.x instalado em sua máquina.

### Instalação

1.  Clone este repositório para o seu ambiente local:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd seu-repositorio
    ```

### Execução

Para iniciar o sistema, execute o seguinte comando no seu terminal:

```bash
python sistema_bancario.py
```

Após a execução, um menu interativo será exibido no console, permitindo que você escolha a operação desejada.

## Estrutura do Código

O projeto é composto por um único arquivo principal, `sistema_bancario.py`, que contém toda a lógica para o funcionamento do sistema. As variáveis principais incluem:

  * `saldo`: Armazena o valor atual da conta.
  * `limite`: Define o valor máximo por saque.
  * `extrato`: Uma string que acumula o histórico de transações.
  * `numero_saques`: Um contador para o número de saques realizados no dia.
  * `LIMITE_SAQUES`: Uma constante que define o número máximo de saques diários.

## Próximos Passos (Futuras Versões)

  * **v2:** Modularização do código em funções.
  * **v3:** Adição de múltiplos usuários e contas.
  * **v4:** Implementação de classes e orientação a objetos.
  * **v5:** Conexão com um banco de dados para persistência dos dados.

## Contribuição

Contribuições são bem-vindas\! Se você tiver sugestões para melhorar este projeto, sinta-se à vontade para criar um "fork" e enviar um "pull request".

## Autor

**Izaac "H4D3S" Emanoel**

  * **GitHub:** [yH4D3S](https://www.google.com/search?q=https://github.com/yH4D3S)
