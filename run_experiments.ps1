# PowerShell Script for automated cognitive experimentation of CQ Mythos
# Designed for Windows PowerShell / Core. Runs unified diagnostic suites with automatic Python resolution.

Clear-Host
$Host.UI.RawUI.WindowTitle = "🌌 CQ MYTHOS | COGNITIVE EXPERIMENTATION PLATFORM"

# Gorgeous ANSI Colors for premium experience
$C_PINK = "[38;2;255;110;180m"
$C_CYAN = "[38;2;0;229;255m"
$C_BLUE = "[38;2;100;149;237m"
$C_GREEN = "[38;2;50;205;50m"
$C_YELLOW = "[38;2;255;215;0m"
$C_RED = "[38;2;255;69;0m"
$C_RESET = "[0m"
$C_BOLD = "[1m"

Write-Host -ForegroundColor Cyan "   _  _   _  _   _  _   _  _   _  _   _  _   _  _   _  _"
Write-Host -ForegroundColor Magenta "  ( \/ ) ( \/ ) ( \/ ) ( \/ ) ( \/ ) ( \/ ) ( \/ ) ( \/ )"
Write-Host -ForegroundColor Cyan "   \  /   \  /   \  /   \  /   \  /   \  /   \  /   \  /"
Write-Host -ForegroundColor Magenta "    \/     \/     \/     \/     \/     \/     \/     \/"
Write-Host ""
Write-Host -ForegroundColor Yellow "   🌌 CQ MYTHOS | AUTONOMOUS COGNITIVE EXPERIMENTATION PLATFORM"
Write-Host -ForegroundColor DarkCyan "   ============================================================="
Write-Host ""

# ==============================================================================
# PHASE 1: DYNAMIC PYTHON RESOLUTION
# ==============================================================================
Write-Host -ForegroundColor Gray "[*] Initializing telemetry pipeline. Resolving local Python interpreter..."

$resolvedPython = $null
$pyCheck = Get-Command python -ErrorAction SilentlyContinue

if ($pyCheck) {
    # Check if this is the dummy App Store execution alias
    $pyTest = & python --version 2>$null
    if ($pyTest -like "*Python 3*") {
        $resolvedPython = "python"
        Write-Host -ForegroundColor Green "  ✓ Found system Python in Path: $($pyTest)"
    }
}

if (-not $resolvedPython) {
    # Search common directories for active Python installation
    $commonPaths = @(
        "$env:USERPROFILE\AppData\Local\Programs\Python\Python312\python.exe",
        "$env:USERPROFILE\AppData\Local\Programs\Python\Python311\python.exe",
        "$env:USERPROFILE\AppData\Local\Programs\Python\Python310\python.exe",
        "C:\Program Files\Python312\python.exe",
        "C:\Program Files\Python311\python.exe",
        "C:\Program Files\Python310\python.exe",
        "C:\Python312\python.exe",
        "C:\Python311\python.exe",
        "C:\Python310\python.exe"
    )
    foreach ($path in $commonPaths) {
        if (Test-Path $path) {
            $resolvedPython = $path
            Write-Host -ForegroundColor Green "  ✓ Located local Python binary: $resolvedPython"
            break
        }
    }
}

# If Python is missing completely, offer automatic installation via Winget
if (-not $resolvedPython) {
    Write-Host "" -NoNewline
    Write-Host -ForegroundColor Red "⚠️  Python 3.10+ was not found on your system PATH or local folders."
    Write-Host -ForegroundColor Yellow "[*] Initiating automatic, silent deployment of Python 3.11 via Winget..."
    
    # Run Winget install silently
    Start-Process winget -ArgumentList "install --id Python.Python.3.11 --exact --silent --accept-package-agreements --accept-source-agreements" -NoNewWindow -Wait
    
    # Reload environment Path
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
    
    # Search standard paths again
    $commonPaths = @(
        "$env:USERPROFILE\AppData\Local\Programs\Python\Python311\python.exe",
        "$env:USERPROFILE\AppData\Local\Programs\Python\Python312\python.exe",
        "C:\Program Files\Python311\python.exe",
        "C:\Program Files\Python312\python.exe"
    )
    foreach ($path in $commonPaths) {
        if (Test-Path $path) {
            $resolvedPython = $path
            break
        }
    }
    
    if (-not $resolvedPython) {
        Write-Host -ForegroundColor Red "❌ Automatic installation failed or requires system reboot."
        Write-Host -ForegroundColor Yellow "Please install Python manually from https://python.org and run this script again."
        Read-Host "Press enter to exit"
        Exit 1
    }
    Write-Host -ForegroundColor Green "✅ Python successfully deployed: $resolvedPython"
}

# ==============================================================================
# PHASE 2: VIRTUAL ENVIRONMENT INTEGRITY CHECK
# ==============================================================================
Write-Host -ForegroundColor Gray "[*] Checking virtual environment integrity..."

$venvRoot = Join-Path $PSScriptRoot "venv"
if (-not (Test-Path $venvRoot)) {
    Write-Host -ForegroundColor Yellow "[!] Virtual environment venv is missing. Spawning a new container..."
    & $resolvedPython -m venv venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host -ForegroundColor Red "❌ Error: Failed to initialize virtual environment."
        Read-Host "Press enter to exit"
        Exit 1
    }
    Write-Host -ForegroundColor Green "  ✓ Created new virtual environment successfully."
}

# Activate Virtual Environment
Write-Host -ForegroundColor Gray "[*] Injecting virtual environment context into session..."
$activateScript = Join-Path $venvRoot "Scripts\Activate.ps1"
if (Test-Path $activateScript) {
    . $activateScript
} else {
    # Fallback to local execution
    $env:PATH = "$(Join-Path $venvRoot 'Scripts');" + $env:PATH
}

# Upgrade pip and install package in editable mode
Write-Host -ForegroundColor Gray "[*] Synchronizing project dependencies..."
python -m pip install --upgrade pip --quiet
python -m pip install -e . --quiet
if ($LASTEXITCODE -ne 0) {
    Write-Host -ForegroundColor Yellow "⚠️  Warning: Package synchronizer threw an error, continuing diagnostic run..."
}

# ==============================================================================
# PHASE 3: EXECUTE AUTOMATED DIAGNOSTIC SUITE
# ==============================================================================
Write-Host ""
Write-Host -ForegroundColor Magenta "🧪 SPINDLE LAUNCHER | EXECUTING MASTER TELEMETRY ENGINE"
Write-Host -ForegroundColor Magenta "--------------------------------------------------------"

# Launch the unified master automation in python run.py
python run.py experiment_automation

Write-Host ""
Write-Host -ForegroundColor Gray "[*] Telemetry run finished. Restoring terminal session context."
Write-Host -ForegroundColor Green "✓ Complete. Press any key to release terminal focus."
Read-Host
