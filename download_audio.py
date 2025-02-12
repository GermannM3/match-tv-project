import requests
import yt_dlp
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def download_audio():
    """Загрузка аудио материалов"""
    
    # Создаем директории для аудио
    Path('audio/voices').mkdir(parents=True, exist_ok=True)
    Path('audio/music').mkdir(parents=True, exist_ok=True)
    
    # Словарь с URL голосов комментаторов
    voices = {
        'cherdantsev': 'https://www.youtube.com/watch?v=example1',  # Заменить на реальные URL
        'guberniev': 'https://www.youtube.com/watch?v=example2',
        'genich': 'https://www.youtube.com/watch?v=example3',
        'orzul': 'https://www.youtube.com/watch?v=example4',
        'naguchev': 'https://www.youtube.com/watch?v=example5'
    }
    
    # Словарь с URL музыки
    music = {
        'sports_theme': 'https://www.youtube.com/watch?v=example6',
        'match_tv_intro': 'https://www.youtube.com/watch?v=example7',
        'background_music': 'https://www.youtube.com/watch?v=example8'
    }
    
    # Настройки для yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True
    }
    
    # Загрузка голосов комментаторов
    logger.info("Загрузка голосов комментаторов...")
    for name, url in voices.items():
        try:
            ydl_opts['outtmpl'] = f'audio/voices/{name}.%(ext)s'
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            logger.info(f"✅ Загружен голос {name}")
        except Exception as e:
            logger.error(f"❌ Ошибка при загрузке голоса {name}: {str(e)}")
    
    # Загрузка музыки
    logger.info("\nЗагрузка музыки...")
    for name, url in music.items():
        try:
            ydl_opts['outtmpl'] = f'audio/music/{name}.%(ext)s'
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            logger.info(f"✅ Загружена музыка {name}")
        except Exception as e:
            logger.error(f"❌ Ошибка при загрузке музыки {name}: {str(e)}")

if __name__ == "__main__":
    download_audio() 