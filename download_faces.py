import requests
import os
from pathlib import Path

def download_faces():
    """Загрузка фотографий комментаторов"""
    
    # Создаем директорию если её нет
    Path('faces').mkdir(exist_ok=True)
    
    # Словарь с URL фотографий комментаторов
    faces = {
        'cherdantsev': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Георгий_Черданцев.jpg/800px-Георгий_Черданцев.jpg',
        'guberniev': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Дмитрий_Губерниев.jpg/800px-Дмитрий_Губерниев.jpg',
        'genich': 'https://img.championat.com/s/735x490/news/big/z/o/konstantin-genich-prokommentiroval-match-real-barselona_1571477294850855246.jpg',
        'orzul': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Мария_Орзул.jpg/800px-Мария_Орзул.jpg',
        'naguchev': 'https://img.championat.com/s/735x490/news/big/q/v/roman-naguchev-stal-kommentatorom-match-tv_15714772948508552462.jpg'
    }
    
    for name, url in faces.items():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(f'faces/{name}.jpg', 'wb') as f:
                    f.write(response.content)
                print(f"✅ Загружено фото {name}")
            else:
                print(f"❌ Ошибка загрузки фото {name}")
        except Exception as e:
            print(f"❌ Ошибка при загрузке {name}: {str(e)}")

if __name__ == "__main__":
    download_faces() 