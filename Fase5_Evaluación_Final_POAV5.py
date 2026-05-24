#Importar la librería tkinter
import tkinter as tk

#alertas, confirmaciones
#from tkinter import messagebox

#tablas
from tkinter import ttk

# Funcion para calcular la cantidad a solicitar
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Matriz con los articulos
inventario = [
    [101, "PS/PD CARTAGO AD GRIS CLARO 31X60 PRIM 1.86 SLO", 986, 100],
    [102, "PS BELTRAN BLANCO 50X50 PRIM 2.75 SLO", 300, 100],
    [103, "PS/PD MACERATA AVELLANA 30X60 PRIM 1.80 ITA", 500, 100],
    [104, "PS MINERALIA CYR 58.4X118.4 PRIM 1.38 ITA", 80, 100],
    [105, "PS EXTERIOR CROACIA MIX 60X60 PRIM 2.16 EUR", 200, 100],
    [106, "PD ARA BLANCO 30.5X45 PRIM 1.78 ALF", 96, 100]
]


# Diseño de la ventana
ventana = tk.Tk()
ventana.title("Sistema de Auditoría de Inventario")
ventana.geometry("1080x550")
ventana.config(bg="#f4f6f9")

titulo = tk.Label(
    ventana,
    text="SISTEMA DE AUDITORÍA DE INVENTARIO",
    font=("Arial", 24, "bold"),
    bg="#f4f6f9",
    fg="#cd1417"
)

titulo.pack(pady=15)


# Creacion de la tabla
frame_tabla = tk.Frame(ventana)
frame_tabla.pack(pady=10)
scroll_y = tk.Scrollbar(frame_tabla)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

tabla = ttk.Treeview(
    frame_tabla,
    yscrollcommand=scroll_y.set,
    height=10
)

scroll_y.config(command=tabla.yview)

tabla["columns"] = ("Codigo","Articulo","StockActual","StockMinimo","Estado","CantidadPedir")

tabla.column("#0", width=0, stretch=tk.NO)

tabla.column("Codigo", anchor=tk.CENTER, width=90)
tabla.column("Articulo", anchor=tk.CENTER, width=300)
tabla.column("StockActual", anchor=tk.CENTER, width=120)
tabla.column("StockMinimo", anchor=tk.CENTER, width=140)
tabla.column("Estado", anchor=tk.CENTER, width=200)
tabla.column("CantidadPedir", anchor=tk.CENTER, width=150)

tabla.heading("#0", text="")

tabla.heading("Codigo", text="Código")
tabla.heading("Articulo", text="Artículo")
tabla.heading("StockActual", text="Stock actual")
tabla.heading("StockMinimo", text="Stock mínimo")
tabla.heading("Estado", text="Estado")
tabla.heading("CantidadPedir", text="Cantidad a pedir")

tabla.tag_configure("reabastecer", background="#f8d7da")
tabla.tag_configure("suficiente", background="#d4edda")


# Acumuladores
total_articulos = 0
articulos_reabastecer = 0
total_unidades_pedir = 0


# Ciclo que recorre la matriz
for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)
    total_articulos += 1

    # Verificar estado
    if cantidad_pedir > 0:
        estado = "Requiere reabastecimiento"
        color = "reabastecer"

        articulos_reabastecer += 1
        total_unidades_pedir += cantidad_pedir
    else:
        estado = "Stock suficiente"
        color = "suficiente"

    # Insertar datos en la tabla
    tabla.insert(
        parent="",
        index="end",
        values=(codigo, nombre, stock_actual, stock_minimo, estado, cantidad_pedir),
        tags=(color,)
    )
tabla.pack()


# Resumen
frame_resumen = tk.Frame(
    ventana,
    bg="#f4f6f9"
)
frame_resumen.pack(pady=20)

label_total = tk.Label(
    frame_resumen,
    text=f"Total de artículos revisados: {total_articulos}",
    font=("Arial", 12, "bold"),
    bg="#f4f6f9"
)
label_total.pack()

label_reabastecer = tk.Label(
    frame_resumen,
    text=f"Artículos que requieren pedido: {articulos_reabastecer}",
    font=("Arial", 12, "bold"),
    bg="#f4f6f9"
)
label_reabastecer.pack()

label_unidades = tk.Label(
    frame_resumen,
    text=f"Total de unidades a pedir: {total_unidades_pedir}",
    font=("Arial", 12, "bold"),
    bg="#f4f6f9"
)
label_unidades.pack()

boton_salir = tk.Button(
    ventana,
    text="Cerrar Sistema",
    command=ventana.destroy,
    bg="#cd1417",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=15,
    pady=5
)
boton_salir.pack(pady=10)

ventana.mainloop()