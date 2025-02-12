import cv2
import insightface
from insightface.app import FaceAnalysis
import numpy as np
from pathlib import Path

def swap_faces(video_path, faces_dict):
    """Замена лиц в видео"""
    try:
        # Инициализация моделей
        app = FaceAnalysis(name='buffalo_l')
        app.prepare(ctx_id=0, det_size=(640, 640))
        swapper = insightface.model_zoo.get_model('inswapper_128.onnx')

        # Загрузка фотографий лиц
        face_embeddings = {}
        for name, photo_path in faces_dict.items():
            img = cv2.imread(photo_path)
            faces = app.get(img)
            if faces:
                face_embeddings[name] = faces[0]

        # Открываем видео
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # Создаем выходное видео
        output_path = str(Path(video_path).parent / 'office_faces_swapped.mp4')
        out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Определяем лица в кадре
            faces = app.get(frame)
            
            # Заменяем лица
            result = frame.copy()
            for face, (name, target_face) in zip(faces, face_embeddings.items()):
                result = swapper.get(result, face, target_face, paste_back=True)
            
            out.write(result)

        cap.release()
        out.release()
        return True
    except Exception as e:
        print(f"Ошибка при замене лиц: {str(e)}")
        return False 