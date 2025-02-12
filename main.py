import os
import logging
from download_assets import *
from upscale import upscale_video
from face_swap import swap_faces
from titles import replace_titles
from sports_swap import create_sports_swap
from utils import check_video_file, check_image_file

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def prepare_project():
    """Подготовка проекта"""
    # Создание директорий и загрузка материалов
    create_directories()
    download_office_intro()
    download_commentators_photos()
    download_sports_videos()
    download_match_tv_logo()

def process_office_intro():
    """Обработка интро Office"""
    # Апскейл видео до 1080p
    upscale_video('source/office_intro.mp4', 'temp/office_upscaled.mp4')
    
    # Замена лиц
    faces_dict = {
        'cherdantsev': 'faces/cherdantsev.jpg',
        'guberniev': 'faces/guberniev.jpg',
        'genich': 'faces/genich.jpg',
        'orzul': 'faces/orzul.jpg',
        'naguchev': 'faces/naguchev.jpg'
    }
    swap_faces('temp/office_upscaled.mp4', faces_dict)
    
    # Замена титров
    replace_titles('temp/office_faces_swapped.mp4')

def process_sports_videos():
    """Создание спортивного видео"""
    create_sports_swap()

def verify_downloads():
    """Проверка загруженных файлов"""
    required_files = {
        'source/office_intro.mp4': check_video_file,
        'source/match_tv_logo.png': check_image_file
    }
    
    for file_path, check_func in required_files.items():
        if not Path(file_path).exists() or not check_func(file_path):
            raise FileNotFoundError(f"Required file missing or corrupt: {file_path}")

def main():
    try:
        logger.info("Starting project setup...")
        prepare_project()
        
        logger.info("Verifying downloads...")
        verify_downloads()
        
        logger.info("Processing Office intro...")
        process_office_intro()
        
        logger.info("Creating sports video...")
        process_sports_videos()
        
        logger.info("Project completed successfully!")
        
    except Exception as e:
        logger.error(f"Project failed: {str(e)}")
        raise

if __name__ == "__main__":
    main() 