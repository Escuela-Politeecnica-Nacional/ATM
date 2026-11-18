# Proyecto - ATM

## Visión del Producto
**Para** clientes de Banco del Pacífico
**quiénes** necesitan acceder a efectivo y realizar operaciones financieras básicas fuera del horario bancario tradicional,
**el** Cajero Automático (ATM) **es un** canal de autoservicio financiero de alta disponibilidad
**que** permite realizar retiros de dinero y consultas de forma autónoma, segura y rápida.
**A diferencia de** las ventanillas físicas tradicionales, que están sujetas a horarios de atención limitados, tiempos de espera prolongados y trámites manuales en papel, **nuestro producto** ofrece disponibilidad ininterrumpida (24/7), transacciones seguras mediante autenticación con tarjeta y PIN, y una interfaz de usuario optimizada para minimizar los tiempos de operación.

## Objetivos 

- Obj 1: Mantener un servicio de transacciones ATM disponible 24/7 junto con mecanismos para su disponibilidad operativa. 

- Obj 2: Incluir métodos de seguridad física y lógica en cada transacción. 

- Obj 3: Proveer mecanismos eficientes para capturar la retroalimentación del usuario final sobre la calidad del servicio, permitiendo una mejora continua.

## Capacidades / Capabilities
// Sustantivos y no deben ir RNF, check para verificar

| Descripción / Actividad | Objetivo 1 | Objetivo 2 | Objetivo 3 |
| :--- | :---: | :---: | :---: |
| 1. Monitoreo activo del cajero | X | | |
| 2. Autenticación con tarjeta ATM | | X | |
| ~~Respuesta ante incidentes~ | | X | |
| 3. Reporte de incidente | | X | |
| 4. Alerta de mantenimiento preventivo | X | | |
| 5. Registro y auditoria de transacciones | | X | |
| 6. Feedback de los usuarios mediante encuestas | | | X |

 - Acceso continuo de los clientes al sistema financiero mediante la 
autenticación segura por tarjeta y PIN, operando sin intervención de personal humano.

-  Controlar, auditar y administrar el inventario interno de billetes y efectivo dentro del dispositivo, incluyendo las alertas de niveles y el registro de retiros o abastecimientos.

- Monitorear el estado físico del cajero, cifrar las comunicaciones con el núcleo bancario y prevenir manipulaciones fraudulentas.

- Recopilar datos de satisfacción y reportes breves de incidencias por parte del usuario tras finalizar una transacción.

## Características / Features

- Módulo de autenticación de tarjeta y validación de PIN encriptado.

- Flujo interactivo de selección de montos de retiro rápido y montos personalizados.

- Sistema de control y registro automático de billetes dispensados por denominación.

- Interfaz de control para el personal autorizado (operadores/blindadas) para el abastecimiento, arqueo y retiro de dinero físico.

- Alerta automatizada por niveles críticos de efectivo (bajo inventario).

- Encriptación de extremo a extremo para la comunicación de datos transaccionales con el Core Bancario de Banco del Pacífico.

- Bloqueo automático de sesión e invalidación de tarjeta ante intentos fallidos consecutivos de PIN.

- Pantalla final de calificación del servicio (estrellas/escala de satisfacción) opcional para el cliente.