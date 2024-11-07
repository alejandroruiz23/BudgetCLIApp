# Budget APP [v 0.1]
A través del uso de arquitecturas de software y patrones de diseño se desarrolló una aplicación básica que permite correr en consola y contiene un menú interactivo que permite cargar ingresos y gastos para mantener un presupuesto. Automaticamente lleva el saldo actual de acuerdo con esos ingresos y gastos.

##  1. Arquitectura
Se hizo uso de la arquitectura por capas para garantizar la separación de responsabilidades de cada una de las partes de la aplicación desde la persistencia para el acceso a datos, el dominio o las reglas de negocio que establece la forma de manejo de la información y la capa de presentación que establece las condiciones para la presentación del menu y las funcionalidades asociadas.

![image](https://github.com/user-attachments/assets/a9b859f4-ea93-4ff2-8bb8-580566cceec4)

 
## 2. Patrones de diseño
Como parte de la implementación del aplicativo, se aplicaron dos patrones de diseño. El primero es el patron creacional Factory, que me permite elegir entre dos posibles bases de datos a usar segun las necesidades. Para este caso se planteó el uso de una base datos SQLlite y una base de datos PostgreSQL en donde estan las pruebas y producción respectivamente.
Adicionalmente se implmentó el patron Command para garantizar la separación y centralización de resposabilidades similares delegadas en un comando para garantizar que la solicitud se haga a través de objetos independientes.

## 3. Implementación

![image](https://github.com/user-attachments/assets/1decca11-7f99-47d4-92cd-799dba4c1d4f)

Como parte de la prueba, se agregó una estructura de datos que simula una base de datos para almacenar cada una de las transacciones realizadas para consultas futuras con fines ilustrativos.

A través del menú puedo registrar un ingreso, un gasto, conocer el saldo basado en los movimientos de ingresos y gastos, conocer todos los movimientos que incluyen ingresos y gastos, además permite ver movimientos asociados solo a ingresos o solo a gastos.


