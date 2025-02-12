from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import numpy as np

def replace_titles(video_path):
    """Замена титров в видео"""
    try:
        # Загружаем видео
        video = VideoFileClip(video_path)
        
        # Создаем титры
        titles = [
            ("Георгий Черданцев", 5),
            ("Дмитрий Губерниев", 10),
            ("Константин Генич", 15),
            ("Мария Орзул", 20),
            ("Роман Нагучев", 25)
        ]
        
        # Добавляем титры
        clips = [video]
        for title, start_time in titles:
            text = TextClip(
                title, 
                fontsize=70, 
                color='white',
                font='Arial'
            ).set_position(('center', 'bottom')).set_duration(3).set_start(start_time)
            clips.append(text)
        
        # Собираем финальное видео
        final = CompositeVideoClip(clips)
        final.write_videofile("output/final_output.mp4")
        return True
    except Exception as e:
        print(f"Ошибка при замене титров: {str(e)}")
        return False

# ... остальные функции ... 