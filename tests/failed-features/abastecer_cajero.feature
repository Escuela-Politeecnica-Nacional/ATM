# language: es
Feature: Abastecimiento y control de inventario de dinero en el ATM
  Como operador autorizado del Banco del Pacífico
  Quiero recargar el monto máximo de efectivo en los casetes del cajero automático
  Para garantizar que los clientes dispongan de billetes y puedan realizar retiros de forma continua 24/7

  Background:
    Given que el operador del banco se ha autenticado exitosamente en el panel de mantenimiento del ATM
    And el cajero se encuentra en modo de servicio/mantenimiento

  Scenario: Recarga exitosa de efectivo en los casetes del ATM
    Given que el nivel actual de efectivo en el cajero está por debajo del umbral operativo
    When el operador ingresa las denominaciones y la cantidad de billetes añadidos a cada casete
    And el sistema valida la coincidencia física con el arqueo ingresado
    Then el sistema debe actualizar el inventario interno de dinero al monto máximo configurado
    And el sistema debe registrar la transacción de abastecimiento en la bitácora de auditoría del cajero

  Scenario: Intento de recarga superando la capacidad máxima de los casetes
    Given que los casetes del cajero tienen una capacidad límite de almacenamiento
    When el operador intenta registrar una cantidad de billetes superior a la capacidad física permitida
    Then el sistema debe rechazar la operación de abastecimiento
    And el sistema debe mostrar un mensaje de error indicando que se excede la capacidad máxima del casete