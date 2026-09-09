# Restaurante App

Base gráfica de la aplicación del restaurante para la Semana 13. Esta versión adapta la organización del proyecto docente Biblioteca App y se concentra en cargar y consultar productos y usuarios mediante una interfaz Tkinter.

## Estructura

```text
datos/
  productos.json
  usuarios.json
modelos/
  producto.py
  usuario.py
servicios/
  archivo_servicio.py
  restaurante_servicio.py
ui/
  login_view.py
  main_view.py
main.py
```

- `modelos/` representa productos y usuarios.
- `servicios/` lee los JSON y concentra la validación de acceso y las consultas.
- `ui/` contiene las vistas de login y del panel principal.
- `main.py` prepara las dependencias, crea una única ventana y coordina el cambio de vistas.

## Flujo implementado

Al iniciar se muestra el login. Las credenciales se validan mediante `RestauranteServicio`. Después del ingreso correcto, el panel permite consultar productos y usuarios cargados desde los JSON, muestra Ventas como funcionalidad pendiente y permite cerrar sesión para regresar al login dentro de la misma ventana.

## Ejecución

Requiere Python 3.10 o superior y Tkinter, incluido normalmente en la instalación estándar de Python para Windows.

```powershell
python main.py
```

Credenciales de ejemplo:

- Identificación: `C001`, contraseña: `1234`
- Identificación: `C002`, contraseña: `abcd`

La autenticación es únicamente una simulación pedagógica; no es un sistema de seguridad real. Las funcionalidades de ventas y administración permanecen para etapas posteriores.