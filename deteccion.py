from ultralytics import YOLO
import cv2
import sys

def main():
    if len(sys.argv) != 3:
        print("Uso: python deteccion.py <ruta_imagen_entrada> <ruta_imagen_salida>")
        sys.exit(1)

    ruta_imagen_entrada = sys.argv[1]
    ruta_imagen_salida = sys.argv[2]

    model = YOLO('best.pt')
    frame = cv2.imread(ruta_imagen_entrada)
    resultados = model.predict(frame, imgsz=640)

    anotaciones = resultados[0].plot()

    cv2.imwrite(ruta_imagen_salida, anotaciones)

if __name__ == "__main__":
    main()
