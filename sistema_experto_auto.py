#David Alejandro Villarreal Aguirre

def preguntar(p):
    r = input(p + " (s/n): ").strip().lower()
    return r in ["s", "si", "sí", "y"]

def diagnostico():
    print("="*65)
    print("   SISTEMA EXPERTO - DIAGNÓSTICO DE AUTOS (versión alternativa)")
    print("="*65)

    # Regla 1 y 2
    arranca = preguntar("¿El auto arranca?")
    if not arranca:
        tablero = preguntar("¿Se encienden las luces del tablero?")
        if not tablero:
            print("\nPosible causa: Batería descargada o conexiones defectuosas.\n")
            return
        else:
            print("\nPosible causa: Falla en el motor de arranque.\n")
            return

    # Regla 3
    apaga_acelerar = preguntar("¿El auto se apaga al acelerar?")
    if apaga_acelerar:
        print("\nPosible causa: Problema en el suministro de combustible.\n")
        return

    # Regla 4
    humo_negro = preguntar("¿Sale humo negro por el escape?")
    if humo_negro:
        print("\nPosible causa: Mezcla rica de combustible.\n")
        return

    # Regla 5
    humo_blanco = preguntar("¿Sale humo blanco constante por el escape?")
    if humo_blanco:
        print("\nPosible causa: Falla en la junta de culata.\n")
        return

    # Si ninguna regla aplica
    print("\nNo se encontró un diagnóstico con las reglas actuales.\n")

def main():
    while True:
        diagnostico()
        otra = input("¿Quieres hacer otro diagnóstico? (s/n): ").strip().lower()
        if otra not in ["s", "si", "sí", "y"]:
            print("¡Gracias por usar el sistema experto! 🚗🔧")
            break

if __name__ == "__main__":
    main()

