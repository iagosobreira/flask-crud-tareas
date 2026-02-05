# Flask Tareas

Una aplicación web de gestión de tareas desarrollada con Flask que permite a los usuarios registrarse, iniciar sesión y gestionar sus tareas personales.

## Características

- **Autenticación de usuarios**: Registro, inicio de sesión y cierre de sesión
- **Gestión de tareas**: Crear, eliminar y marcar tareas como completadas
- **Base de datos**: Utiliza PostgreSQL con SQLAlchemy
- **Sesiones**: Manejo de sesiones de usuario con Flask
- **Interfaz web**: HTML5 con CSS para la interfaz de usuario

## Tecnologías Utilizadas

- **Backend**: Flask 3.1.2
- **Base de datos**: PostgreSQL con SQLAlchemy 2.0.46
- **Frontend**: HTML5, CSS3
- **ORM**: Flask-SQLAlchemy 3.1.1
- **Variables de entorno**: python-dotenv 1.2.1

## Estructura del Proyecto

```
Flask_Tareas/
├── app/                           # Aplicación principal
│   ├── app.py                     # Aplicación principal de Flask
│   ├── config.py                  # Configuración de la aplicación
│   ├── extensions.py              # Extensiones de Flask
│   ├── .env.example               # Ejemplo de variables de entorno
│   ├── main/                      # Módulo de rutas principales
│   │   └── routes.py
│   ├── tareas/                    # Módulo de gestión de tareas
│   │   ├── routes.py              # Rutas de gestión de tareas
│   │   └── services.py            # Lógica de negocio de tareas
│   ├── usuario/                   # Módulo de autenticación
│   │   ├── routes.py              # Rutas de usuario
│   │   └── services.py            # Pequeña lógica usuario
│   ├── templates/                 # Plantillas HTML
│   │   ├── layout.html            # Plantilla base
│   │   ├── index.html             # Página de inicio/login
│   │   ├── registro.html          # Formulario de registro
│   │   └── area.html              # Área personal del usuario
│   └── static/                    # Archivos estáticos
│       └── css/
│           ├── login.css          # Estilos para login
│           └── area.css           # Estilos para area
├── README.md                      # Documentación del proyecto
└── requirements.txt               # Dependencias del proyecto
```

## Instalación

1. Clona el repositorio:
```bash
git clone <URL-del-repositorio>
cd Flask_Tareas
```

2. Crea un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Configura las variables de entorno:
Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:
```
SECRET_KEY=tu_clave_secreta_aqui
DATABASE_URL=postgresql://usuario:password@localhost/nombre_db
```

5. Ejecuta la aplicación:
```bash
python app/app.py
```

## Uso

1. Abre tu navegador y accede a `http://localhost:5000`
2. Registra una nueva cuenta o inicia sesión
3. Una vez autenticado, podrás:
   - Agregar nuevas tareas
   - Marcar tareas como completadas
   - Eliminar tareas
   - Ver todas tus tareas en el área personal

## Rutas Principales

- `/` - Página de inicio y login
- `/crear_registro` - Registro de nuevos usuarios (POST)
- `/login` - Inicio de sesión (POST)
- `/logout` - Cierre de sesión
- `/area` - Área personal del usuario con sus tareas
- `/agregar_tarea` - Agregar nueva tarea (POST)
- `/eliminar_tarea` - Eliminar tarea (POST)
- `/realizar_tarea` - Marcar tarea como completada (POST)

## Base de Datos

La aplicación utiliza PostgreSQL con tablas principales:
- `usuarios`: Almacena información de los usuarios
- `tareas`: Almacena las tareas de cada usuario

## Esquema de la base de datos

```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contrasena TEXT NOT NULL,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE tareas (
    id SERIAL PRIMARY KEY,
    tarea TEXT NOT NULL,
    realizada BOOLEAN DEFAULT FALSE,
    id_usuario INTEGER REFERENCES usuarios(id)
);
```

## Contribución

1. Fork del proyecto
2. Crear una rama para la nueva característica
3. Realizar los cambios necesarios
4. Enviar un pull request

## Licencia

Este proyecto está bajo la Licencia MIT.