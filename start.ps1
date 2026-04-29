# meu-youtube: Script de Inicialização Industrial (Windows)
# ---------------------------------------------------------
# Este script configura o ambiente e inicia o dashboard v2.6.0

Write-Host "🌑 INICIANDO MEU YOUTUBE INDUSTRIAL v2.6.0" -ForegroundColor Cyan

# 1. Verificar se o Python está instalado
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ ERRO: Python não encontrado. Por favor, instale o Python 3.10+." -ForegroundColor Red
    pause
    exit
}

# 2. Criar ambiente virtual se não existir
if (!(Test-Path "venv")) {
    Write-Host "⚙️ Criando ambiente virtual isolado (venv)..." -ForegroundColor Yellow
    python -m venv venv
}

# 3. Instalar/Atualizar dependências
Write-Host "📦 Verificando dependências..." -ForegroundColor Yellow
.\venv\Scripts\python.exe -m pip install --upgrade pip
.\venv\Scripts\python.exe -m pip install -r requirements.txt

# 4. Iniciar o Servidor
Write-Host "🚀 Lançando servidor em http://localhost:5005" -ForegroundColor Green
Write-Host "Pressione CTRL+C para encerrar." -ForegroundColor DarkGray

# Pequeno delay antes de abrir o navegador
Start-Sleep -Seconds 2
Start-Process "http://localhost:5005"

.\venv\Scripts\python.exe app.py
