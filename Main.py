# Importaciones
from datetime import date, datetime, timedelta
import math

today = date.today()
now = datetime.now()

# Clases 
class Vehiculo:
    def __init__(self, marca: str, modelo: str, patente: str, kmActual: int, ultKm: int, ultAceite: int, ultCorrea: int, ultBujia: int, ultNeumatico: int, ultVtv: int):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.kmActual = kmActual
        self.ultKm = ultKm
        self.ultAceite = ultAceite
        self.ultCorrea = ultCorrea
        self.ultBujia = ultBujia
        self.ultNeumatico = ultNeumatico
        self.ultVtv = ultVtv
        
    def obtener_km_actual(self):
        return self.kmActual

    def obtener_ultimo_km(self):
        self.kmAnterior = self.kmActual
        self.kmActual = self.ultKm
        return self.kmAnterior, self.kmActual

    def proximo_cambio_aceite(self):
        # se suma el kilometraje del dia del ultimo cambio de aceite y 10000, que es la cantidad de km que dura el cambio de aceite.
        tope_de_duracion = self.ultAceite + 10000
        # Se resta el total de km que puede recorrer el vehiculo con el anterior cambio de aceite, con la cantidad de km que tiene actualemte.
        tiempo_restante = tope_de_duracion - self.kmActual

        if self.kmActual < tope_de_duracion:
            return "Su proximo cambio de aceite es a los: ", tope_de_duracion, "km y falta recorrer ", tiempo_restante, "."
        else:
            return "Se paso del cambio de aceite hace: ", tiempo_restante, "km."

    def proximo_cambio_correa(self):
        tope_de_duracion = self.ultCorrea + 60000
        tiempo_restante = tope_de_duracion - self.kmActual

        if self.kmActual < tope_de_duracion:
            return "El proximo cambio de correas es a los ", tope_de_duracion, "km y le faltan ", tiempo_restante, "."
        else:
            return "Se paso del cambio de correas hace: ", tiempo_restante, "km."

    def proximo_cambio_bujia(self):
        tope_de_duracion = self.ultBujia + 30000
        tiempo_restante = tope_de_duracion - self.kmActual

        if self.kmActual < tope_de_duracion:
            return "El proximo cambio de bujias es a los: ", tope_de_duracion, "km y le faltan", tiempo_restante, "."
        else:
            return "Se paso del cambio de bujias hace ", tiempo_restante, "km."

    def obtener_ultimo_cambio_neumaticos(self):
        tope_de_duracion = self.ultNeumatico + 50000
        tiempo_restante = tope_de_duracion - self.kmActual

        if self.kmActual < tope_de_duracion:
            return "El proximo cambio de neumaticos es a los ", tope_de_duracion, "km y le faltan", tiempo_restante, "."
        else:
            return "Se paso del cambio de neumaticos hace ", tiempo_restante, "km."

    def realizar_vtv(self):
        b = True
        if b:
            self.vtv = datetime.strptime(self.ultVtv, "%d/%m/%Y")
            self.proxVtv = self.ultVtv + timedelta(days=365)
            return "La proxima vtv, se debe realizar en la fecha: ", self.proxVtv, "."
        else:
            return "No ha ingresado una fecha correcta."

    def calcular_recorrido(self):
        estimativo_recorrido_por_mes = self.kmAnterior
        estimativo_por_dia = self.kmAnterior / 30
        return "Por mes realiza un estimativo de ", estimativo_recorrido_por_mes, "km. El estimativo de km recorridos por dia son de: ", estimativo_por_dia, "."


class Supervisor:
    def _init_(self, nombre: str, apellido: str, auto):
        self.nombre = nombre
        self.apellido = apellido
        self.auto = auto


class Gastos(Vehiculo):
    def __init__(self, precioAceite: int, precioCorrea: int, precioBujia: int, precioNeumatico: int):
        self.precioAceite = precioAceite
        self.precioCorrea = precioCorrea
        self.precioBujia = precioBujia
        self.precioNeumatico = precioNeumatico
        self.mantenimiento = ["aceite", "correa", "bujia", "neumaticos"]
        self.gastos = []

    def historialAceite(self):
        # Dividimos la cantidad total de kilometros del vehiculo por 10000, que es la duracion en km de cada cambio de aceite.
        # Asi obtenemos el total de cambios de aceite realizados hasta el momento.
        aceiteHistorico = math.floor(self.kmActual / 10000)
        # Multiplicamos el total de cambios por el valor del aceite, y obtenemos el gasto total del vehiculo en el mismo.
        valorAceite = aceiteHistorico * self.precioAceite
        self.gastos.append(valorAceite)

    def historialCorrea(self):
        correaHistorico = math.floor(self.kmActual / 60000)
        valorCorrea = correaHistorico * self.precioCorrea
        self.gastos.append(valorCorrea)

    def historialBujia(self):
        bujiaHistorico = math.floor(self.kmActual / 30000)
        valorBujia = bujiaHistorico * self.precioBujia
        self.gastos.append(valorBujia)

    def historialNeumatico(self):
        self.neumaticoHistorico = math.floor(self.kmActual / 50000)
        valorNeumatico = self.neumaticoHistorico * self.precioNeumatico
        self.gastos.append(valorNeumatico)

    def gastos_totales(self):
        return "El total de los gastos en ", self.mantenimiento[0], " es de ", self.gastos[0], "El total de los gastos en ", self.mantenimiento[1], " es de ", self.gastos[1], "El total de los gastos en ", self.mantenimiento[2], " es de ", self.gastos[2], "El total de los gastos en ", self.mantenimiento[3], " es de ", self.gastos[3]


# Ingreso de vehiculos
Auto1 = Vehiculo("Volkswagen", "Gold Trend", "AB234MK",
                 50000, 55000, 30000, 31000, 30500, 29500, 11/5/2019)
Auto2 = Vehiculo("Renault", "Megane", "OXQ291",
                 17000, 18000, 15000, 16000, 15500, 15750, 15/12/2020)
Auto3 = Vehiculo("Ford", "Ka", "AA397GS",
                 45000, 45500, 35000, 37500, 38000, 38250, 30/4/2021)
Auto4 = Vehiculo("Chevrolete", "Onix", "AE414MP",
                 50000, 65000, 49000, 49500, 49750, 49800, 15/11/2022)

# Ingreso de supervisores
Loyola1 = Supervisor("Eduardo", "loyola", Auto1)
Maciel1 = Supervisor("Claudio", "maciel", Auto2)
Gajardo1 = Supervisor("Lucciano", "gajardo", Auto3)
Velazquez1 = Supervisor("Jorge", "velazquez", Auto4)

# Ingreso de gastos
gasto1 = Gastos(Auto1, 20000, 80000, 46000, 190000)
gasto2 = Gastos(Auto2, 15000, 60000, 45000, 200000)
gasto3 = Gastos(Auto3, 25000, 70000, 50000, 150000)
gasto4 = Gastos(Auto4, 21000, 90000, 48000, 250000)

# Lista de autos y supervisores
listaDeAutos = [Auto1, Auto2, Auto3, Auto4]
lista = [Loyola1, Maciel1, Gajardo1, Velazquez1]

# INICIO DEL PROGRAMA

def pregunta(apellido):
    if apellido == Loyola1.apellido:
        print("Bienvenido ", Loyola1.nombre)
        kmAct1 = Auto1.obtener_km_actual()
        kmUlt1 = Auto1.obtener_ultimo_km()
        return kmAct1, kmUlt1
    elif apellido == Maciel1.apellido:
        print("Bienvenido ", Maciel1.nombre)
        kmAct2 = Auto2.obtener_km_actual()
        kmUlt2 = Auto2.obtener_ultimo_km()
        return kmAct2, kmUlt2
    elif apellido == Gajardo1.apellido:
        print("Bienvenido ", Gajardo1.nombre)
        kmAct3 = Auto3.obtener_km_actual()
        kmUlt3 = Auto3.obtener_ultimo_km()
        return kmAct3, kmUlt3
    elif apellido == Velazquez1.apellido:
        print("Bienvenido ", Velazquez1.nombre)
        kmAct4 = Auto4.obtener_km_actual()
        kmUlt4 = Auto4.obtener_ultimo_km()
        return kmAct4, kmUlt4
    else:
        return print("Ingreso mal el apellido")

def opciones(auto):
    arranque = True
    while arranque:
        opcion = int(input("INDIQUE QUE QUIERE SABER :",
                           "1. Kilometro anterior y actual del Vehiculo",
                           "2. Proximo cambio de ACEITE",
                           "3. Proximo cambio de CORREA ",
                           "4. Proximo cambio de CABLE Y BUJIA",
                           "5. Proximo cambio de NEUMATICO",
                           "6. Proxima VTV",
                           "7. Kilometros recorridos diarios/mensual",
                           "8. Cerrar sesion"))
        if opcion == 1:
            auto.obtener_km_actual()
            auto.obtener_ultimo_km()
        elif opcion == 2:
            auto.obtener_ultimo_cambio_aceite()
        elif opcion == 3:
            auto.obtener_ultimo_cambio_correa()
        elif opcion == 4:
            auto.obtener_ultimo_cambio_bujia()
        elif opcion == 5:
            auto.obtener_ultimo_cambio_neumaticos()
        elif opcion == 6:
            auto.realizar_vtv()
        elif opcion == 7:
            auto.calcular_recorrido()
        elif opcion == 8:
            arranque = False


def correrGasto(auto):
    arranque = True
    while arranque:
        opcion = int(input("INDIQUE QUE QUIERE SABER :",
                           "1. Gasto total de aceite",
                           "2. Gasto total de correa",
                           "3. Gasto total de bujias",
                           "4. Gasto total de neumaticos",
                           "5. Cerrar sesion"))
        if opcion == 1:
            auto.historialAceite()
        elif opcion == 2:
            auto.historialCorrea()
        elif opcion == 3:
            auto.historialBujia()
        elif opcion == 4:
            auto.historialNeumatico()
        elif opcion == 5:
            print("A R S E C")
            arranque = False


apellido = input("Ingrese su Apellido:")

# INICIACION PARA LA CONSOLA
for n in lista:
    n = apellido
    if apellido == Loyola1.apellido:
        a = pregunta(Auto1)
        b = correrGasto(Gasto1)
        c = opciones(Auto1)
    elif apellido == Maciel1.apellido:
        a = pregunta(Auto2)
        b = correrGasto(Gasto2)
        c = opciones(Auto2)
    elif apellido == Velazquez1.apellido:
        a = pregunta(Auto4)
        b = correrGasto(Gasto3)
        c = opciones(Auto3)
    elif apellido == Gajardo1.apellido:
        a = pregunta(Auto3)
        b = correrGasto(Gasto4)
        c = opciones(Auto4)
    break
