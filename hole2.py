import cv2
import time # Adicione o import do time

# ... (Mantenha todas as suas outras funções exatamente iguais) ...

def get_camera():
    # Iniciar câmera (0 para webcam, ou mude para 'video.mp4')
    cam = cv2.VideoCapture('http://10.20.57.48:8080/video')
    return cam


def show_frame(frame):
    # COMENTADO PARA NÃO QUEBRAR NO DOCKER (TV BOX)
    # cv2.imshow('Video', frame)
    pass

def get_detector():
    # Carrega o arquivo XML com as regras do modelo (fica fora do loop, carrega só uma vez)
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    return detector

def get_hole(frame, detector):
    # 1. Carrega o arquivo XML com as regras do modelo (fica fora do loop, carrega só uma vez)

    # ... (dentro do seu loop de captura de vídeo) ...

    # 2. Converte o frame capturado (variável 'frame') para tons de cinza
    frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 3. Faz a detecção. Retorna uma lista com [x, y, largura, altura] para cada rosto achado
    rostos = detector.detectMultiScale(frame_cinza, scaleFactor=1.1, minNeighbors=5)

    # 4. Exemplo de uso: se a lista não estiver vazia, achou algo
    print(f"Achou {len(rostos)}")

    return rostos[0] if len(rostos) > 0 else None

def get_gps(hole):
    return {"latitude": 0.0, "longitude": 0.0}  # Implementação fictícia para obter coordenadas GPS do buraco


def main():
    cam = get_camera()
    detector = get_detector()

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Falha ao capturar o vídeo")
            break

        hole = get_hole(frame, detector)
        if hole is not None:
            x, y, w, h = hole
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            print(f"Buraco desenhado em X:{x} Y:{y}") # Print para você saber que funcionou

        show_frame(frame)

        # Sem o imshow, o waitKey não funciona direito. 
        # Como a própria leitura da câmera (cam.read()) já trava no tempo certo do frame, 
        # você não precisa de delay extra. Mas se precisar parar o código, use Ctrl+C no terminal.
        time.sleep(0.01) 

    cam.release()

if __name__ == "__main__":
    main()