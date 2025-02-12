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
    """Загрузка интро сериала Office"""
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'source/office_intro.%(ext)s',
            'quiet': True,
            'no_warnings': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            logger.info("Downloading Office intro...")
            ydl.download(['https://www.youtube.com/watch?v=_iiOgRrPS2E'])
    except Exception as e:
        logger.error(f"Error downloading Office intro: {str(e)}")
        raise

def download_commentators_photos():
    """Загрузка фотографий комментаторов"""
    commentators = {
        'cherdantsev': 'https://img.championat.com/s/735x490/news/big/z/p/georgij-cherdancev-prokommentiroval-uhod-dzyuby-iz-zenita_16530727051194112605.jpg',
        'guberniev': 'https://upload.wikimedia.org/wikipedia/commons/7/7a/Dmitry_Guberniev_2016.jpg',
        'genich': 'https://static.bombardir.ru/images/profile/32/86/konstantin-genich.jpg',
        'orzul': 'https://s5o.ru/storage/simple/ru/edt/90/51/d7/7c/rue5891431f6d.jpg',
        'naguchev': 'https://img.championat.com/s/735x490/news/big/q/l/roman-naguchev-pokinul-match-tv_15674065001801495682.jpg'
    }
    
    for name, url in commentators.items():
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'faces/{name}.jpg', 'wb') as f:
                f.write(response.content)

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
    """Загрузка логотипа Матч ТВ"""
    url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Match_TV_logo.svg/1200px-Match_TV_logo.svg.png'
    response = requests.get(url)
    if response.status_code == 200:
        with open('source/match_tv_logo.png', 'wb') as f:
            f.write(response.content)

if __name__ == "__main__":
    create_directories()
    download_office_intro()
    download_commentators_photos()
    download_sports_videos()
    download_match_tv_logo() 