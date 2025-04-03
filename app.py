import flet as ft

def main(page: ft.Page):
    page.title = "Clinica Cocula"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
        ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            width=350,
                            height=400,
                            padding=20,
                            border_radius=10,
                            bgcolor=ft.colors.SURFACE_VARIANT,
                            alignment=ft.alignment.center,
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.TextField(label="Usuario",width=300,)
                                        ]
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.TextField(label="Contraseña",width=300,password=True)
                                        ]
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.TextButton("Iniciar Sesion",width=300)
                                        ]
                                    )
                                ]
                            )
                        )
                    ], expand=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ], expand=True
        )
    )


ft.app(main, veiw=ft.WEB_BROWSER)
