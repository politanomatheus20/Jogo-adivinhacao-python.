import random

def gerar_numero_secreto(min_val: int = 1, max_val: int = 100) -> int:
    """
    Gera e retorna um número secreto aleatório dentro de um intervalo.

    Args:
        min_val (int): O valor mínimo do intervalo (inclusivo).
        max_val (int): O valor máximo do intervalo (inclusivo).

    Returns:
        int: O número secreto gerado.
    """
    return random.randint(min_val, max_val)

def obter_palpite_valido(min_val: int = 1, max_val: int = 100) -> int:
    """
    Solicita um palpite ao usuário, garantindo que seja um número inteiro válido
    e que esteja dentro do intervalo permitido.

    Args:
        min_val (int): O valor mínimo permitido.
        max_val (int): O valor máximo permitido.

    Returns:
        int: O palpite válido fornecido pelo usuário.
    """
    while True:
        try:
            entrada = input(f"Digite seu palpite (entre {min_val} e {max_val}): ")
            palpite = int(entrada)
            
            if min_val <= palpite <= max_val:
                return palpite
            else:
                print(f"Palpite inválido! Por favor, digite um número entre {min_val} e {max_val}.")
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números inteiros.")

def jogar(tentativas_maximas: int = 10, min_val: int = 1, max_val: int = 100) -> None:
    """
    Gerencia o loop principal do jogo, comparando o palpite com o número secreto
    e controlando o número de tentativas restantes.

    Args:
        tentativas_maximas (int): O número máximo de tentativas permitidas.
        min_val (int): O valor mínimo do número secreto.
        max_val (int): O valor máximo do número secreto.
    """
    numero_secreto = gerar_numero_secreto(min_val, max_val)
    tentativas = 0

    print("=" * 40)
    print("Bem-vindo ao Jogo de Adivinhação!")
    print(f"Estou pensando em um número entre {min_val} e {max_val}.")
    print(f"Você tem {tentativas_maximas} tentativas para adivinhar.")
    print("=" * 40)

    while tentativas < tentativas_maximas:
        tentativas += 1
        print(f"\n--- Tentativa {tentativas}/{tentativas_maximas} ---")
        palpite = obter_palpite_valido(min_val, max_val)

        if palpite == numero_secreto:
            print(f"\n🎉 Parabéns! Você acertou o número secreto ({numero_secreto}) em {tentativas} tentativa(s)!")
            return
        elif palpite < numero_secreto:
            print("O número secreto é *MAIOR* que o seu palpite.")
        else:
            print("O número secreto é *MENOR* que o seu palpite.")

    print("\n" + "=" * 40)
    print("Fim de Jogo! Suas tentativas acabaram.")
    print(f"O número secreto era: {numero_secreto}")
    print("=" * 40)

def main() -> None:
    """
    Função de entrada que inicia o jogo e gerencia a vontade do jogador de jogar novamente.
    """
    while True:
        jogar()
        repetir = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if repetir != 's':
            print("Obrigado por jogar! Até a próxima.")
            break

if __name__ == "__main__":
    main()
