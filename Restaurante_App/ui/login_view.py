from __future__ import annotations

import tkinter as tk
from tkinter import messagebox
from typing import Callable

from modelos.usuario import Usuario
from servicios.restaurante_servicio import RestauranteServicio


class LoginView(tk.Frame):
    def __init__(self, master: tk.Misc, servicio: RestauranteServicio, al_ingresar: Callable[[Usuario], None]) -> None:
        super().__init__(master, padx=32, pady=32)
        self.servicio = servicio
        self.al_ingresar = al_ingresar
        self._crear_controles()

    def _crear_controles(self) -> None:
        tk.Label(self, text="Restaurante App", font=("Segoe UI", 20, "bold")).pack(pady=(8, 4))
        tk.Label(self, text="Acceso simulado").pack(pady=(0, 24))

        formulario = tk.Frame(self)
        formulario.pack()
        tk.Label(formulario, text="Identificación").grid(row=0, column=0, sticky="w", pady=6)
        self.identificacion = tk.Entry(formulario, width=30)
        self.identificacion.grid(row=1, column=0, pady=(0, 10))
        tk.Label(formulario, text="Contraseña").grid(row=2, column=0, sticky="w", pady=6)
        self.contrasena = tk.Entry(formulario, width=30, show="*")
        self.contrasena.grid(row=3, column=0, pady=(0, 16))
        tk.Button(formulario, text="Ingresar", command=self._ingresar, width=28).grid(row=4, column=0)
        self.identificacion.focus_set()
        self.contrasena.bind("<Return>", lambda _evento: self._ingresar())

    def _ingresar(self) -> None:
        identificacion = self.identificacion.get().strip()
        contrasena = self.contrasena.get()
        if not identificacion or not contrasena:
            messagebox.showwarning("Datos incompletos", "Ingrese identificación y contraseña.")
            return
        usuario = self.servicio.validar_acceso(identificacion, contrasena)
        if usuario is None:
            messagebox.showerror("Acceso rechazado", "Las credenciales no son válidas.")
            return
        self.al_ingresar(usuario)