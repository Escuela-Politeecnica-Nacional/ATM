import behave.runner
from behave import *
from src.entidades import *

# use_step_matcher("re")

@step("un operador autorizado que tiene asignado el cajero {atm_nombre}, activo y conectado")
def step_impl(context: behave.runner.Context, atm_nombre: str):
    """
    :type context: behave.runner.Context
    :type atm_nombre: str
    """
    context.operador = Operador()
    context.atm = ATM(atm_nombre.strip('"'))
    context.operador.asignar_atm(context.atm)
    assert context.atm.operador_asignado == context.operador
    assert context.atm.activo and context.atm.conectado

@step("el cajero {atm_nombre} tiene establecido")
def step_impl(context: behave.runner.Context, atm_nombre: str):
    """
    :type context: behave.runner.Context
    :type atm_nombre: str
    """
    assert context.atm.nombre == atm_nombre.strip('"')
    for fila in context.table:
        denominacion = int(fila["denominacion"].split()[0])  # "20 dólares" -> 20
        context.atm.establecer_casete(
            denominacion,
            int(fila["cantidad_maxima"]),
            int(fila["monto_mínimo"]),
        )
    assert len(context.atm.casetes) == len(context.table.rows)


@step("actualmente cuenta con 5 billetes de 20 dólares y 2 billetes de 10 dólares")
def step_impl(context: behave.runner.Context):
    """
    :type context: behave.runner.Context
    """
    context.atm.cargar_billetes(20, 5)
    context.atm.cargar_billetes(10, 2)


@step("se verifica la capacidad actual")
def step_impl(context: behave.runner.Context):
    """
    :type context: behave.runner.Context
    """
    context.alerta = context.atm.verificar_capacidad()


@step("debe enviar la alerta de nivel crítico para el {atm_nombre} al operador asignado con el siguiente mensaje:")
def step_impl(context: behave.runner.Context, atm_nombre: str):
    """
    :type context: behave.runner.Context
    :type atm_nombre: str
    """
    assert context.alerta is not None, "No se generó ninguna alerta"
    assert context.alerta["atm"] == atm_nombre.strip('"')
    assert context.alerta["nivel"] == "Crítico"
    assert context.alerta in context.operador.alertas, "La alerta no llegó al operador asignado"
    assert context.alerta["mensaje"] == context.text.strip(), (
        f"Esperado: {context.text.strip()!r} | Obtenido: {context.alerta['mensaje']!r}"
    )
