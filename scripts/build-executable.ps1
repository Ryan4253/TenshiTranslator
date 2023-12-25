$scriptsDir = Get-Location

# Install dependencies
set-location ..
pip install -r requirements.txt
pip install pyinstaller

# Build executable
pyinstaller TenshiTranslator/Backend.py --onefile --distpath dist

# Copy executable to backend folder
If (!(test-path Backend)){
    mkdir Backend
}
Copy-Item -Path dist/Backend.exe -Destination Backend/Backend.exe

# Remove build files
Remove-Item -Recurse build
Remove-Item -Recurse Backend.spec
Remove-Item -Recurse dist/Backend.exe

# Return to scripts directory
Set-Location $scriptsDir