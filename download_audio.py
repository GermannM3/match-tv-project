import requests
import yt_dlp
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def download_audio():
    """Основная функция загрузки аудио"""
    voices = {
        'cherdantsev': 'https://www.youtube.com/watch?v=5qap5aO4i9A',  # Пример комментария
        'guberniev': 'https://www.youtube.com/watch?v=r-LmVWgzp60',     # Пример комментария
        'genich': 'https://www.youtube.com/watch?v=oPEJczAyjqw',      # Пример комментария
        'orzul': 'https://www.youtube.com/watch?v=j_k0vLtA_qQ',        # Пример комментария
        'naguchev': 'https://www.youtube.com/watch?v=f_hA-vHBhpE'       # Пример комментария
    }

    music = {
        'sports_theme': 'https://www.youtube.com/watch?v=dyRsYk0LyA8',
        'match_tv_intro': 'https://www.youtube.com/watch?v=3sMn7vnFWVU',
        'background_music': 'https://www.youtube.com/watch?v=B7bqAsxee4I' # Пример фоновой музыки
    }

    # Создаем директории
    Path("audio/voices").mkdir(parents=True, exist_ok=True)
    Path("audio/music").mkdir(parents=True, exist_ok=True)

    # Загрузка голосов
    logger.info("Загрузка голосов комментаторов...")
    for name, url in voices.items():
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'audio/voices/{name}.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                }]
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            logger.info(f"✅ Голос {name} загружен")
        except Exception as e:
            logger.error(f"❌ Ошибка загрузки {name}: {str(e)}")

    # Загрузка музыки
    logger.info("\nЗагрузка музыки...")
    for name, url in music.items():
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'audio/music/{name}.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                }]
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            logger.info(f"✅ Музыка {name} загружена")
        except Exception as e:
            logger.error(f"❌ Ошибка загрузки {name}: {str(e)}")

if __name__ == "__main__":
    download_audio() 