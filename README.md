# ✂️ Sistema Gerenciador de Barbearia

Este é um sistema interativo em linha de comando desenvolvido em Python para o gerenciamento de fluxos de atendimento e controle financeiro de uma barbearia. O projeto foi construído para consolidar os conceitos de **Programação Orientada a Objetos (POO)** e **Persistência de Dados** na disciplina de Programação Estruturada do IFPB.

O software segue rigorosamente a estrutura de requisitos proposta no **Exercício 50** da disciplina, utilizando serialização de objetos para garantir que os dados sobrevivam entre diferentes execuções.

---

## 🚀 Funcionalidades

O sistema oferece um menu interativo com as seguintes operações:
1. **Adicionar Agendamento:** Registra um novo cliente, o serviço solicitado e o valor, gerando um ID de identificação único de forma automática.
2. **Listar Todos:** Exibe na tela todos os agendamentos cadastrados utilizando o método mágico `__str__` para formatação.
3. **Buscar por ID:** Localiza as informações detalhadas de um atendimento específico a partir do seu ID.
4. **Remover Agendamento:** Exclui um registro do sistema pelo ID.
5. **Concluir Serviço (Dar Baixa):** Altera o status de um agendamento de `"Pendente"` para `"Concluído"`.
6. **Ver Faturamento Total (Funcionalidade Extra):** Calcula e exibe dinamicamente a soma financeira de todos os serviços efetivamente concluídos.
0. **Sair:** Salva os estados atuais e encerra o programa.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3** (Nativo, sem dependências externas)
* **Biblioteca `pickle`:** Para serialização e persistência de dados em formato binário (`.pkl`).
* **Biblioteca `os`:** Para verificação de existência prévia de arquivos no disco.

---

## 📦 Estrutura do Código

O projeto está dividido de forma modular seguindo o paradigma de POO:

* **`Agendamento` (Classe Entidade):** Molde que representa a unidade fundamental de dados do sistema (um atendimento com id, nome, serviço, valor e status).
* **`GerenciadorBarbearia` (Classe Gerenciadora):** Entidade responsável por manipular a lista de objetos cadastrados, realizar buscas, exclusões e os métodos de persistência (`salvar` e `carregar`).
* **`menu()` (Função de Interface):** Camada visual via terminal (CLI) equipada com estruturas de repetição (`while`) e blocos de tratamento de exceções (`try/except ValueError`) para garantir a resiliência do programa contra entradas inválidas.

---

## 🔧 Como Executar o Projeto

1. Certifique-se de ter o Python 3 instalado em sua máquina.
2. Clone este repositório ou baixe os arquivos em uma pasta local.
3. Abra o terminal ou prompt de comando na pasta do projeto.
4. Execute o seguinte comando:

```bash
python app.py