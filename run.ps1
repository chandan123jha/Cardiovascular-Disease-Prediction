# PowerShell script to run the Cardiovascular Disease Prediction application
# This handles paths with spaces properly

$projectDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$appDir = Join-Path $projectDir "Cardiovascular-Disease Prediction"
$pythonExe = Join-Path $projectDir ".venv-1\Scripts\python.exe"

Write-Host "Starting Cardiovascular Disease Prediction Application..." -ForegroundColor Green
Write-Host "Project Directory: $projectDir" -ForegroundColor Cyan

Set-Location -Path $appDir
& $pythonExe heartGUI_main.py

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Application failed with exit code $LASTEXITCODE" -ForegroundColor Red
    Read-Host "Press Enter to exit"
}
