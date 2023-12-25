$scriptsDir = Get-Location

# Install dependencies
set-location ..
pip install -r requirements.txt
set-location test
pip install -r requirements.txt

# Run tests
set-location ..
pytest --cov-config=.coveragerc --cov=TenshiTranslator --cov-report=xml test/

# Remove cache
Remove-Item -Recurse .pytest_cache
Remove-Item -Recurse .coverage

# Return to scripts directory
Set-Location $scriptsDir