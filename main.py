from Juego import Juego

if __name__ == "__main__":
    try:
        Juego().jugar()
    except (KeyboardInterrupt, EOFError):
        print("Partida terminada")
        