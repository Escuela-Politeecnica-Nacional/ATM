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
    context.atm = ATM(atm_nombre)
    context.operador.asignar_atm(context.atm)
    assert context.atm.operdor_asignado == context.operador

@step("el cajero {atm_nombre} tiene establecido")
def step_impl(context: behave.runner.Context, atm_nombre: str):
    """
    :type context: behave.runner.Context
    :type atm_nombre: str
    """
    raise NotImplementedError(u'STEP: Y el cajero "ATM-A" tiene establecido')


@step("actualmente cuenta con 5 billetes de 20 dólares y 2 billetes de 10 dólares")
def step_impl(context: behave.runner.Context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Y actualmente cuenta con 5 billetes de 20 dólares y 2 billetes de 10 dólares')


@step("se verifica la capacidad actual")
def step_impl(context: behave.runner.Context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Cuando se verifica la capacidad actual')


@step("debe enviar la alerta de nivel crítico para el {atm_nombre} al operador asignado con el siguiente mensaje:")
def step_impl(context: behave.runner.Context, atm_nombre: str):
    """
    :type context: behave.runner.Context
    :type atm_nombre: str
    """
    raise NotImplementedError(
        u'STEP: Entonces debe enviar la alerta de nivel crítico para el "ATM-A" al operador asignado con el siguiente mensaje:')