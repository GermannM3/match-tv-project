import cv2
import numpy as np
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def check_video_file(file_path):
    """Проверка видео файла"""
    try:
        cap = cv2.VideoCapture(file_path)
        if not cap.isOpened():
            raise ValueError(f"Cannot open video file: {file_path}")
        return True
    except Exception as e:
        logger.error(f"Error checking video file: {str(e)}")
        return False

def check_image_file(file_path):
    """Проверка изображения"""
    try:
        img = cv2.imread(file_path)
        if img is None:
            raise ValueError(f"Cannot open image file: {file_path}")
        return True
    except Exception as e:
        logger.error(f"Error checking image file: {str(e)}")
        return False 