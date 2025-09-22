param(
    [switch]$WithTests
)

$ErrorActionPreference = "Stop"

function Write-Info($msg) { Write-Host "[INFO] $msg" -ForegroundColor Cyan }
function Write-Ok($msg) { Write-Host "[ OK ] $msg" -ForegroundColor Green }

Write-Info "Creating virtual environment (./venv) if missing..."
if (!(Test-Path -Path "venv")) {
    python -m venv venv
}

Write-Ok "Virtual environment ready."

Write-Info "Activating virtual environment..."
& "venv/Scripts/Activate.ps1"

Write-Info "Upgrading pip and installing runtime dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

if ($WithTests) {
    Write-Info "Installing development/testing dependencies..."
    pip install -r requirements-dev.txt
    Write-Info "Running tests..."
    python -m pytest -q
}

Write-Ok "Done. Use 'venv\\Scripts\\Activate.ps1' to activate next time."

