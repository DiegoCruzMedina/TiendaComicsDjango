# Tienda de Comics - Proyecto Django

Este es un proyecto funcional en Django para la venta de cómics de DC, Marvel y mangas.

--- --- --- --- ---

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/DiegoCruzMedina/TiendaComicsDjango.git
   ```

2. Crear y activar un ambiente virtual:
   ```bash
   py -m venv myvenv
   .\myvenv\Scripts\Activate
   ```

3. Actualizar pip dentro del ambiente virtual:
   ```bash
   py -m pip install --upgrade pip
   ```

4. Instalar los requerimientos del proyecto desde `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

5. Ejecutar el servidor para iniciar la aplicación:
   ```bash
   python manage.py runserver
   ```

--- --- --- --- ---

### Funcionalidades del Proyecto

- **Autenticación**: Permite el inicio de sesión y registro de usuarios. Los usuarios registrados tienen acceso a funcionalidades adicionales.
  
- **Carrito**: Los usuarios pueden agregar cómics al carrito para comprar.
  
- **Comics**: Gestiona los cómics disponibles para la venta. Los cambios se reflejan automáticamente en la interfaz web.
  
- **Contacto**: Los usuarios pueden enviar consultas mediante un formulario que se guarda en la base de datos para que los administradores respondan.
  
- **Órdenes**: Gestiona las compras realizadas por los usuarios, quienes pueden ver el historial de sus compras en su interfaz de usuario.
  
- **TiendaWeb**: Gestiona archivos estáticos como CSS, JS, imágenes, etc., y proporciona bases extensibles para la interfaz de usuario.

- **TiendaComics**: Proyecto carpeta principal donde instalamos apps y creamos urls.

--- --- ---

**Nota**: Asegúrate de configurar correctamente tu ambiente virtual antes de ejecutar el proyecto.

--- --- ---

