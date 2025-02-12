#!/bin/bash

# Проверка наличия Python
if command -v python3 &>/dev/null; then
    PYTHON_CMD=python3
elif command -v python &>/dev/null; then
    PYTHON_CMD=python
else
    echo "❌ Ошибка: Python не установлен"
    echo "Установите Python командой:"
    echo "sudo apt-get install python3"
    exit 1
fi

# Проверка виртуального окружения
if [ ! -d "venv" ]; then
    echo "Создание виртуального окружения..."
    $PYTHON_CMD -m venv venv
fi

# Активация виртуального окружения
source venv/bin/activate

# Установка зависимостей
echo "Установка зависимостей..."
pip install -r requirements.txt

# Проверка окружения
echo "Проверка окружения..."
$PYTHON_CMD -c "import torch; print('CUDA доступен:', torch.cuda.is_available())"

# Запуск базовых тестов
echo "Запуск базовых тестов..."
$PYTHON_CMD -m unittest test_project.py -v

# Запуск полного тестирования
echo "Запуск полного тестирования..."
$PYTHON_CMD -m unittest tests/test_full_pipeline.py -v

# Проверка результатов
echo "Проверка результатов..."
if [ -f "output/final_output.mp4" ]; then
    echo "✅ Тестирование успешно завершено"
else
    echo "❌ Ошибка: финальное видео не создано"
    exit 1
fi 