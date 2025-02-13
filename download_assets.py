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
    """Скачивание интро The Office"""
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'source/office_intro.%(ext)s',
            'quiet': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            logger.info("Скачивание интро The Office...")
            ydl.download(['https://www.youtube.com/watch?v=m7Y7Hq-Ta4o'])  # Актуальное интро
    except Exception as e:
        logger.error(f"Ошибка загрузки интро: {e}")
        raise

def download_commentators_photos():
    # Данный шаг уже выполняется через download_faces.py
    print("Функция загрузки фото комментаторов реализована в download_faces.py. Пропускаем этот шаг.")

def download_sports_videos():
    """Скачивание спортивных моментов"""
    athletes = {
        'messi': 'https://www.youtube.com/watch?v=auXQtoAyCGA',
        'ronaldo': 'https://www.youtube.com/watch?v=OUKGsb8CpF8'
    }
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'source/%(title)s.%(ext)s',
        'max_filesize': '500M'
    }

    for name, url in athletes.items():
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                logger.info(f"Скачивание видео {name}...")
                ydl.download([url])
        except Exception as e:
            logger.error(f"Ошибка загрузки {name}: {e}")

def download_match_tv_logo():
    """Скачивание логотипа Match TV"""
    url = "https://upload.wikimedia.org/wikipedia/commons/a/a9/Match_TV_logo.png"
    try:
        response = requests.get(url)
        with open('source/match_tv_logo.png', 'wb') as f:
            f.write(response.content)
        logger.info("Логотип Match TV скачан")
    except Exception as e:
        logger.error(f"Ошибка загрузки логотипа: {e}")
        raise

if __name__ == "__main__":
    create_directories()
    download_office_intro()
    download_commentators_photos()
    download_sports_videos()
    download_match_tv_logo() 