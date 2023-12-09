$scriptsDir = Get-Location

# Install dependencies
set-location ..
python -m pip install --upgrade pip
python -m pip install --upgrade build

# Build package
python -m build

# Return to scripts directory
Set-Location $scriptsDir