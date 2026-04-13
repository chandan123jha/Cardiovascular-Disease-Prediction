@echo off
REM This batch file runs the Cardiovascular Disease Prediction application
setlocal enabledelayedexpansion
cd /d "%~dp0"

REM Navigate to the project directory
cd "Cardiovascular-Disease Prediction"

REM Use the correct Python interpreter from .venv-1
".\.venv-1\Scripts\python.exe" heartGUI_main.py

REM Pause to see any errors
if errorlevel 1 (
    echo.
    echo ERROR: Application failed to start
    echo Press any key to exit...
    pause
)
