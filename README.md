# Organizador Automático de Archivos (Python)

# Descripción
Este proyecto es un script de automatización desarrollado en Python que clasifica y organiza archivos desordenados dentro de un directorio. El programa lee la extensión de cada archivo y lo mueve automáticamente a una subcarpeta correspondiente (Documentos, Imágenes, Instaladores, etc.), ahorrando tiempo de gestión manual.

# Características Principales
* Clasificación Inteligente: Mapeo automático de más de 20 extensiones de archivo comunes.
* Creación Dinámica de Directorios: Si la carpeta de destino no existe, el script la genera automáticamente.
* Prevención de Errores: Verifica la existencia de las rutas antes de ejecutar acciones para evitar pérdida de datos o interrupciones.
* Código Escalable: Estructurado con diccionarios y funciones claras para facilitar la adición de nuevas categorías.

# Tecnologías Utilizadas
* Lenguaje: Python 3.x
* Librerías Estándar: `os`, `shutil` (No requiere instalación de dependencias externas).

# Cómo usarlo
1. Clona este repositorio o descarga el archivo `organizador.py`.
2. Abre el archivo y modifica la variable `ruta_a_organizar` con la ruta de la carpeta que deseas limpiar.
3. Ejecuta el script desde tu terminal:
   ```bash
   python organizador.py
