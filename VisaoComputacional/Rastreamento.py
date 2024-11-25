import cv2

# Ler o video

video_path: str = r'C:\Users\VictorCampos\Udemy\Data_Science\VisaoComputacional\rua.mp4'

tracker = cv2.TrackerCSRT_create()

video = cv2.VideoCapture(video_path)


load_bool, frame  = video.read() 
# load_bool = se carregou corretamente
# frame = o primeiro frame do vídeo

bounding_box = cv2.selectROI(frame) # ROI = Region of Interest
# print(bounding_box)

load_bool = tracker.init(frame, bounding_box)


# Uma vez inicializado a ROI
while True:
    load_bool, frame = video.read()
    if not load_bool:
        break

    load_bool, bounding_box = tracker.update(frame)

    if load_bool:
        (x, y, largura, altura) = [int(v) for v in bounding_box] 
        cv2.rectangle(frame, (x,y), (x+ largura, y+altura), (0, 255, 0), 2, 1) # Desenha o retângulo
    else:
        cv2.putText(frame, "Falha no Rastreamento", (100,80), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, .75, (0,0, 255), 2)

    cv2.imshow('Rastreando', frame)

    # Se apertar "Esc"
    if cv2.waitKey(1) & 0XFF == 27:
        break
