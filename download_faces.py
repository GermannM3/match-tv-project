import requests
import os
from pathlib import Path
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def download_faces():
    """Загрузка фотографий комментаторов"""
    
    # Создаем директорию если её нет
    Path('faces').mkdir(exist_ok=True)
    
    # Словарь с URL фотографий комментаторов
    faces = {
        'cherdantsev': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Georgy_Cherdantsev_2018.jpg/800px-Georgy_Cherdantsev_2018.jpg',
        'guberniev': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Dmitry_Guberniev_2019.jpg/800px-Dmitry_Guberniev_2019.jpg',
        'genich': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Konstantin_Genich_2018.jpg/800px-Konstantin_Genich_2018.jpg',
        'orzul': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Maria_Orzul_2019.jpg/800px-Maria_Orzul_2019.jpg',
        'naguchev': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Roman_Naguchev_2018.jpg/800px-Roman_Naguchev_2018.jpg'
    }
    
    for name, url in faces.items():
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Проверка на ошибки HTTP
            with open(f'faces/{name}.jpg', 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            logger.info(f"✅ Загружено фото {name}")
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Ошибка загрузки фото {name}: {e}")
        except Exception as e:
            logger.error(f"❌ Ошибка загрузки фото {name}: {e}")

if __name__ == "__main__":
    download_faces() 