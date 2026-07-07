param(
    [Parameter(Mandatory = $true)]
    [string]$SkillsRoot
)

# Resolve root path
$SkillsRoot = Resolve-Path $SkillsRoot

# Find all SKILL.md files directly inside skill folders
Get-ChildItem -Path $SkillsRoot -Directory | ForEach-Object {
    $skillFolder = $_
    $skillFile = Join-Path $skillFolder.FullName "SKILL.md"

    if (Test-Path $skillFile) {
        $newFileName = "$($skillFolder.Name).md"
        $newFilePath = Join-Path $skillFolder.FullName $newFileName

        if (Test-Path $newFilePath) {
            Write-Warning "Skipping '$skillFile' because '$newFileName' already exists."
        }
        else {
            Rename-Item -Path $skillFile -NewName $newFileName
            Write-Host "Renamed: $skillFile -> $newFileName"
        }
    }
    else {
        Write-Host "No SKILL.md found in: $($skillFolder.FullName)"
    }
}