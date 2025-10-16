"""
Proyecto: Casa Inteligente 🏠💡
Autores: Muratalla Márquez Demian, Marcos López Hernández
Fecha: 16/10/2025
Descripción:
    Este programa implementa un sistema básico de casa inteligente
    utilizando Programación Orientada a Objetos (POO) en Python.

    Cumple con los siguientes requisitos:
    - Clase abstracta Dispositivo (usando abc.ABC y @abstractmethod)
    - Subclases concretas: LuzInteligente, CamaraSeguridad, SensorMovimiento
    - Sobrescritura de métodos mostrar_datos()
    - Clase compuesta CasaInteligente que gestiona dispositivos
    - Simulación de encendido, lecturas y ejecución de una escena automática
"""

from abc import ABC, abstractmethod
import random
import time

# ==================================================
# Clase Abstracta: Dispositivo
# ==================================================
class Dispositivo(ABC):
    """
    Clase abstracta base para todos los dispositivos inteligentes.
    """

    def __init__(self, id_dispositivo):
        self.__id_dispositivo = id_dispositivo
        self.__estado = False  # Apagado por defecto

    @abstractmethod
    def encender(self):
        """Método abstracto para encender el dispositivo."""
        pass

    @abstractmethod
    def apagar(self):
        """Método abstracto para apagar el dispositivo."""
        pass

    @abstractmethod
    def mostrar_datos(self):
        """Método abstracto para mostrar los datos específicos del dispositivo."""
        pass

    # Métodos comunes
    def obtener_estado(self):
        """Devuelve el estado actual del dispositivo."""
        return "Encendido" if self.__estado else "Apagado"

    def cambiar_estado(self, nuevo_estado: bool):
        """Cambia el estado interno del dispositivo."""
        self.__estado = nuevo_estado

    def obtener_id(self):
        """Devuelve el ID del dispositivo."""
        return self.__id_dispositivo


# ==================================================
# Subclases concretas
# ==================================================
class LuzInteligente(Dispositivo):
    """
    Representa una luz inteligente con control de intensidad.
    """

    def __init__(self, id_dispositivo):
        super().__init__(id_dispositivo)
        self.intensidad = 0  # Valor de 0 a 100 %

    def encender(self):
        self.cambiar_estado(True)
        self.intensidad = random.randint(30, 100)

    def apagar(self):
        self.cambiar_estado(False)
        self.intensidad = 0

    def mostrar_datos(self):
        return f"[LuzInteligente #{self.obtener_id()}] Estado: {self.obtener_estado()} | Intensidad: {self.intensidad}%"


class CamaraSeguridad(Dispositivo):
    """
    Representa una cámara de seguridad.
    """

    def __init__(self, id_dispositivo):
        super().__init__(id_dispositivo)
        self.grabando = False

    def encender(self):
        self.cambiar_estado(True)
        self.grabando = True

    def apagar(self):
        self.cambiar_estado(False)
        self.grabando = False

    def mostrar_datos(self):
        return f"[CamaraSeguridad #{self.obtener_id()}] Estado: {self.obtener_estado()} | Grabando: {self.grabando}"


class SensorMovimiento(Dispositivo):
    """
    Representa un sensor de movimiento.
    """

    def __init__(self, id_dispositivo):
        super().__init__(id_dispositivo)
        self.movimiento_detectado = False

    def encender(self):
        self.cambiar_estado(True)
        # Simula detección aleatoria de movimiento
        self.movimiento_detectado = random.choice([True, False])

    def apagar(self):
        self.cambiar_estado(False)
        self.movimiento_detectado = False

    def mostrar_datos(self):
        return f"[SensorMovimiento #{self.obtener_id()}] Estado: {self.obtener_estado()} | Movimiento detectado: {self.movimiento_detectado}"


# ==================================================
# Clase Compuesta: CasaInteligente
# ==================================================
class CasaInteligente:
    """
    Representa una casa inteligente que contiene múltiples dispositivos.
    """

    def __init__(self):
        self.dispositivos = []

    def agregar_dispositivo(self, dispositivo: Dispositivo):
        """Agrega un dispositivo a la casa."""
        self.dispositivos.append(dispositivo)

    def mostrar_todos(self):
        """Muestra los datos de todos los dispositivos."""
        print("\n📋 ESTADO ACTUAL DE LOS DISPOSITIVOS:")
        for d in self.dispositivos:
            print("  ", d.mostrar_datos())

    def ejecutar_escena(self):
        """
        Escena automática:
        Si algún sensor detecta movimiento → encender luces y activar cámaras.
        """
        print("\n🤖 Ejecutando escena automática...\n")
        hay_movimiento = any(
            isinstance(d, SensorMovimiento) and d.movimiento_detectado for d in self.dispositivos
        )

        if hay_movimiento:
            print("🚨 Movimiento detectado → Encendiendo luces y cámaras...")
            for d in self.dispositivos:
                if isinstance(d, (LuzInteligente, CamaraSeguridad)):
                    d.encender()
        else:
            print("✅ No se detectó movimiento. La casa permanece en modo reposo.")


# ==================================================
# Simulación
# ==================================================
if __name__ == "__main__":
    print("🏠 Simulación de Casa Inteligente 🏠\n")

    casa = CasaInteligente()

    # Crear 5 dispositivos de distintos tipos
    dispositivos = [
        LuzInteligente(1),
        LuzInteligente(2),
        CamaraSeguridad(3),
        CamaraSeguridad(4),
        SensorMovimiento(5)
    ]

    # Agregarlos a la casa
    for d in dispositivos:
        casa.agregar_dispositivo(d)

    # Encender todos los dispositivos
    for d in dispositivos:
        d.encender()

    # Mostrar el estado inicial
    casa.mostrar_todos()

    # Esperar un momento para simular lectura
    time.sleep(1)

    # Ejecutar la escena automática
    casa.ejecutar_escena()

    # Mostrar resultados finales
    time.sleep(1)
    casa.mostrar_todos()

    print("\n🏁 Fin de la simulación 🏁")
