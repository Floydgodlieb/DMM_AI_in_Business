@echo off
cd /d %~dp0

echo ============================================
echo   Academic Pipeline - Progress Report
echo ============================================
echo.

where python >nul 2>nul
if errorlevel 1 (
    echo Python was not found on this computer.
    echo See README.md, "One-time setup", to install it.
    goto end
)

python scripts\progress.py report

echo.
echo ---- status.md ----
echo.
type status.md

:end
echo.
echo Press any key to close this window.
pause >nul
