$scriptsDir = Get-Location

# Install dependencies
set-location ..
pip install -r requirements.txt
set-location docs
pip install -r requirements.txt

# Remove old docs
Remove-Item -Recurse html

# Build docs
sphinx-apidoc -o apidocs ../TenshiTranslator ../TenshiTranslator/TenshiTranslatorCLI.py --separate
make html

# Extract docs
copy-item -Path build\html -Destination ..\docs -Recurse

# Remove build files
Remove-Item -Recurse build
Remove-Item -Recurse apidocs

# Return to scripts directory
Set-Location $scriptsDir