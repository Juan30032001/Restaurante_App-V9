from __future__ import annotations

import tkinter as tk
from typing import Callable

from modelos.usuario import Usuario
from servicios.restaurante_servicio import RestauranteServicio


class MainView(tk.Frame):
    def __init__(self, master: tk.Misc, servicio: RestauranteServicio, usuario: Usuario, cerrar_sesion: Callable[[], None]) -> None:
        super().__init__(master, padx=24, pady=24)
        self.servicio = servicio
        self.usuario = usuario
        self.cerrar_sesion = cerrar_sesion
        self._crear_controles()

    def _crear_controles(self) -> None:
        tk.Label(self, text=f"Bienvenido, {self.usuario.nombre}", font=("Segoe UI", 18, "bold")).pack(anchor="w")
        tk.Label(self, text="Panel principal del restaurante").pack(anchor="w", pady=(0, 16))

        acciones = tk.Frame(self)
        acciones.pack(fill="x")
        tk.Button(acciones, text="Productos", command=self.mostrar_productos).pack(side="left", padx=(0, 8))
        tk.Button(acciones, text="Usuarios", command=self.mostrar_usuarios).pack(side="left", padx=8)
        tk.Button(acciones, text="Ventas (pendiente)", command=self.mostrar_pendiente).pack(side="left", padx=8)
        tk.Button(acciones, text="Cerrar sesión", command=self.cerrar_sesion).pack(side="right")

        self.contenido = tk.Text(self, height=14, width=78, state="disabled", wrap="word")
        self.contenido.pack(fill="both", expand=True, pady=(20, 0))
        self.mostrar_productos()

    def _mostrar_lineas(self, titulo: str, lineas: list[str]) -> None:
        self.contenido.configure(state="normal")
        self.contenido.delete("1.0", tk.END)
        self.contenido.insert(tk.END, titulo + "\n\n")
        self.contenido.insert(tk.END, "\n".join(lineas) if lineas else "No hay registros cargados.")
        self.contenido.configure(state="disabled")

    def mostrar_productos(self) -> None:
        productos = self.servicio.listar_productos()
        self._mostrar_lineas("Productos registrados", [producto.mostrar_informacion() for producto in productos])

    def mostrar_usuarios(self) -> None:
        usuarios = self.servicio.listar_usuarios()
        self._mostrar_lineas("Usuarios registrados", [usuario.mostrar_informacion() for usuario in usuarios])

    def mostrar_pendiente(self) -> None:
        self._mostrar_lineas("Ventas", ["Esta funcionalidad se incorporará en una versión posterior."])