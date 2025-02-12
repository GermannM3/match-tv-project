import unittest
from pathlib import Path
from utils import check_video_file, check_image_file
from download_assets import create_directories

class TestMatchTVProject(unittest.TestCase):
    def setUp(self):
        create_directories()

    def test_directories_exist(self):
        required_dirs = ['source', 'faces', 'output', 'temp']
        for dir_name in required_dirs:
            self.assertTrue(Path(dir_name).exists())

    def test_file_checks(self):
        # Создаем тестовое видео
        test_video = 'temp/test.mp4'
        with open(test_video, 'wb') as f:
            f.write(b'test')
        self.assertFalse(check_video_file(test_video))

if __name__ == '__main__':
    unittest.main() 