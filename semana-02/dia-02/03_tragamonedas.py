import random

class Tragamonedas:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

    def mostrar(self):
        print(f"🎰 {self.nombre} — Créditos: S/ {self.creditos}")

    def girar(self):
        simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
        resultado = []
        # Aqui viene la logica del giro
        for i in range(3):
            # Debemos generar un indice alazar 
            indice = random.randint(0,len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(resultado)
        return resultado

    def jugar(self, apuesta):
        if apuesta > self.creditos:
            print(f"No tienes suficientes creditos, solo dispones de {self.creditos}")
            return

        self.creditos = self.creditos - apuesta
        resultado = self.girar() # ['🍀', '🍒', '🍒']

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 10
            print(f"Ganaste {premio}")
            self.creditos = self.creditos + premio
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 2
            print(f"Ganaste {premio}")
            self.creditos = self.creditos + premio
        else:
            print("Lo siento lo perdiste")
        
maquina = Tragamonedas("La Siete", 100)
maquina.jugar(100)