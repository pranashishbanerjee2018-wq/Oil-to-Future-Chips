@echo off
setlocal enabledelayedexpansion

title SEMICONDUCTORS — THE NEW OIL OF THE FUTURE

echo ========================================================================
echo  SEMICONDUCTORS — THE NEW OIL OF THE FUTURE
echo  An Academic Presentation ^& Computational Microelectronics Suite
echo  Lead Researchers: Dr. Theodore Voss ^& Dr. Caleb Sterling
echo ========================================================================
echo.

:: 1. Navigate to project directory (resilient to any launch origin)
cd /d "%~dp0"
if not exist "app.py" (
    cd /d "C:\Users\prana\.gemini\antigravity\scratch\Semiconductors_The_New_Oil_of_the_Future"
)

echo [1/4] Project Directory:
cd
echo.

:: 2. Configure proxy bypass for localhost
set NO_PROXY=localhost,127.0.0.1
set no_proxy=localhost,127.0.0.1

:: 3. Verify Python runtime
echo [2/4] Verifying Python installation...
python --version >nul 2>&1
if !errorlevel! neq 0 (
    echo [CRITICAL ERROR] Python is not installed or not found in system PATH.
    echo Command failed: python --version
    echo Please install Python 3.10+ from python.org and add it to system PATH.
    echo.
    echo >> startup.log [CRITICAL ERROR] Python is not installed or not found in system PATH.
    pause
    exit /b 1
)
for /f "tokens=*" %%v in ('python --version') do set PYTHON_VERSION=%%v
echo Found: !PYTHON_VERSION!
echo.

:: 4. Run preflight diagnostics, dependencies, and port checks
echo [3/4] Running pre-flight diagnostics and dependency checks...
python startup_check.py
set PREFLIGHT_CODE=!errorlevel!

:: Handle missing dependencies (Exit Code 10)
if !PREFLIGHT_CODE! equ 10 (
    echo.
    echo Installing missing requirements from requirements.txt...
    python -m pip install -r requirements.txt
    if !errorlevel! neq 0 (
        echo.
        echo [CRITICAL ERROR] Failed to install missing dependencies via pip.
        echo Command failed: python -m pip install -r requirements.txt
        echo Check your network connection or Python permissions.
        echo See startup.log for details.
        pause
        exit /b 1
    )
    echo Re-running pre-flight diagnostics...
    python startup_check.py
    set PREFLIGHT_CODE=!errorlevel!
)

:: Handle server already running (Exit Code 2)
if !PREFLIGHT_CODE! equ 2 (
    echo.
    echo ========================================================================
    echo  NOTICE: The presentation server is ALREADY ACTIVE on http://127.0.0.1:5000/
    echo  Browser tab has been opened to the active session.
    echo ========================================================================
    echo.
    pause
    exit /b 0
)

:: Handle preflight errors
if !PREFLIGHT_CODE! neq 0 (
    echo.
    echo [CRITICAL ERROR] Pre-flight checks failed with exit code: !PREFLIGHT_CODE!
    echo Check startup.log for error details.
    pause
    exit /b !PREFLIGHT_CODE!
)
echo.

:: 5. Launch Presentation Server
echo [4/4] Launching presentation application...
echo The application will automatically open your default browser when ready.
echo.
python app.py
set APP_EXIT_CODE=!errorlevel!

if !APP_EXIT_CODE! neq 0 (
    echo.
    echo ========================================================================
    echo  [APPLICATION ERROR] Flask server stopped with exit code: !APP_EXIT_CODE!
    echo  Command that failed: python app.py
    echo  Please inspect the error details above or in startup.log.
    echo ========================================================================
    echo.
) else (
    echo.
    echo Server session ended normally.
)

pause
exit /b !APP_EXIT_CODE!
