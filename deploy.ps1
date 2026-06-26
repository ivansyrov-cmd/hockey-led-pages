# Публикация на GitHub Pages (запустить после: gh auth login)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

$repoName = "hockey-led-pages"

if (-not (gh auth status 2>$null)) {
    Write-Host "Сначала войдите в GitHub: gh auth login" -ForegroundColor Yellow
    exit 1
}

$owner = gh api user -q .login
Write-Host "Аккаунт: $owner"

if (-not (git remote get-url origin 2>$null)) {
    gh repo create $repoName --public --source=. --remote=origin --description "Учёт оплат за лёд — Hockey dads"
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
Write-Host "Готово! Страница (может открыться через 1-2 мин):" -ForegroundColor Green
Write-Host $url
Write-Host ""
Write-Host "На iPhone: Safari -> Поделиться -> На экран Домой" -ForegroundColor Cyan
