from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
import numpy as np

def add_commentary(video_path, voice_path, output_path):
    """Добавление комментариев к видео"""
    video = VideoFileClip(video_path)
    voice = AudioFileClip(voice_path)
    
    # Подгонка длительности голоса под видео
    if voice.duration > video.duration:
        voice = voice.subclip(0, video.duration)
    
    # Добавление голоса
    final_video = video.set_audio(voice)
    final_video.write_videofile(output_path)

def add_background_music(video_path, music_path, output_path, volume=0.3):
    """Добавление фоновой музыки"""
    video = VideoFileClip(video_path)
    music = AudioFileClip(music_path)
    
    # Зацикливание музыки если нужно
    if music.duration < video.duration:
        repeats = int(np.ceil(video.duration / music.duration))
        music = music.loop(repeats)
    
    # Обрезка музыки по длине видео
    music = music.subclip(0, video.duration)
    
    # Уменьшение громкости музыки
    music = music.volumex(volume)
    
    # Смешивание аудио
    final_audio = CompositeVideoClip([video.set_audio(music)])
    final_audio.write_videofile(output_path) 