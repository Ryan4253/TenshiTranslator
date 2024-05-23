$scriptsDir = Get-Location

# Install dependencies
set-location ..
pip install -r requirements.txt
pip install pyinstaller

# Build executable
pyinstaller TenshiTranslator/TenshiTranslatorGUI.py --onefile --distpath dist

# Copy executable to bin folder
If (!(test-path bin)){
    mkdir bin
}
Copy-Item -Path dist/TenshiTranslatorGUI.exe -Destination bin/TenshiTranslator.exe

# Remove build files
Remove-Item -Recurse build
Remove-Item -Recurse TenshiTranslatorGUI.spec
Remove-Item -Recurse dist/TenshiTranslatorGUI.exe

# Return to scripts directory
Set-Location $scriptsDir