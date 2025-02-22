# Match TV Project 🎥

[![Match TV Project CI](https://github.com/GermannM3/match-tv-project/actions/workflows/test.yml/badge.svg)](https://github.com/GermannM3/match-tv-project/actions/workflows/test.yml)

Проект для автоматической обработки видео для Match TV с использованием искусственного интеллекта и компьютерного зрения.

## 🎯 Возможности

### 1. Обработка интро "The Office"
- ⬆️ Повышение разрешения до 1080p
- 👥 Замена лиц актеров на комментаторов Match TV:
  - Стив Карелл → Георгий Черданцев
  - Рэйн Уилсон → Дмитрий Губерниев
  - Джон Красински → Константин Генич
  - Йена Фишер → Мария Орзул
  - Би Джей Новак → Роман Нагучев
- 🎨 Замена титров и логотипов

### 2. Создание спортивного видео
- 🏃 Замена видов спорта у спортсменов
- 🎤 Генерация комментариев
- 🎵 Добавление музыкального сопровождения

## 🚀 Тестирование проекта

Для тестирования проекта в Google Colab выполните следующие шаги:
1. Откройте [ноутбук в Google Colab](https://colab.research.google.com/github/GermannM3/match-tv-project/blob/main/match_tv_project.ipynb)
2. Выберите Runtime → Change runtime type → GPU
3. Запустите все ячейки ноутбука

## 💻 Системные требования

- Python 3.8+
- CUDA-совместимый GPU
- 16GB RAM
- 50GB свободного места на диске

## 📁 Структура проекта

- `source/` – исходные видео и изображения
- `faces/` – фотографии комментаторов (скачиваются автоматически)
- `audio/` – аудиоматериалы (скачиваются автоматически)
- `download_faces.py` – скрипт для загрузки фотографий комментаторов
- `download_assets.py` – скрипт для загрузки видео материалов
- `download_audio.py` – скрипт для загрузки аудио материалов
- `audio_processing.py` – модуль для работы с аудио
- `requirements.txt` – зависимости проекта
- `match_tv_project.ipynb` – основной ноутбук для тестирования в Colab 