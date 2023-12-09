# Importar las bibliotecas necesarias
from ultralytics import YOLO
import cv2
import sys

# Función principal que toma las rutas de entrada y salida como parámetros
def main(image_path, output_path):
    # Crear una instancia del modelo YOLO cargando los datos preentrenados (best.pt)
    model = YOLO('best.pt')

    # Leer la imagen de entrada utilizando OpenCV
    frame = cv2.imread(image_path)

    # Realizar predicciones en la imagen utilizando el modelo YOLO con un tamaño de imagen de 640x640
    resultados = model.predict(frame, imgsz=640)

    # Obtener las anotaciones de los resultados y visualizarlas en la imagen original
    anotaciones = resultados[0].plot()

    # Guardar la imagen con las anotaciones en la ruta de salida
    cv2.imwrite(output_path, anotaciones)

# Verificar si el script se ejecuta directamente (no se importa como módulo)
if __name__ == "__main__":
    # Verificar si se proporcionan los argumentos adecuados al ejecutar el script
    if len(sys.argv) != 3:
        print("Uso: python main.py <ruta_imagen_entrada> <ruta_imagen_salida>")
        sys.exit(1)

    # Obtener las rutas de la imagen de entrada y salida desde los argumentos de la línea de comandos
    ruta_imagen_entrada = sys.argv[1]
    ruta_imagen_salida = sys.argv[2]

    # Llamar a la función principal con las rutas de entrada y salida como parámetros
    main(ruta_imagen_entrada, ruta_imagen_salida)
