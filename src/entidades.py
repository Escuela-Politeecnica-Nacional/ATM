
class Operador:
    def __init__(self):
        self.atms_asignados = []
        self.alertas = []

    def asignar_atm(self, atm):
        self.atms_asignados.append(atm)
        atm.operador_asignado = self

    def recibir_alerta(self, alerta):
        self.alertas.append(alerta)


class ATM(Operador):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.activo = True
        self.conectado = True
        self.operador_asignado = None
        # {denominacion: {"cantidad_maxima": int, "cantidad_minima": int, "cantidad_actual": int}}
        self.casetes = {}

    def establecer_casete(self, denominacion, cantidad_maxima, cantidad_minima):
        self.casetes[denominacion] = {
            "cantidad_maxima": cantidad_maxima,
            "cantidad_minima": cantidad_minima,
            "cantidad_actual": 0,
        }

    def cargar_billetes(self, denominacion, cantidad):
        self.casetes[denominacion]["cantidad_actual"] = cantidad

    def esta_en_nivel_critico(self):
        return any(c["cantidad_actual"] < c["cantidad_minima"] for c in self.casetes.values())

    def mensaje_reabastecimiento(self):
        faltantes = [
            (den, c["cantidad_maxima"] - c["cantidad_actual"])
            for den, c in sorted(self.casetes.items(), reverse=True)
        ]
        primero = f"{faltantes[0][1]} billetes de {faltantes[0][0]} dólares"
        resto = [f"{cant} de {den} dólares" for den, cant in faltantes[1:]]
        return "Se requieren " + " y ".join([primero] + resto)

    def verificar_capacidad(self):
        if self.esta_en_nivel_critico():
            alerta = {
                "atm": self.nombre,
                "nivel": "Crítico",
                "mensaje": self.mensaje_reabastecimiento(),
            }
            self.operador_asignado.recibir_alerta(alerta)
            return alerta
        return None
