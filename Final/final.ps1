# This script was written to be run on a daily basis via a cron job, which is not something I can do for this project
Import-Module Microsoft.Powershell.Utility
$dir = "C:\logs"

if ((Test-Path -Path $dir) -eq $false) {
    mkdir C:\logs
}

# Checking the current storage capacity of all drives on a daily basis and then logging it

function CreateLog {
    $driveUse = Get-PSDrive

    $date = Get-Date -Format "dd-MM-yyyy"
    if ((Test-Path -Path "$dir\$date.log") -eq $false) {
        New-Item "$dir\$date.log"
    }
    Get-PSDrive -PSProvider FileSystem | Out-File "$dir\$date.log"
}

CreateLog

