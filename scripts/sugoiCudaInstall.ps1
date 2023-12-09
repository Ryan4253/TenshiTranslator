$scriptsDir = $PWD

Function Select-Folder($initialDirectory="") {
    [System.Reflection.Assembly]::LoadWithPartialName("System.windows.forms")|Out-Null

    $foldername = New-Object System.Windows.Forms.FolderBrowserDialog
    $foldername.Description = "Select Sugoi Toolkit folder"
    $foldername.rootfolder = "MyComputer"
    $foldername.SelectedPath = $initialDirectory

    if($foldername.ShowDialog() -eq "OK")
    {
        $folder += $foldername.SelectedPath
    }
    return $folder
}

# Select Sugoi Toolkit folder
Write-Host "Please select the Sugoi Toolkit folder  (check background for popups)" -ForegroundColor Yellow
$sugoi = Select-Folder
$sugoiCheck = "$sugoi/Sugoi-Toolkit (click here).bat";

# Folder check
if (-not(Test-Path -Path $sugoiCheck -PathType Leaf)) {
    Write-Host "Could not find Sugoi-Toolkit (click here).bat, incorrect folder selected" -ForegroundColor Red
    return;
}

# Install pytorch
Write-Host "Installing Pytorch" -ForegroundColor Green
Set-Location $sugoi
Set-Location Code/Power-Source/Python39
./python -m pip install pip
Set-Location Scripts
./pip3 install --upgrade torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118

# Downgrade Numpy
Write-Host "Downgrading Numpy" -ForegroundColor Green
./pip3 install --upgrade --no-deps numpy==1.23.0

# Install flask server
Write-Host "Installing Updated Flask Server" -ForegroundColor Green
Set-Location $scriptsDir
$file = "$scriptsDir/assets/flaskServer.py";
$target = "$sugoi/code/backendServer/Program-Backend/Sugoi-Japanese-Translator/offlineTranslation/fairseq/flaskServer.py"
Copy-Item -Path "$file" -Destination "$target"

# Completion
Write-Host "Installation complete." -ForegroundColor Green
Read-Host -Prompt "Press enter to exit."

# Return to scripts directory
Set-Location $scriptsDir