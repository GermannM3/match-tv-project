#!/bin/bash

# Проверка наличия необходимых утилит
command -v python3 >/dev/null 2>&1 || { echo "Python 3 не установлен"; exit 1; }
command -v pip3 >/dev/null 2>&1 || { echo "pip3 не установлен"; exit 1; }
command -v git >/dev/null 2>&1 || { echo "git не установлен"; exit 1; }

# Создание и активация виртуального окружения
python3 -m venv venv
source venv/bin/activate

# Установка зависимостей
pip install --upgrade pip
pip install -r requirements.txt

# Проверка установки
python -c "import torch; print('CUDA доступен:', torch.cuda.is_available())"

echo "Установка завершена!" 