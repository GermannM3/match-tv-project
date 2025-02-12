#!/bin/bash

# Установка системных пакетов
apt-get update
apt-get install -y ffmpeg kdenlive python3-pip git

# Установка Python-зависимостей
pip3 install opencv-python numpy moviepy requests yt-dlp torch torchvision

# Установка Roop для замены лиц
git clone https://github.com/s0md3v/roop
cd roop
pip3 install -r requirements.txt
cd ..

# Установка дополнительных инструментов для обработки видео
pip3 install stable-diffusion-torch torch-audiogen

# Создание рабочей директории
mkdir -p ~/match_tv_project
cd ~/match_tv_project

echo "Установка завершена!" 