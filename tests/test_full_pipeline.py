import unittest
import os
from pathlib import Path
from download_assets import *
from upscale import upscale_video
from face_swap import swap_faces
from titles import replace_titles
from sports_swap import create_sports_swap
from utils import check_video_file, check_image_file

class TestMatchTVPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Подготовка тестового окружения"""
        # Создаем тестовые директории
        create_directories()
        
    def test_1_download_assets(self):
        """Тест загрузки материалов"""
        # Загружаем интро Office
        download_office_intro()
        self.assertTrue(Path('source/office_intro.mp4').exists())
        
        # Загружаем фото комментаторов
        download_commentators_photos()
        commentators = ['cherdantsev', 'guberniev', 'genich', 'orzul', 'naguchev']
        for commentator in commentators:
            self.assertTrue(Path(f'faces/{commentator}.jpg').exists())
            
        # Проверяем логотип
        download_match_tv_logo()
        self.assertTrue(Path('source/match_tv_logo.png').exists())

    def test_2_upscale(self):
        """Тест повышения разрешения"""
        input_path = 'source/office_intro.mp4'
        output_path = 'temp/office_upscaled.mp4'
        upscale_video(input_path, output_path)
        self.assertTrue(check_video_file(output_path))

    def test_3_face_swap(self):
        """Тест замены лиц"""
        input_video = 'temp/office_upscaled.mp4'
        faces_dict = {
            'cherdantsev': 'faces/cherdantsev.jpg',
            'guberniev': 'faces/guberniev.jpg',
            'genich': 'faces/genich.jpg',
            'orzul': 'faces/orzul.jpg',
            'naguchev': 'faces/naguchev.jpg'
        }
        swap_faces(input_video, faces_dict)
        self.assertTrue(Path('temp/office_faces_swapped.mp4').exists())

    def test_4_sports_video(self):
        """Тест создания спортивного видео"""
        create_sports_swap()
        self.assertTrue(Path('output/final_output.mp4').exists())

    @classmethod
    def tearDownClass(cls):
        """Очистка после тестов"""
        # Можно добавить удаление временных файлов
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2) 