#Problema 3

Se requiere una herramienta para auditar el inventario y decidir qué artículos necesitan ser reabastecidos. La información se encuentra en una matriz: [Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]. 

Requisitos de Desarrollo 
  - Matriz: Crear una matriz con al menos 5 artículos. 
  - Módulos: Se requiere un módulo (función) para determinar la cantidad exacta a pedir para un artículo. 
  - Lógica de Negocio: 
    ✓ Si el Stock Actual es menor al Stock Mínimo, la cantidad a pedir es la diferencia (Mínimo Requerido - Stock Actual). 
    ✓ Si el Stock Actual es suficiente (mayor o igual al Mínimo), la cantidad a pedir es cero. 
  - Salida: Imprimir una lista de pedidos que muestre el nombre del artículo y la cantidad exacta que debe ser solicitada.

# Sistema de Auditoría de Inventario

Proyecto desarrollado en Python utilizando:
- matrices
- funciones
- estructuras repetitivas
- interfaz gráfica con Tkinter

El sistema permite auditar el inventario y determinar qué artículos necesitan reabastecimiento.
