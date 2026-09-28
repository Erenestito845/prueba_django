# Catálogo Django

Proyecto Django con dos catálogos independientes:

- `juegosApp`: muestra la página de inicio y el catálogo de juegos.
- `hardwareApp`: muestra la página de inicio y un catálogo de componentes de hardware.

Los datos de ambos catálogos se almacenan en archivos JSON dentro de `data/`. Las vistas los leen y envían a sus respectivas plantillas HTML.

## Requisitos

- Python 3.12 o superior
- Django 5.2
- `python-dotenv`

## Instalación

Activa el entorno virtual del proyecto e instala las dependencias:

```bash
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Configuración

La configuración se encuentra en `config/settings.py`. Las variables se cargan desde `.env`, que no se debe subir a Git. El proyecto usa SQLite por defecto para el desarrollo local.

Para pasar a MySQL en AWS, cambia `DB_ENGINE` y completa el nombre, usuario, contraseña y endpoint de tu base de datos. No guardes credenciales reales en el repositorio. Después de configurar la base, ejecuta las migraciones con `python manage.py migrate`.

Variables disponibles (la plantilla está en `.env.example`):

```env
SECRET_KEY=una-clave-secreta-generada-para-el-entorno
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_ENGINE=django.db.backends.mysql
DB_NAME=nombre_de_la_base
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=endpoint-de-la-base-de-datos
DB_PORT=3306
```

## Ejecución

Desde la raíz del proyecto:

```bash
python manage.py runserver
```

Rutas principales:

| Ruta | Descripción |
| --- | --- |
| `/` | Inicio del catálogo de juegos |
| `/catalogo/` | Lista de juegos leída desde `data/juegos.json` |
| `/hard/` | Inicio del catálogo de hardware |
| `/hard/componentes/` | Lista de componentes leída desde `data/hardware.json` |
| `/admin/` | Panel de administración de Django |

## Estructura relevante

```text
config/          Configuración global y rutas principales
juegosApp/       Vistas y rutas del catálogo de juegos
hardwareApp/     Vistas y rutas del catálogo de hardware
data/            Archivos JSON con los datos mostrados
templates/       Plantillas HTML
static/          CSS, JavaScript e imágenes
```
