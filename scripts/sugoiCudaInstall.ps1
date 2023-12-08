$curDir = $PWD

Function Get-Folder($initialDirectory="") {
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

Write-Host "Please select the install folder (Check new window, might be in the background)" -ForegroundColor Yellow
$ocrfolder = Get-Folder
$installtest = "$ocrfolder\Code\Sugoi-ASMR-Translator.bat";

$Env:PATH = "$ocrfolder\Code\Power-Source\Python39;$ocrfolder\Code\Power-Source\Python39\Scripts;$Env:PATH"

if (-not(Test-Path -Path $installtest -PathType Leaf)) {
    Write-Host "Could not find Sugoi-Toolkit (click here).bat, not a sugoi 2.0 install folder?" -ForegroundColor Red
    return;
}

Write-Host "Installing Pytorch" -ForegroundColor Green
Set-Location $ocrfolder
cd Code\Power-Source\Python39
./python -m pip install pip
cd Scripts
./pip3 install --upgrade torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118

Write-Host "Downgrading numpy (fairseq version is to old)" -ForegroundColor Green
./pip3 install --upgrade --no-deps numpy==1.23.0

Write-Host "Installing: Multiline Cuda Script" -ForegroundColor Green
Set-Location $curDir
$ccc = "$curDir\Files\flaskServer-multiline.py";
$ttt = "$ocrfolder\code\backendServer\Program-Backend\Sugoi-Japanese-Translator\offlineTranslation\fairseq\flaskServer.py"
cp "$ccc" "$ttt"

Write-Host "" -ForegroundColor Green
Write-Host "Installation done." -ForegroundColor Green
Read-Host -Prompt "Press enter to exit."