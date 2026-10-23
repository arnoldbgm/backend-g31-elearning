# POO => Programacion Orientada a Objetos
# Es un paradigma de programacion, vamos a organizar nuestro codigo
# mediante clases y objetos
# Es representar a los elementos del mundo real, dentro de un programa

# MUNDIAL 2026 
nombre1 = "Messi"
edad1 = 37
posicion1 = "Delantero"
equipo1 = "Argentina"

nombre2 = "Mbappe"
edad2 = 27
posicion2 = "Delantero"
equipo2 = "Francia"

# Para solucionar el problema de arriba, usaremos las clases
# ¿Que es una clase? (PLANO)
# Una clase es una plantilla o molde, que define las caracteristicas
# y los metodos (comportamientos)

# ¿Como puedo solicitar valores para crear mi clase?
# El constructor, te va a permitir recibir datos y con 
# esos tu podras crear tu instancia (objeto)
# Constructor => __init__
class Jugador:
    # La creacion de un constructor
    # REGLA DE ORO: Toda funcion dentro de una clase
    # su primer argumento es el self
    def __init__(self, nombre, edad, posicion, equipo):
        # Jugador.nombreCompleto = nombre
        # self = Jugador (a nuestra clase)
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo = equipo

    def correr(self):
        print(f"El jugador {self.nombre} esta corriendo")

    def mostrar_info(self):
        # Messi - 37 año - Delantero - Argentina
        print(f"{self.nombre} - {self.edad} años - {self.posicion} - {self.equipo}")

    def anotar_gol(self, equipo_rival):
        print(f"El jugador {self.nombre} anoto un gol contra {equipo_rival}")
# Convertir una clase en algo tangible
# Instanciar (Crear un objeto)

messi = Jugador("Lionel Messi", 37, "Delantero", "Argentina")
mbappe = Jugador("Kylian Mbappe", 27, "Delantero", "Francia")

# Metodos - Funciones
# Una clase no solo tiene datos, sino tambien puede realizar
# acciones
# Ejecucion de un metodo
mbappe.correr()
mbappe.mostrar_info()
mbappe.anotar_gol("Valencia")

# PILARES DEL POO
# ABSTRACCION
# POLIMORFISMO
# HERENCIA
# ENCAPSULAMIENTO

# Abstraccion
# Significa  extrare las propiedades y metodos de parte de un objeto real

class Equipo:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        print(f"Jugador insertado exitosamente")

brasil = Equipo("Seleccion de Brasil", "Brasil")

ronaldo = Jugador("Ronaldo", 29, "Delantero", "Seleccion de Brasil")
rivaldo = Jugador("Rivaldo", 28, "Delantero", "Seleccion de Brasil")
ronaldinho = Jugador("Ronaldinho", 27, "Mediocampista", "Seleccion de Brasil")

brasil.agregar_jugador(ronaldo)
brasil.agregar_jugador(rivaldo)
brasil.agregar_jugador(ronaldinho)

print(brasil.jugadores)

# POLIMORFISMO
# Significa que una clase puede tomar muchas formas
cristiano_ronaldo = Jugador("Cristiano Ronaldo", 41, "Volante", "Seleccion de Portugal")
halland = Jugador("Halland", 24, "Delantero", "Seleccion de Noruega")

# HERENCIA
#              hereda
# La clase padre ->  clase hija
# Vas a heredar el comportamiento de las propiedas y los metodos a la clase hija

class JugadorPadre:
    def __init__(self, nombre, edad, equipo):
        self._nombre= nombre
        self.edad = edad
        self.equipo = equipo
    def entrenar(self):
        print(f"Hola estoy entrando, te saluda {self.nombre}")

#           (HERENCIA)
class Arquero(JugadorPadre):
    # Necesitamos estatura, el penalesAtajados
    def __init__(self, nombre, edad, equipo, estatura, penalesAtajados):
        super().__init__(nombre, edad, equipo)
        self.estatura = estatura
        self.penalesAtajados = penalesAtajados

    def atajar(self):
        print(f"Balon atajado por {self.nombre}")

dibu = Arquero("Dibu Martinez", 33, "Argentina", 1.95, 150)

print(dibu._nombre)

dibu._nombre = "Emiliano Martinez"

print(dibu._nombre)