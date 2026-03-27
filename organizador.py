import os
import shutil

def organizar_archivos(ruta_directorio):
"""
Organiza los archivos de un directorio en subcarpetas según su extensión.
"""
if not os.path.exists(ruta_directorio):
    print(f"Error: La ruta '{ruta_directorio}' no existe.")
        return

categorias = {
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    'Videos': ['.mp4', '.avi', '.mkv'],
    'Audio': ['.mp3', '.wav'],
    'Comprimidos': ['.zip', '.rar', '.tar', '.gz'],
    'Instaladores': ['.exe', '.msi'],
    'Scripts': ['.py', '.js', '.html']
    }

archivos_movidos = 0

for archivo in os.listdir(ruta_directorio):
    ruta_completa = os.path.join(ruta_directorio, archivo)

     if os.path.isfile(ruta_completa):
         _, extension = os.path.splitext(archivo)
         extension = extension.lower()
            
carpeta_destino = 'Otros'

    for categoria, extensiones in categorias.items():
         if extension in extensiones:
            carpeta_destino = categoria
             break
            
ruta_carpeta_destino = os.path.join(ruta_directorio, carpeta_destino)
            
    if not os.path.exists(ruta_carpeta_destino):
        os.makedirs(ruta_carpeta_destino)
            
        ruta_final = os.path.join(ruta_carpeta_destino, archivo)
        shutil.move(ruta_completa, ruta_final)
        print(f"Movido: {archivo} -> {carpeta_destino}/")
        archivos_movidos += 1

    print(f"\n¡Organización completada! Se movieron {archivos_movidos} archivos.")

if __name__ == "__main__":
    ruta_a_organizar = r"C:\Users\valen\OneDrive\Desktop\Mis proyectos\prueba" 
    
    print("Iniciando el script organizador...")
    organizar_archivos(ruta_a_organizar)
