# Script de Configuración de Proyecto con Arquitectura Limpia

Este script (`create_clean_architecture.py`) es una utilidad en Python diseñada para automatizar la creación de una estructura de proyecto siguiendo los principios de **Arquitectura Limpia** (Clean Architecture). Genera una jerarquía de carpetas y archivos esenciales para un proyecto en Python, optimizado para frameworks como FastAPI, con el objetivo de garantizar un diseño modular, escalable y listo para entornos de desarrollo y despliegue. La estructura está diseñada para ser replicada por cada módulo del proyecto, permitiendo una organización clara y consistente para aplicaciones con múltiples módulos.

## Propósito
El script crea una estructura de directorios estandarizada para un proyecto en Python basado en Arquitectura Limpia, separando las responsabilidades en capas: **dominio**, **infraestructura** y **presentación**. Además, incluye un directorio `tests` con subdirectorios para pruebas unitarias e integración, y genera archivos esenciales como `.gitignore`, `.env`, `dockerfile`, `.dockerignore`, `README.md` y `requirements.txt`. Esta estructura debe replicarse para cada módulo del proyecto, asegurando que cada módulo mantenga su propia independencia y organización.

## Características
- Crea una estructura de directorios con las siguientes capas:
  - **Dominio**: Contiene entidades, repositorios (interfaces) y casos de uso.
  - **Infraestructura**: Incluye configuraciones de base de datos, implementaciones concretas de repositorios y utilidades de logging.
  - **Presentación**: Gestiona puntos de acceso API u otras interfaces.
  - **Tests**: Incluye subdirectorios para pruebas unitarias (`unitarios`) y de integración (`integracion`).
- Genera archivos `__init__.py` vacíos para convertir los directorios en paquetes de Python.
- Crea archivos clave en la raíz del proyecto y en `src/`:
  - `.gitignore`: Configurado para proyectos de Python, importado desde `archivoGitIgnore`.
  - `main.py`: Punto de entrada para FastAPI, importado desde `archivoMain`.
  - `.env`: Para variables de entorno.
  - `dockerfile` y `.dockerignore`: Para contenedorización con Docker.
  - `README.md`: Documentación básica del proyecto.
  - `requirements.txt`: Lista de dependencias del proyecto.
  - `config.py`: Para configuraciones del proyecto.
- Añade un mensaje de confirmación al finalizar la creación de la estructura.
- **Modularidad**: La estructura de `src/` (con `domain`, `infrastructure`, `presentation`) debe replicarse para cada módulo del proyecto, organizando cada módulo de manera independiente dentro de `src/`.

## Uso
1. **Ejecutar el Script**:
   ```bash
   python create_clean_architecture.py
   ```
2. **Ingresar el Nombre del Proyecto**:
   - Cuando se solicite, introduce el nombre deseado para el proyecto.
   - Si no se proporciona un nombre (es decir, presionas Enter), se usará el nombre predeterminado `FASTAPI_CLEANARCHITECTURE`.
3. **Resultado**:
   - El script crea una carpeta con el nombre del proyecto especificado, conteniendo la estructura de Arquitectura Limpia.
   - Se muestra un mensaje de confirmación: `Estructura básica de Clean Architecture creada para el proyecto '<project_name>'`.

## Estructura Generada
El script genera el siguiente árbol de directorios para el proyecto base:
```
<project_name>/
├── .dockerignore
├── .env
├── .gitignore
├── dockerfile
├── README.md
├── requirements.txt
├── src/
│   ├── config.py
│   ├── main.py
│   ├── __init__.py
│   ├── domain/
│   │   ├── entities/
│   │   │   └── __init__.py
│   │   ├── repositories/
│   │   │   └── __init__.py
│   │   ├── use_cases/
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── infrastructure/
│   │   ├── database/
│   │   │   └── __init__.py
│   │   ├── repositories/
│   │   │   └── __init__.py
│   │   ├── logs/
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── presentation/
│   │   ├── api/
│   │   │   └── __init__.py
│   │   └── __init__.py
├── tests/
│   ├── integracion/
│   │   └── __init__.py
│   ├── unitarios/
│   │   └── __init__.py
│   └── __init__.py
```

### Replicación por Módulo
Para proyectos con múltiples módulos, la estructura dentro de `src/` debe replicarse para cada módulo. Por ejemplo, si el proyecto tiene módulos como `users` y `products`, la estructura se organizaría así:

```
<project_name>/
├── .dockerignore
├── .env
├── .gitignore
├── dockerfile
├── README.md
├── requirements.txt
├── src/
│   ├── config.py
│   ├── main.py
│   ├── __init__.py
│   ├── users/
│   │   ├── domain/
│   │   │   ├── entities/
│   │   │   │   └── __init__.py
│   │   │   ├── repositories/
│   │   │   │   └── __init__.py
│   │   │   ├── use_cases/
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   ├── infrastructure/
│   │   │   ├── database/
│   │   │   │   └── __init__.py
│   │   │   ├── repositories/
│   │   │   │   └── __init__.py
│   │   │   ├── logs/
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   ├── presentation/
│   │   │   ├── api/
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── products/
│   │   ├── domain/
│   │   │   ├── entities/
│   │   │   │   └── __init__.py
│   │   │   ├── repositories/
│   │   │   │   └── __init__.py
│   │   │   ├── use_cases/
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   ├── infrastructure/
│   │   │   ├── database/
│   │   │   │   └── __init__.py
│   │   │   ├── repositories/
│   │   │   │   └── __init__.py
│   │   │   ├── logs/
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   ├── presentation/
│   │   │   ├── api/
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   └── __init__.py
├── tests/
│   ├── integracion/
│   │   └── __init__.py
│   ├── unitarios/
│   │   └── __init__.py
│   └── __init__.py
```

En este ejemplo, los módulos `users` y `products` tienen su propia estructura de Arquitectura Limpia, replicando las capas `domain`, `infrastructure` y `presentation` dentro de cada módulo. Esto asegura que cada módulo sea independiente y siga los principios de Clean Architecture.

### Archivos Clave
- **main.py**: Ubicado en `src/`, sirve como punto de entrada para la aplicación FastAPI. Su contenido se importa desde `archivoMain`, que contiene una estructura básica para un proyecto FastAPI.
- **.gitignore**: Configurado para proyectos de Python, su contenido se importa desde `archivoGitIgnore`, excluyendo archivos como `__pycache__`, `.env`, `venv/`, entre otros.
- **.env**: Archivo para variables de entorno, inicialmente vacío.
- **dockerfile**: Archivo para definir la configuración de un contenedor Docker, inicialmente vacío.
- **.dockerignore**: Archivo para excluir elementos no necesarios en el contenedor Docker, inicialmente vacío.
- **README.md**: Documentación inicial del proyecto, inicialmente vacía.
- **requirements.txt**: Lista de dependencias, inicialmente vacía.
- **config.py**: Archivo para configuraciones del proyecto, inicialmente vacío.

## Ejemplo de Ejecución
```bash
$ python create_clean_architecture.py
Ingrese el nombre del proyecto: MiProyecto
Estructura básica de Clean Architecture creada para el proyecto 'MiProyecto'
```

## Notas
- Asegúrate de tener Python instalado y los módulos `archivoMain` y `archivoGitIgnore` disponibles en el mismo directorio que el script, ya que contienen el contenido de `main.py` y `.gitignore`, respectivamente.
- La estructura generada está optimizada para proyectos FastAPI, pero es flexible para adaptarse a otros frameworks o necesidades.
- Los archivos generados como `.env`, `dockerfile`, `.dockerignore`, `README.md`, `requirements.txt` y `config.py` están vacíos inicialmente y deben personalizarse según los requerimientos del proyecto.
- Para proyectos con múltiples módulos, crea manualmente los directorios de cada módulo dentro de `src/` y replica la estructura de `domain`, `infrastructure` y `presentation` para cada uno, siguiendo el ejemplo proporcionado.
- Asegúrate de configurar correctamente el entorno de desarrollo (por ejemplo, instalando dependencias en `requirements.txt`) y el contenedor Docker si planeas usarlo.