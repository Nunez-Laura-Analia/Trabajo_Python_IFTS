# Importaciones
from datetime import date, datetime, timedelta
import math

today = date.today()
now = datetime.now()

# Clases

class Vehiculo:
    def __init__(self, marca: str, modelo: str, patente: str, kmActual: int, ultKm: int, ultAceite: int, ultCorrea: int, ultBujia: int, ultNeumatico: int, respuesta: int, ultVtv: int):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.kmActual = kmActual
        self.ultKm = ultKm
        self.ultAceite = ultAceite
        self.ultCorrea = ultCorrea
        self.ultBujia = ultBujia
        self.ultNeumatico = ultNeumatico
        self.respuesta = respuesta
        self.ultVtv = ultVtv
        super().__init__(kmActual)

    def obtener_km_actual(self):
        return self.kmActual

    def obtener_ultimo_km(self):
        self.kmAnterior = self.kmActual
        self.kmActual = self.ultKm
        return self.kmAnterior, self.kmActual

    def obtener_ultimo_cambio_aceite(self):
        self.valorAceite = 20000
        self.proxAceite = self.ultAceite + 10000
        self.tiempoAceite = self.proxAceite - self.kmActual

        if self.kmActual < self.proxAceite:
            return "Para su proximo cambio de haciente le falta recorrer: ", self.tiempoAceite, "km. El proximo cambio de aceite seran: $", self.valorAceite
        else:
            self.tiempo_Aceite = self.proxAceite - self.kmActual
            return self.tiempoAceite

    def calcular_recorrido(self):
        self.diferencia = self.kmActual - self.kmAnterior
        self.diario = self.diferencia / 25
        return "Por mes realiza un estimado de ", self.diferencia, "km al mes. Los km recorrido diarios son :", self.diario, "Km."

    def obtener_ultimo_cambio_correa(self):
        self.valorCorrea = 80000
        self.proxCorrea = self.ultCorrea + 60000
        self.tiempoCorrea = self.proxCorrea - self.kmActual

        if self.kmActual < self.proxCorrea:
            return "El proximo cambio de correas es a los ", self.proxCorrea, "km y le faltan ", self.tiempoCorrea, "km. Tiene un valor de $", self.valorCorrea, "."
        else:
            return "Se paso el cambio de correas hace: ", self.tiempoCorrea, "km."

    def obtener_ultimo_cambio_bujia(self):
        self.valorCable = 40000
        self.proxBujia = self.ultBujia + 30000
        self.tiempoBujia = self.proxBujia - self.kmActual

        if self.kmActual > self.proxBujia:
            return "Se paso del cambio de bujias ", self.tiempoBujia, "km."
        else:
            return "Su proximo cambio de bujias es a los ", self.proxBujia, "km y le faltan", self.tiempoBujia, ". Tiene un valor de $", self.valorCable, "."

    def obtener_ultimo_cambio_neumaticos(self):
        self.valorNeumatico = 200000
        self.proxNeumatico = self.ultNeumatico + 50000
        self.tiempoNeumatico = self.proxNeumatico - self.kmActual

        if self.kmActual < self.proxNeumatico:
            return "Su proximo cambio de neumaticos es a los ", self.proxNeumatico, "km y le faltan", self.tiempoNeumatico, ". Tiene un valor de $", self.valorNeumatico, "."
        else:
            return "Se paso ", self.tiempoNeumatico, "km."

    def realizar_vtv(self):
        if self.respuesta == 1:
            self.respuesta = True
            return self.respuesta
        elif self.respuesta != 1:
            self.respuesta = False

        while self.respuesta:
            try:
                self.ultVtv = datetime.strptime(self.ultVtv, "%d/%m/%Y")
                self.proxVtv = self.ultVtv + timedelta(days=365)
                return "La proxima vtv, se realizara en la fecha: ", self.proxVtv, "."
            except:
                return "No ha ingresado una fecha correcta."


class Supervisor:
    def _init_(self, nombre: str, apellido: str, auto):
        self.nombre = nombre
        self.apellido = apellido
        self.auto = auto


class Gastos(Vehiculo):
    def _init_(self, kmActual):
        super().__init__(kmActual)

    def gastosAuto(self):
        self.gastos = []

    def historialAceite(self):
        self.aceiteHistorico = math.floor(self.kmActual / 10000)
        self.precioAceite = self.aceiteHistorico * 20000
        return "Hasta el momento solo con el aceite gasto: $", self.precioAceite, "."

    def historialCorrea(self):
        self.correaHistorico = math.floor(self.kmActual / 60000)
        self.precioCorrea = self.correaHistorico * 80000
        return "Hasta el momento solo con la correa gasto: $", self.precioCorrea, "."

    def historialBujia(self):
        self.bujiaHistorico = math.floor(self.kmActual / 30000)
        self.precioBujia = self.bujiaHistorico * 40000
        return "Hasta el momento solo con la bujia gasto: $", self.precioBujia, "."

    def historialNeumatico(self):
        self.neumaticoHistorico = math.floor(self.kmActual / 50000)
        self.precioNeumatico = self.neumaticoHistorico * 200000
        return "Hasta el momento solo con los neumaticos gasto: $", self.precioNeumatico, "."


# Ingreso de vehiculos
Auto1 = Vehiculo("Volkswagen", "Gold Trend", "AB234MK",
                 50000, 55000, 60, 60, 60, 60, 60, 11/5/2019)
Auto2 = Vehiculo("Renault", "Megane", "OXQ291",
                 50000, 55000, 60, 60, 60, 60, 60, 15/12/2020)
Auto3 = Vehiculo("Ford", "Ka", "AA397GS", 40000,
                 45000, 50, 50, 50, 50, 50, 30/4/2021)
Auto4 = Vehiculo("Chevrolete", "Onix", "AE414MP",
                 50000, 65000, 70, 70, 70, 70, 70, 15/11/2022)

# Ingreso de supervisores
Loyola1 = Supervisor("Eduardo", "loyola", Auto1)
Maciel1 = Supervisor("Claudio", "maciel", Auto2)
Gajardo1 = Supervisor("Lucciano", "gajardo", Auto3)
Velazquez1 = Supervisor("Jorge", "velazquez", Auto4)

# Ingreo de gastos
Gasto1 = Gastos(Auto1)
Gasto2 = Gastos(Auto2)
Gasto3 = Gastos(Auto3)
Gasto4 = Gastos(Auto4)

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

def auto_elegido(listaDeAutos, vehiculo_elegido):
    if vehiculo_elegido > 4:
        return "Ha ocurrido un error."
    else:
        vehiculo_elegido = listaDeAutos[vehiculo_elegido] - 1
        return vehiculo_elegido
    
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
            auto.btener_ultimo_cambio_correa()
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


apellido = input("Ingrese su APELLIDO:")
pregunta(apellido)

vehiculo_elegido = int(input("Ingrese el numero de auto que desea ver. Por ejemplo si es el auto uno, inglrese 1: "))
auto = auto_elegido(listaDeAutos, vehiculo_elegido)

opciones(auto)

correrGasto(auto)

# INICIACION PARA LA CONSOLA
# for n in lista:
#     n = apellido1
#     if apellido1 == Loyola1.apellido:
#         a = pregunta(Auto1)
#         b = correrGasto(Gasto1)
#         c = opciones(Auto1)
#     elif apellido1 == Maciel1.apellido:
#         a = pregunta(Gasto2)
#         b = correrGasto(Auto2)
#         c = opciones(Auto2)
#     elif apellido1 == Velazquez1.apellido:
#         a = pregunta(Auto4)
#         b = correrGasto(Gasto4)
#         c = opciones(Auto3)
#     elif apellido1 == Gajardo1.apellido:
#         a = pregunta(Auto3)
#         b = correrGasto(Gasto3)
#         c = opciones(Auto4)
#     break

         