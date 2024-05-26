$scriptsDir = Get-Location

# Install dependencies
set-location ..
pip install -r requirements.txt
pip install pyinstaller

# Build executable
pyinstaller TenshiTranslator/TenshiTranslatorCLI.py --onefile --distpath dist

# Copy executable to bin folder
If (!(test-path bin)){
    mkdir bin
}
Copy-Item -Path dist/TenshiTranslatorCLI.exe -Destination bin/TenshiTranslatorCLI.exe

# Remove build files
Remove-Item -Recurse build
Remove-Item -Recurse TenshiTranslatorCLI.spec
Remove-Item -Recurse dist/TenshiTranslatorCLI.exe

# Return to scripts directory
Set-Location $scriptsDir