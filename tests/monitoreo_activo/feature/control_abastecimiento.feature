# language: es
Característica: Alerta automatizada por niveles críticos de efectivo (bajo inventario).
  Como operador autorizado del Banco del Pacífico
  Quiero recibir notificaciones sobre el estado del monto crítico definido de los cajeros asignados
  Para notificar a los dispensadores #Beneficio

#  Escenario:  El cajero no tiene monto suficiente
#    Dado que el operador autorizado está registrado en el sistema
#    Y el cajero A está asignado a Juan
#    Y Juan está disponible
#    Y el cajero está activo
#    Y el monto mínimo es 200$
#    Y con capacidad máxima de 1 500$
#    Cuando el cajero está por debajo del monto mínimo
#    Entonces el cajero debe enviar la notificación al operador autorizado sobre la recomposición del monto crítico definido


#  Esquema del escenario: : Notificar al operador cuando el efectivo del cajero cae por debajo del mínimo
#        Dado que Juan es un operador autorizado y tiene asignado el cajero "ATM-A", activo y conectado
#        Y el cajero tiene un mínimo de 200 dólares y capacidad para 40 billetes de 20 dólares y 20 billetes de 10 dólares
#        Y dispone inicialmente de 10 billetes de 20 dólares y 2 billetes de 10 dólares, equivalentes a 220 dólares
#        Cuando el cajero confirma un retiro exitoso de 40 dólares mediante 2 billetes de 20 dólares
#        Entonces el sistema debe actualizar el efectivo disponible a 180 dólares
#        Y debe registrar una alerta de nivel crítico para "ATM-A" y notificar a Juan en su bandeja de alertas
#        Y debe informar que quedan 8 billetes de 20 dólares y 2 de 10 dólares
#        Y debe indicar que se requieren 32 billetes de 20 dólares y 18 de 10 dólares, equivalentes a 820 dólares, para completar su capacidad
#
#     Ejemplos:
#            | inicial | retiro | restante | estado  | alertas |
#            | 220     | 40     | 180      | Crítico | 1       |
#            | 260     | 60     | 200      | Normal  | 0       |
#            | 280     | 40     | 240      | Normal  | 0       |





      Escenario: Notificar al operador cuando el efectivo del cajero cae por debajo del mínimo
        Dado un operador autorizado que tiene asignado el cajero "ATM-A", activo y conectado
        Y el cajero "ATM-A" tiene establecido
          | denominacion        | cantidad_maxima | monto_mínimo |
          | 20 dólares          | 40              | 10           |
          | 10 dólares          | 20              | 5            |
        Y actualmente cuenta con 5 billetes de 20 dólares y 2 billetes de 10 dólares
        Cuando se verifica la capacidad actual
        Entonces debe enviar la alerta de nivel crítico para el "ATM-A" al operador asignado con el siguiente mensaje:
          """
          Se requieren 35 billetes de 20 dólares y 18 de 10 dólares
          """

#     Ejemplos:
#            | inicial | retiro | restante | estado  | alertas |
#            | 220     | 40     | 180      | Crítico | 1       |
#            | 260     | 60     | 200      | Normal  | 0       |
#            | 280     | 40     | 240      | Normal  | 0       |

