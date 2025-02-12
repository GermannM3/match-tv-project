import requests
import os
import yt_dlp
from pathlib import Path
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_directories():
    """Создание структуры папок для проекта"""
    try:
        directories = ['source', 'faces', 'output', 'temp']
        for dir_name in directories:
            Path(dir_name).mkdir(exist_ok=True)
        logger.info("Directories created successfully")
    except Exception as e:
        logger.error(f"Error creating directories: {str(e)}")
        raise

def download_office_intro():
    url = "https://example.com/office_intro.mp4"  # Замените на реальный URL
    dest = Path("source/office_intro.mp4")
    dest.parent.mkdir(parents=True, exist_ok=True)
    print("Скачивание интро Office...")
    try:
        response = requests.get(url)
        with open(dest, "wb") as f:
            f.write(response.content)
        print("✅ Интро Office скачано")
    except Exception as e:
        print("❌ Ошибка при скачивании интро Office:", e)

def download_commentators_photos():
    # Данный шаг уже выполняется через download_faces.py
    print("Функция загрузки фото комментаторов реализована в download_faces.py. Пропускаем этот шаг.")

def download_sports_videos():
    """Загрузка видео со спортсменами"""
    # Используем короткие клипы с YouTube
    athletes = {
        'messi': 'https://www.youtube.com/watch?v=S7_XjS6_VnE',  # Лучшие моменты Месси
        'ovechkin': 'https://www.youtube.com/watch?v=Ht_gKUmXJ2o',  # Хайлайты Овечкина
        'medvedeva': 'https://www.youtube.com/watch?v=JUL5gK6c6Gs',  # Выступление Медведевой
        'vinicius': 'https://www.youtube.com/watch?v=W8U_qp_Rz0E'  # Моменты Винисиуса
    }
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'source/%(title)s.%(ext)s',
        'max_filesize': '100M'  # Ограничим размер файлов
    }
    
    for name, url in athletes.items():
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

def download_match_tv_logo():
    url = "https://example.com/match_tv_logo.png"  # Замените на реальный URL
    dest = Path("source/match_tv_logo.png")
    dest.parent.mkdir(parents=True, exist_ok=True)
    print("Скачивание логотипа Match TV...")
    try:
        response = requests.get(url)
        with open(dest, "wb") as f:
            f.write(response.content)
        print("✅ Логотип Match TV скачан")
    except Exception as e:
        print("❌ Ошибка при скачивании логотипа Match TV:", e)

if __name__ == "__main__":
    create_directories()
    download_office_intro()
    download_commentators_photos()
    download_sports_videos()
    download_match_tv_logo() 