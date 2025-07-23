import os
from archivoMain import main
from archivoGitIgnore import gitIgnore

def create_clean_architecture(project_name: str) -> None:
    """Crea la estructura básica de carpetas y archivos para un proyecto con Clean Architecture."""
    # Definir la estructura de directorios dentro de src
    structure = {
        f"{project_name}/": ["__init__.py", ".env", "dockerfile", ".dockerignore", "README.md", "requirements.txt",],
        f"{project_name}/src/": ["__init__.py", "main.py", "config.py"],
        f"{project_name}/src/domain/": ["__init__.py"],
        f"{project_name}/src/domain/entities/": ["__init__.py"],
        f"{project_name}/src/domain/repositories/": ["__init__.py"],
        f"{project_name}/src/domain/use_cases/": ["__init__.py"],
        f"{project_name}/src/infrastructure/": ["__init__.py"],
        f"{project_name}/src/infrastructure/database/": ["__init__.py"],
        f"{project_name}/src/infrastructure/repositories/": ["__init__.py"],
        f"{project_name}/src/infrastructure/logs/": ["__init__.py"],
        f"{project_name}/src/presentation/": ["__init__.py"],
        f"{project_name}/src/presentation/api/": ["__init__.py"],
        f"{project_name}/tests/": ["__init__.py"],
        f"{project_name}/tests/unitarios/": ["__init__.py"],
        f"{project_name}/tests/integracion/": ["__init__.py"],
    }

    # Crear directorios y archivos __init__.py
    for directory, files in structure.items():
        os.makedirs(directory, exist_ok=True)
        for file in files:
            file_path = os.path.join(directory, file)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("")

    # Crear archivo main.py en presentation/api
    main_content = main

    with open(f"{project_name}/src/main.py", 'w', encoding='utf-8') as f:
        f.write(main_content)

    # Crear archivo .gitignore
    gitignore_content = gitIgnore
    
    with open(f"{project_name}/.gitignore", 'w', encoding='utf-8') as f:
        f.write(gitignore_content)

    print(f"Estructura básica de Clean Architecture creada para el proyecto '{project_name}'")

if __name__ == "__main__":
    project_name = input("Ingrese el nombre del proyecto: ") or "FASTAPI_CLEANARCHITECTURE"
    create_clean_architecture(project_name)