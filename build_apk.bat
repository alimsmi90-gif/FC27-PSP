@echo off
setlocal
cd /d "%~dp0"
echo ========================================
echo FC 27 - Android APK Build
echo ========================================
echo.
where wsl >nul 2>&1
if errorlevel 1 (
  echo WSL is not installed or not available in PATH.
  echo Install/configure WSL first, then run this file again.
  pause
  exit /b 1
)

wsl bash -lc "cd \"$(wslpath -a '%cd%')\" && buildozer -v android debug"
set ERR=%ERRORLEVEL%

echo.
if %ERR%==0 (
  echo Build completed successfully.
  echo The APK should be in the bin folder.
) else (
  echo Build failed. Read the error above.
)
pause
exit /b %ERR%
