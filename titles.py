import moviepy.editor as mp
from moviepy.video.tools.drawing import color_gradient

def replace_titles(video_path):
    video = mp.VideoFileClip(video_path)
    
    # Создание новых титров
    def create_title(text, duration):
        return mp.TextClip(text, 
                          font='Helvetica', 
                          fontsize=48, 
                          color='white')
    
    # Замена титров для каждого актера
    titles = {
        'Георгий Черданцев': (10, 13),
        'Дмитрий Губерниев': (14, 17),
        # ... остальные тайминги ...
    }
    
    # Замена финального логотипа
    match_tv_logo = mp.ImageClip('match_tv_logo.png')
    
    # ... существующий код ... 