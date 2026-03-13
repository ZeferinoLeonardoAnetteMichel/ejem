import flet as ft
def main(page: ft.Page):
    page.title = "Inicio de sesion"
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    titulo = ft.Text("Iniciar Sesión", size=30, weight="bold",color="purple")
    
    
    usuario = ft.TextField(
        label="Usuario",
        icon=ft.Icons.PERSON,
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
        bgcolor="purple"  
    )
    olvido = ft.TextButton(
    content="¿Olvidaste tu contraseña?",
    icon_color=ft.Colors.PURPLE,
)

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

    page.add(contenedor)

ft.app(target=main)
