# Sistema de Atendimento e Pedidos em Python

## Informações do Projeto
- **Estudante:** Matheus Carvalho Pereira
- **Disciplina:** Algoritmos e Programação
- **Curso:** Análise e Desenvolvimento de Sistemas

---

## Descrição do Programa
Este programa é uma solução desenvolvida em Python para automatizar o atendimento e a realização de pedidos de uma lanchonete. O sistema permite cadastrar o nome do cliente, exibir o cardápio disponível, processar a escolha de múltiplos produtos e quantidades, validar entradas do usuário, calcular automaticamente descontos progressivos com base no valor total acumulado e registrar a forma de pagamento escolhida.

---

## Principais Funcionalidades
1. **Identificação do Cliente:** Captura do nome para personalização do atendimento.
2. **Exibição e Seleção de Produtos:** Apresentação de cardápio com 5 produtos fixos e validação de códigos.
3. **Cálculo de Subtotal e Total:** Acúmulo do valor da compra sem a necessidade de guardar histórico em listas/dicionários.
4. **Validação de Entradas:** Tratamento de opções inválidas (códigos inexistentes, quantidades negativas/nulas e respostas incorretas).
5. **Regra de Desconto Automática:**
   - Compras abaixo de R$ 50,00: Sem desconto (0%).
   - Compras de R$ 50,00 a R$ 99,99: 5% de desconto.
   - Compras iguais ou superiores a R$ 100,00: 10% de desconto.
6. **Seleção e Validação de Pagamento:** Opções de Dinheiro, PIX e Cartão com estrutura `match-case`.
7. **Resumo Detalhado da Compra:** Apresentação do recibo com nome, total original, taxa de desconto, valor abatido, valor final e forma de pagamento.

---

## Instruções para Executar o Programa

### Pré-requisitos
- Python versão 3.10 ou superior instalado.

### Passos para Execução
1. Clone este repositório ou baixe os arquivos para a sua máquina local:
   ```bash
   git clone https://github.com/matheus01pereiracarva-sketch/trabalho-15-pontos.git
 