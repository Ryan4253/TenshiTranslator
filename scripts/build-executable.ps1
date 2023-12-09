$scriptsDir = Get-Location

# Install dependencies
set-location ..
pip install -r requirements.txt
pip install pyinstaller

# Build executable
pyinstaller TenshiTranslator/api.py --onefile --distpath dist

# Copy executable to backend folder
If (!(test-path Backend)){
    mkdir Backend
}
Copy-Item -Path dist/api.exe -Destination Backend/api.exe

# Remove build files
Remove-Item -Recurse build
Remove-Item -Recurse api.spec
Remove-Item -Recurse dist/api.exe

# Return to scripts directory
Set-Location $scriptsDir