import flet as ft

def sumar_numeros(num_1,num_2,num_3,num_4,num_5,num_6, result_text):
    try:
        num1=float(num_1.value.strip())
        num2=float(num_2.value.strip())
        num3=float(num_3.value.strip())
        num4=float(num_4.value.strip())
        num5=float(num_5.value.strip())
        num6=float(num_6.value.strip())
        suma = num1 + num2 + num3 + num4 + num5 + num6
        result_text.value = f"La suma es: {suma}"
    except ValueError:
        result_text.value = "Error al sumar los números."
    
    

def main(page: ft.Page):
    page.title = "Suma de 6 números"
    
    # Creación de los 6 campos de texto
    num_1 = ft.TextField(label="ingresatu tu 1er num")
    num_2 = ft.TextField(label="ingresatu tu 2do num")
    num_3 = ft.TextField(label="ingresatu tu 3er num")
    num_4 = ft.TextField(label="ingresatu tu 4to num")
    num_5 = ft.TextField(label="ingresatu tu 5to num")
    num_6 = ft.TextField(label="ingresatu tu 6to num") 
    # Texto para mostrar el resultado
    
    result_text = ft.Text("Resultado:")
    
    # Botón para realizar la suma
    sumar_button = ft.ElevatedButton("Suma",
                                    on_click=lambda e:boton(e))

    def boton(e):
        sumar_numeros(num_1,num_2,num_3,num_4,num_5,num_6, result_text),
        page.update()
    # Añadir los campos de texto y el botón a la página
    page.add(
       ft.Column(controls=[
          ft.Row(controls=[num_1,num_2,num_3,],alignment="centro"),
          ft.Row(controls=[num_4,num_5,num_6],alignment="centro"),
       ft.Row(controls=[result_text],alignment="centro"),
       ft.Row(controls=[sumar_button],alignment="center") 
       ]),
    )

ft.app(target=main)
