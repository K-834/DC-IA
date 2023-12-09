# Importar las funciones necesarias de Flask y otras bibliotecas
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os

# Obtener la ruta del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Combinar la ruta actual con la carpeta que deseas para almacenar imágenes de resultados
resultados_images_folder = os.path.join(current_dir, 'resultados_images')

# Configurar la aplicación Flask y especificar la carpeta de imágenes estáticas
app = Flask(__name__, static_folder=resultados_images_folder)

# Carpeta para cargar archivos de los usuarios
UPLOAD_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Carpeta para almacenar resultados de detección
app.config['RESULT_FOLDER'] = 'resultados_images'

# Definir la ruta principal que renderiza un template 'Web.html'
@app.route('/')
def index():
    return render_template('Web.html')

# Definir la ruta para procesar una imagen enviada mediante un formulario POST
@app.route('/procesar_imagen', methods=['POST'])
def procesar_imagen():
    # Verificar si se ha enviado un archivo con el nombre 'file'
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    # Verificar si se ha seleccionado un archivo
    if file.filename == '':
        return redirect(request.url)

    if file:
        # Guardar el archivo en la carpeta de carga definida
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Llamar al script de detección y obtener la ruta del resultado
        resultado_filename = ejecutar_script_deteccion(filename)

        # Renderizar el template y pasar la ruta del resultado
        return render_template('Web.html', resultado_deteccion=resultado_filename)

# Función para ejecutar el script de detección y devolver la ruta del resultado
def ejecutar_script_deteccion(filename):
    # Llamar al script de detección y guardar el resultado en la carpeta de resultados
    resultado_filename = os.path.join(app.config['RESULT_FOLDER'], 'resultado_deteccion.jpg')
    resultado_filename = resultado_filename.replace("\\", "/") 
    os.system(f'python deteccion.py {filename} {resultado_filename}')

    return resultado_filename

# Iniciar la aplicación Flask en modo de depuración si se ejecuta este script directamente
if __name__ == '__main__':
    app.run(debug=True)
