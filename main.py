# main.py
from ultralytics import YOLO
import cv2
import sys

def main(image_path, output_path):
    model = YOLO('best.pt')
    frame = cv2.imread(image_path)
    resultados = model.predict(frame, imgsz=640)

    anotaciones = resultados[0].plot()

    cv2.imwrite(output_path, anotaciones)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python main.py <ruta_imagen_entrada> <ruta_imagen_salida>")
        sys.exit(1)

    ruta_imagen_entrada = sys.argv[1]
    ruta_imagen_salida = sys.argv[2]

    main(ruta_imagen_entrada, ruta_imagen_salida)
