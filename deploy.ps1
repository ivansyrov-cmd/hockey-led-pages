# Deploy to GitHub Pages (run after: gh auth login)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

$repoName = "hockey-led-pages"

if (-not (gh auth status 2>$null)) {
    Write-Host "Run first: gh auth login" -ForegroundColor Yellow
    exit 1
}

$owner = gh api user -q .login
Write-Host "Account: $owner"

if (-not (git remote 2>$null | Select-String origin)) {
    gh repo create $repoName --public --source=. --remote=origin --description "Hockey ice payment tracker"
    git push -u origin main
} else {
    git push origin main
}

gh api "repos/$owner/$repoName/pages" -X POST `
    -f "build_type=legacy" `
    -f "source[branch]=main" `
    -f "source[path]=/" 2>$null

$url = "https://$owner.github.io/$repoName/"
Write-Host ""
Write-Host "Done! Site URL (may take 1-2 min):" -ForegroundColor Green
Write-Host $url
