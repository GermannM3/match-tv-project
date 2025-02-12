import cv2
import numpy as np

def upscale_video(input_path, output_path):
    # Чтение видео
    cap = cv2.VideoCapture(input_path)
    
    # Получение параметров исходного видео
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Установка нового разрешения 1920x1080
    width = 1920
    height = 1080
    
    # Создание видеозаписи
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # Изменение размера кадра
        resized_frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_LANCZOS4)
        out.write(resized_frame)
    
    cap.release()
    out.release() 