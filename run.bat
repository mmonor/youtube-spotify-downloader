@echo off
TITLE YouTube Downloader Setup

echo Checking Python installation...
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed or not in PATH! Please install Python.
    pause
    exit /b
)

echo Installing required packages...
pip install -r requirements.txt

echo.
echo Starting YouTube Downloader...
start pythonw main.py
exit