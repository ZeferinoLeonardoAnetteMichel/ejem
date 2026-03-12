import flet as ft
def main(page: ft.Page):
    page.title = "Inicio de sesion"
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    titulo = ft.Text("Iniciar Sesión", size=30, weight="bold",color="purple")
    
    usuario = ft.TextField(
        label="Usuario",
        width=300,
        border_color="purple"
        )
    
    password =  ft.TextField(
            label="Contraseña",
            password=True,
            can_reveal_password=True,
            border_color="purple"
        )
    
    boton_login = ft.Button(
        "Iniciar sesion",
        width=300,
        color="white",
        bgcolor="purple50"  
    )
    olvido = ft.Text("¿Olvidaste tu contraseña?", size=20, weight="italic",color="purple150")


    contenedor = ft.Column(
        [
            titulo,
            usuario,
            password,
            boton_login,
            olvido
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(contenedor)

ft.app(target=main)
