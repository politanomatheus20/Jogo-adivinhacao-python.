# 🎮 Jogo de Adivinhação de Números

Um divertido jogo de lógica em Python onde você deve descobrir o número secreto! O jogo fornecerá dicas se o seu palpite é maior ou menor que o número escolhido.

## 🚀 Tecnologias Usadas
* **Python 3.x**
* Biblioteca Padrão: `random`

## ⚙️ Como Executar
1. Certifique-se de ter o Python 3 instalado na sua máquina.
2. Navegue até a pasta do projeto no seu terminal.
3. Execute o script principal localizado na pasta `src`:
   ```bash
   python src/main.py
   ```

## 🧠 Conceitos Aplicados
Este projeto foi desenvolvido como prática de fundamentos do Python, aplicando:
* **Modularização**: Separação da lógica de geração, validação e execução em diferentes funções (`gerar_numero_secreto`, `obter_palpite_valido`, `jogar`, `main`).
* **Loops**: Utilização de laços `while` para gerenciar as tentativas e a opção de jogar novamente.
* **Condicionais**: Estruturas `if/elif/else` para avaliar o palpite em relação ao número secreto e fornecer as dicas (maior ou menor).
* **Tratamento de Exceções**: Utilização de `try/except` com captura de `ValueError` para evitar que o código quebre caso o usuário não digite um número inteiro.
* **Type Hinting**: Dicas de tipo nos parâmetros e retornos para código mais seguro e legível.
