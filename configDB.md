## Configuración de PostgreSQL

### Descargar e Instalar PostgreSQL

1. Accede al sitio web oficial de PostgreSQL: Descargar PostgreSQL: [https://www.postgresql.org/download/](https://www.postgresql.org/download/)
2. Descarga la versión adecuada para tu sistema operativo y sigue las instrucciones de instalación.

### Configurar PostgreSQL

1. Durante la instalación, se te pedirá que establezcas una contraseña para el usuario "postgres". Recuerda esta contraseña, ya que la necesitarás para acceder al servidor PostgreSQL.

### Iniciar el Servidor PostgreSQL

1. Tras la instalación, busca y abre la aplicación "pgAdmin" en tu computadora.
2. En pgAdmin, selecciona el servidor PostgreSQL en el panel izquierdo y haz clic en el botón "Iniciar servidor" si aún no está iniciado.

### Configuración de DBeaver

### Descargar e Instalar DBeaver

1. Visita el sitio web oficial de DBeaver: Descargar DBeaver: [https://dbeaver.io/download/](https://dbeaver.io/download/)
2. Descarga la versión correspondiente a tu sistema operativo y sigue las instrucciones de instalación.

### Conectar DBeaver a PostgreSQL

1. Abre DBeaver después de la instalación.
2. En la ventana principal de DBeaver, haz clic en "Base de datos" en la barra de menú superior y selecciona "Nueva conexión a base de datos".
3. Elige "PostgreSQL" como tipo de base de datos.
4. Completa los detalles de conexión:
    * Host: localhost (si PostgreSQL está instalado en tu equipo)
    * Puerto: 5432 (puerto predeterminado de PostgreSQL)
    * Base de datos: (deja esto en blanco por ahora)
    * Usuario: postgres (o el nombre de usuario que configuraste durante la instalación)
    * Contraseña: Ingresa la contraseña que configuraste durante la instalación de PostgreSQL.
5. Haz clic en "Probar conexión" para verificar que la conexión sea exitosa.
6. Finalmente, haz clic en "Finalizar" para guardar la conexión.

![img2](img/dbeaver.png)

## Crear Tablas y Cargar Datos en PostgreSQL usando DBeaver

### Copiar y Pegar el Código SQL

1. Abre DBeaver y navega hasta tu conexión PostgreSQL en el panel izquierdo.
2. Haz clic derecho en la conexión y selecciona "Editor SQL" > "Nuevo editor SQL" para abrir un nuevo editor de consultas.
3. Copia el siguiente código SQL en tu portapapeles:

```sql
-- Crear la tabla Clientes
CREATE TABLE clientes (
  id_cliente SERIAL PRIMARY KEY,
  nombre VARCHAR(100)
);

-- Insertar datos en la tabla Clientes
INSERT INTO clientes (nombre)
VALUES (1, 'Ana Torres'), (2, 'Luis Rodríguez'), (3, 'María Gómez'), (4, 'Carlos Jiménez'), (5, 'Laura López');

-- Crear la tabla Peliculas
CREATE TABLE peliculas (
  id_pelicula SERIAL PRIMARY KEY,
  titulo VARCHAR(100)
);

-- Insertar datos en la tabla Peliculas
INSERT INTO peliculas (titulo)
VALUES (1, 'El Rey León'), (2, 'Vengadores'), (3, 'Toy Story'), (4, 'Titanic'), (5, 'Jurassic Park');

-- Crear la tabla Reservaciones
CREATE TABLE reservaciones (
  id_reservacion SERIAL PRIMARY KEY,
  id_cliente INT,
  id_pelicula INT,
  fecha_reservacion TIMESTAMP
);

-- Insertar datos en la tabla Reservaciones
INSERT INTO reservaciones (id_cliente, id_pelicula, fecha_reservacion)
VALUES
  (1, 3, '2023-07-01 19:00:00'), (2, 2, '2023-07-02 20:00:00'), (3, 1, '2023-07-03 21:00:00'),
  (4, 5, '2023-07-04 22:00:00'), (5, 3, '2023-07-05 23:00:00'), (1, 1, '2023-07-06 19:00:00'),
  (2, 3, '2023-07-07 20:00:00'), (3, 1, '2023-07-08 21:00:00'), (4, 4, '2023-07-09 22:00:00'),
  (5, 5, '2023-07-10 23:00:00'), (1, 1, '2023-07-11 19:00:00'), (2, 4, '2023-07-12 20:00:00'),
  (3, 5, '2023-07-13 21:00:00'), (4, 3, '2023-07-14 22:00:00'), (5, 3, '2023-07-15 23:00:00'),
  (1, 4, '2023-07-16 19:00:00'), (2, 5, '2023-07-17 20:00:00'), (3, 1, '2023-07-18 21:00:00'),
  (4, 2, '2023-07-19 22:00:00'), (5, 3, '2023-07-20 23:00:00');
```

### Ejecutar el Código SQL

1. Pega el código SQL copiado en el editor SQL de DBeaver.
2. Haz clic en el botón "Ejecutar declaración SQL" (Execute SQL Statement) en la barra de herramientas o presiona Ctrl + Enter en tu teclado.
3. DBeaver ejecutará el código SQL y mostrará los resultados en la parte inferior del editor.

### Verificar la Creación de Tablas y la Inserción de Datos

1. El mensaje en la parte inferior del editor debería indicar que las tablas se crearon correctamente ("CREATE TABLE ... SUCCESS") y que los datos se insertaron correctamente ("INSERT INTO ... SUCCESS").
2. Puedes verificar la estructura de las tablas creadas en el panel izquierdo de DBeaver. Expande la conexión a tu base de datos PostgreSQL y haz clic en la carpeta "Tablas". Deberías ver las tablas "clientes", "peliculas" y "reservaciones" listadas.
3. Para ver los datos insertados, puedes hacer clic derecho en una tabla y seleccionar "Abrir tabla" en el menú contextual. Esto abrirá una nueva vista en DBeaver que muestra los datos de la tabla.
4. También puedes usar consultas SQL para verificar y explorar los datos. Por ejemplo, puedes ejecutar la siguiente consulta para obtener todos los clientes de la tabla "clientes":

```sql
SELECT * FROM clientes;
```

5. Puedes ejecutar consultas similares para ver los datos de las tablas "peliculas" y "reservaciones".
