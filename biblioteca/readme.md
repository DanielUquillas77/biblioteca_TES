# Biblioteca de Libros

Esta aplicación web permite gestionar una biblioteca de libros. Los usuarios pueden:
- **Listar y buscar** libros (por título, autor o género).
- **Agregar** nuevos libros.
- **Editar** la información de libros existentes.
- **Eliminar** libros (incluyendo eliminación múltiple).
- Acceder a la información de los libros mediante una **API RESTful**.

La aplicación utiliza **Flask** como framework, **SQLite** como base de datos y **Flask-RESTful** para exponer la API.

## Características

- **Interfaz Web:**
  - Listado de libros con opción de búsqueda.
  - Formulario de agregar libros con el campo "Año de Publicación" con selector de año.
  - Formulario de edición de libros.
  - Selección múltiple de registros para eliminación.
  - Botones de edición y eliminación ubicados fuera de la tabla de registros.
- **API RESTful:**
  - `GET /api/books`: Lista todos los libros.
  - `GET /api/books/<id>`: Obtiene la información de un libro específico.
  - `POST /api/books`: Agrega un nuevo libro (requiere datos en formato JSON).
  - `PUT /api/books/<id>`: Actualiza la información de un libro.
  - `DELETE /api/books/<id>`: Elimina un libro.

## Estructura del Proyecto

biblioteca/ │
 ├── app.py # Archivo principal: rutas web y API RESTful 
 ├── config.py # Configuración de la base de datos 
 ├── models.py # Modelo de datos (Book) 
 ├── templates/ # Plantillas HTML 
 │ ├── index.html # Listado y búsqueda de libros 
 │ ├── add_book.html # Formulario para agregar libros  
 │ └── edit_book.html # Formulario para editar libros 
 └── static/ # Archivos estáticos (CSS) 
    ├── style_index.css # Estilos para la página de listado 
    ├── style_add_book.css # Estilos para la página de agregar libro 
    └── style_edit_book.css # Estilos para la página de edición


## Instalación

1. **Clona o descarga el proyecto** en tu máquina local.

2. **Navega al directorio del proyecto:**

    cd ruta/al/directorio/biblioteca
    (Reemplaza "ruta/al/directorio" con la ruta real en tu sistema)

    (Si estás en Windows, asegúrate de usar el símbolo del sistema o
    terminal de comandos para ejecutar comandos de terminal)

3. **Instala las dependencias necesarias:**

    pip install flask flask-sqlalchemy flask-restful

4. **Ejecuta la aplicación:**

    python app.py
    (Al ejecutar el comando, deberías ver un mensaje similar a:
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)*)

5. **Accede a la aplicación:**

Abre tu navegador web y dirígete a:
http://127.0.0.1:5000/

6. **Uso de la Interfaz Web:**
- Puedes agregar libros mediante el formulario de "Agregar Libro".
    Haz clic en "Agregar Nuevo Libro" para acceder al formulario.

- Puedes buscar libros por título o autor en la página principal.
    Utiliza la barra de búsqueda para filtrar libros por título, autor o género.

- Puedes editar o eliminar libros mediante sus respectivos enlaces en la página principal.
    Selecciona un único registro mediante checkbox y haz clic en "Editar" si deseas modificar el registro o
    haz clic en "Eliminar" para eliminar el registro seleccionado.

7. **Notas adicionales**

    **Base de Datos:**
    La base de datos SQLite se crea automáticamente al iniciar la aplicación por primera vez en el archivo library.db en el directorio raíz del proyecto.

    **Estilos CSS Diferenciados:**
    Cada página utiliza un archivo CSS distinto ubicado en la carpeta static para personalizar su apariencia.

    **Selector de Año:**
    En los formularios de agregar y editar libro, el campo "Año de Publicación" utiliza un selector (Datepicker) configurado para mostrar únicamente el año.
    Esto facilita la selección del año de publicación para cada libro.

8. **Solucion de Problemas**

    - La aplicación no se inicia:
        Asegúrate de estar en el directorio correcto y de haber instalado todas las dependencias.

    - No se visualizan los estilos:
        Verifica que las rutas de los archivos CSS en las plantillas HTML sean correctas y que los archivos se encuentren en la carpeta static.

    - Problemas con la base de datos:
        Si encuentras errores relacionados con la base de datos, elimina el archivo library.db y vuelve a ejecutar la aplicación para que se cree nuevamente.

    - Problemas con la conexión a la base de datos:
        Asegúrate de que la ruta a la base de datos sea correcta y que no
        esté bloqueada por algún firewall o configuración de seguridad.

    