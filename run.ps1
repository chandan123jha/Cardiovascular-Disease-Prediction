# PowerShell script to run the Cardiovascular Disease Prediction application
# This handles paths with spaces properly

$projectDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonExe = Join-Path $projectDir ".venv\Scripts\python.exe"

Write-Host "Starting Cardiovascular Disease Prediction Application..." -ForegroundColor Green
Write-Host "Project Directory: $projectDir" -ForegroundColor Cyan

Set-Location -Path $projectDir
& $pythonExe app.py

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Application failed with exit code $LASTEXITCODE" -ForegroundColor Red
    Read-Host "Press Enter to exit"
}
