import cv2
import numpy as np
from basicsr.archs.rrdbnet_arch import RRDBNet
from basicsr.utils.download_util import load_file_from_url
from basicsr.utils import img2tensor, tensor2img
import torch

def upscale_video(input_path, output_path):
    """Повышение разрешения видео"""
    try:
        # Загрузка модели для апскейла
        model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32)
        model_path = load_file_from_url(
            'https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth',
            model_dir='weights'
        )
        model.load_state_dict(torch.load(model_path), strict=True)
        model.eval()
        if torch.cuda.is_available():
            model = model.cuda()

        # Открываем видео
        cap = cv2.VideoCapture(input_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) * 2)
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * 2)
        
        # Создаем выходное видео
        out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Преобразуем кадр
            img = img2tensor(frame)
            if torch.cuda.is_available():
                img = img.cuda()
            with torch.no_grad():
                output = model(img)
            output = tensor2img(output)
            
            out.write(output)

        cap.release()
        out.release()
        return True
    except Exception as e:
        print(f"Ошибка при апскейле видео: {str(e)}")
        return False 