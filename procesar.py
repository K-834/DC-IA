from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os

# Obtener la ruta del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Combinar la ruta actual con la carpeta que deseas
resultados_images_folder = os.path.join(current_dir, 'resultados_images')

# Configurar la aplicación Flask
app = Flask(__name__, static_folder=resultados_images_folder)

# Carpeta para cargar archivos de los usuarios
UPLOAD_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Carpeta para almacenar resultados de detección
app.config['RESULT_FOLDER'] = 'resultados_images'

@app.route('/')
def index():
    return render_template('Web.html')

@app.route('/procesar_imagen', methods=['POST'])
def procesar_imagen():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Llamar al script de detección y obtener la ruta del resultado
        resultado_filename = ejecutar_script_deteccion(filename)

        # Renderizar el template y pasar la ruta del resultado
        return render_template('Web.html', resultado_deteccion=resultado_filename)

def ejecutar_script_deteccion(filename):
    # Llamar al script de detección y guardar el resultado
    resultado_filename = os.path.join(app.config['RESULT_FOLDER'], 'resultado_deteccion.jpg')
    resultado_filename = resultado_filename.replace("\\", "/")  # Reemplazar barras invertidas por barras inclinadas
    os.system(f'python deteccion.py {filename} {resultado_filename}')

    return resultado_filename

if __name__ == '__main__':
    app.run(debug=True)