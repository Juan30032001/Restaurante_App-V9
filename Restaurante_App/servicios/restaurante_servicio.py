from __future__ import annotations

from typing import Iterable

from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:
    """Coordina los datos que necesita la interfaz gráfica del restaurante."""

    def __init__(self, productos: Iterable[Producto | dict[str, object]], usuarios: Iterable[Usuario | dict[str, object]]) -> None:
        self._productos = [self._convertir_producto(producto) for producto in productos]
        self._usuarios = [self._convertir_usuario(usuario) for usuario in usuarios]

    @staticmethod
    def _convertir_producto(producto: Producto | dict[str, object]) -> Producto:
        return producto if isinstance(producto, Producto) else Producto.from_dict(producto)

    @staticmethod
    def _convertir_usuario(usuario: Usuario | dict[str, object]) -> Usuario:
        return usuario if isinstance(usuario, Usuario) else Usuario.from_dict(usuario)

    def validar_acceso(self, identificacion: str, contrasena: str) -> Usuario | None:
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion.strip() and usuario.contrasena == contrasena:
                return usuario
        return None

    def listar_productos(self) -> list[Producto]:
        return list(self._productos)

    def listar_usuarios(self) -> list[Usuario]:
        return list(self._usuarios)