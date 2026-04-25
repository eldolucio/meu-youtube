# meu **youtube** 🌑 v2.5.0
> O seu dock de monitoramento industrial ultra-rápido, livre de distrações e focado em alta performance.

[![Static Showcase (GitHub)](https://img.shields.io/badge/Showcase-GitHub_Pages-lime?style=for-the-badge&logo=github)](https://eldolucio.github.io/meu-youtube/)
[![Manifesto](https://img.shields.io/badge/Manifesto-Independência_Digital-white?style=for-the-badge)](https://eldolucio.github.io/meu-youtube/sobre)

![Preview do Dashboard](screenshot.png)

## ⚙️ O que é este projeto?

O **meu-youtube** não é apenas mais um leitor de vídeos; é um **Monitor Tecnológico Industrial** feito para profissionais que precisam de referências sem o ruído do algoritmo do YouTube. 

Ele elimina anúncios, shorts e recomendações viciantes, entregando um feed puro, preto absoluto (OLED) e totalmente sob seu controle.

---

## 🚀 Funcionalidades Principais

### 🌓 Monitor de Edição (Auto-Refresh Pandora)
O dashboard conta com um **Auto-Refresh Assíncrono**. Uma linha de progresso finíssima no topo indica a próxima varredura de vídeos. Ele atualiza seu feed em segundo plano sem interromper a navegação.

### 👤 Gestão Multi-Perfil
Suporte a múltiplos perfis com categorias de filtragem:
- **Adulto**: Acesso total, monitoramento profissional.
- **Adolescente**: Filtros de conteúdo moderados.
- **Criança**: Filtro restritivo automático.

### 🎨 Estética Industrial OLED
Fundo em **#000000** real, tipografia **Barlow 900** e acentos em **Verde Limão**. Desenhado para máxima economia de energia e foco visual.

---

## 🛠️ Como Instalar e Rodar com Docker (Recomendado)

A versão completa com sincronização RSS e banco de dados está disponível neste repositório e foi construída para rodar perfeitamente em containers.
> **Nota de Testes:** O ambiente de execução e as imagens Docker são ativamente testados em uma **Máquina Virtual com Windows**.

### Instalação Rápida via Docker (Apenas Linux)

Se você estiver rodando um servidor ou máquina virtual Linux (Ubuntu/Debian) do zero, pode rodar o super-comando abaixo. Ele instala o Docker automaticamente, baixa o código, sobe os containers e já abre o navegador:

```bash
cd ~ ; sudo apt update ; sudo apt install -y curl git python3 ; curl -fsSL https://get.docker.com | sudo sh ; sudo rm -rf meu-youtube ; git clone https://github.com/eldolucio/meu-youtube.git ; cd meu-youtube ; sudo docker compose up -d --build ; python3 -c "import webbrowser, time; time.sleep(2); webbrowser.open('http://127.0.0.1:5005')"
```

### Instalação Passo a Passo (Windows, Mac e Linux)

1. Certifique-se de ter o [Docker](https://www.docker.com/) instalado em sua máquina.
2. Clone este repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/eldolucio/meu-youtube.git
   cd meu-youtube
   ```
3. Acesse a pasta raiz do projeto via terminal e suba os containers:
   ```bash
   docker-compose up -d --build
   ```
4. O servidor será iniciado em segundo plano. Acesse pelo navegador: `http://localhost:5005`

---

## 💻 Como Instalar Manualmente (Sem Docker)

Se preferir não utilizar o Docker, você pode rodar o projeto diretamente com Python.

### Instalação Completa do Zero (Máquinas Novas)

Se você **não tem nada instalado** e quer baixar e configurar tudo automaticamente de uma só vez (Python, Git, dependências e iniciar o servidor), abra o seu terminal e rode o comando correspondente ao seu sistema. Todos eles limpam tentativas anteriores, baixam o código, instalam tudo de forma isolada e já abrem o navegador:

**No Windows (Abra o PowerShell como Administrador):**
```powershell
cd ~ ; Remove-Item -Recurse -Force .\venv -ErrorAction SilentlyContinue ; Remove-Item -Recurse -Force meu-youtube -ErrorAction SilentlyContinue ; winget install -e --id Git.Git --accept-source-agreements --accept-package-agreements ; winget install -e --id Python.Python.3.11 --accept-source-agreements --accept-package-agreements ; $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User") ; git clone https://github.com/eldolucio/meu-youtube.git ; cd meu-youtube ; python -m venv venv ; .\venv\Scripts\python.exe -m pip install -r requirements.txt ; .\venv\Scripts\python.exe app.py
```

**No Mac (Terminal):**
```bash
cd ~ && rm -rf venv meu-youtube && git clone https://github.com/eldolucio/meu-youtube.git && cd meu-youtube && python3 -m venv venv && source venv/bin/activate && pip3 install -r requirements.txt && python3 app.py
```

**No Linux - Ubuntu/Debian (Bash):**
```bash
cd ~ ; sudo rm -rf venv meu-youtube ; sudo apt update ; sudo apt install -y git python3 python3-venv python3-pip ; git clone https://github.com/eldolucio/meu-youtube.git ; cd meu-youtube ; python3 -m venv venv ; source venv/bin/activate ; pip3 install -r requirements.txt ; python3 app.py
```

### Instalação Rápida (One-Liner)

Se você **já tem o repositório clonado e o Python instalado**, abra o terminal na pasta do projeto e rode **um único comando**:

**No Windows (CMD):**
```cmd
python -m venv venv && .\venv\Scripts\python.exe -m pip install -r requirements.txt && .\venv\Scripts\python.exe app.py
```

**No Windows (PowerShell):**
```powershell
python -m venv venv ; .\venv\Scripts\python.exe -m pip install -r requirements.txt ; .\venv\Scripts\python.exe app.py
```

**No Mac/Linux (Bash):**
```bash
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python3 app.py
```

### Instalação Passo a Passo

1. Certifique-se de ter o [Python 3.8+](https://www.python.org/downloads/) instalado em sua máquina.
2. Clone este repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/eldolucio/meu-youtube.git
   cd meu-youtube
   ```
3. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
4. Instale as dependências executando o Python diretamente do ambiente virtual (evita erros de permissão no Windows):
   ```bash
   # No Windows (CMD/PowerShell):
   .\venv\Scripts\python.exe -m pip install -r requirements.txt

   # No Mac/Linux:
   source venv/bin/activate
   pip install -r requirements.txt
   ```
5. Inicie o servidor:
   ```bash
   # No Windows:
   .\venv\Scripts\python.exe app.py

   # No Mac/Linux:
   python3 app.py
   ```
6. O servidor será iniciado. Acesse pelo navegador: `http://localhost:5005`

---

## 🌐 Demonstração (Vitrine Estática)

Esta versão no GitHub Pages é uma **demonstração interativa**. Você pode explorar a interface, trocar o tema (Light/Dark) e abrir o player de vídeo para ver como o front-end funciona na prática sem precisar instalar nada.

---

**Tecnologias**: Python (Flask), Docker, SQLite, HTML5 Semântico, CSS Industrial, JavaScript.
**Desenvolvido para Máxima Produtividade.** 🌑⚙️📈

---

## 🛑 Troubleshooting (Erros Comuns e Soluções)

Durante o desenvolvimento e testes exaustivos em diversas arquiteturas (Windows, Mac e Máquinas Virtuais Linux ARM64), documentamos as soluções para os erros de ambiente mais comuns:

### 1. Erro C++ no Windows (ARM64)
**Erro:** `Microsoft Visual C++ 14.0 or greater is required` durante a instalação das dependências (pip install).
**Causa:** Falta de compiladores para pacotes C (como antigas versões do Postgres ou leitores XML) em processadores ARM.
**Solução Resolvida:** Adaptamos o `requirements.txt` para instalar o adaptador Postgres (`psycopg2`) apenas em servidores Linux de produção, mantendo o banco SQLite nativo e blindado para uso local.

### 2. GPG Key Error no Debian/Ubuntu
**Erro:** O comando trava no início com `The following signatures couldn't be verified...` (Geralmente repositórios Mozilla/Firefox).
**Causa:** Chaves de segurança de repositórios de terceiros vencidas no Linux.
**Solução:** Nossos scripts "One-Liner" agora utilizam `;` em vez de `&&` após o `apt update` para ignorar esses falsos-positivos e continuar a instalação. Se quiser limpar o erro do seu Linux, rode: `sudo rm -f /etc/apt/sources.list.d/*.list && sudo apt update`.

### 3. "The connection was reset" no Docker
**Erro:** O container sobe, a porta 5005 fica aberta, mas o navegador não carrega a página.
**Causa 1 (Bind de IP):** O Flask estava restrito ao localhost interno do container. Foi corrigido mudando a escuta para `0.0.0.0`.
**Causa 2 (Bug do SQLite no Docker):** Mapear um banco SQLite como um volume nomeado no `docker-compose` faz o Docker criar uma **pasta** com o nome do arquivo, causando crash fatal no Python. Removido o mapeamento isolado; o banco agora persiste nativamente no volume `/app`.

### 4. Permissão Negada ao Deletar a Pasta (rm -rf)
**Erro:** `rm: cannot remove '__pycache__': Permission denied` seguido de erro no `git clone`.
**Causa:** Quando rodado via Docker, o Python dentro do container (usuário Root) compila arquivos de cache (`.pyc`). Ao tentar deletar a pasta como um usuário comum, o sistema bloqueia.
**Solução Resolvida:** Os comandos de instalação rápida agora utilizam `sudo rm -rf` por padrão para obliterar vestígios de instalações anteriores.

### 5. "Address already in use" (Porta 5005 Ocupada)
**Erro:** O Python avisa que a porta 5005 já está em uso por outro programa.
**Causa:** Existe um container Docker "fantasma" rodando em segundo plano (`-d`) de uma tentativa anterior, ou outro processo do Python.
**Solução:** Mate o processo travado rodando: `sudo docker rm -f meu-youtube-v2` e rode o aplicativo novamente.
