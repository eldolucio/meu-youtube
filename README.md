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

### Instalação Rápida (One-Liner)

Se você já tem o repositório clonado e o Python instalado, instale todas as dependências e inicie o projeto com **um único comando**:

**No Windows (CMD):**
```cmd
python -m venv venv && .\venv\Scripts\activate && pip install -r requirements.txt && python app.py
```

**No Windows (PowerShell):**
```powershell
python -m venv venv ; .\venv\Scripts\activate ; pip install -r requirements.txt ; python app.py
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
3. Crie e ative um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Mac/Linux:
   source venv/bin/activate
   ```
4. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```
5. Inicie o servidor:
   ```bash
   python app.py
   ```
6. O servidor será iniciado. Acesse pelo navegador: `http://localhost:5005`

---

## 🌐 Demonstração (Vitrine Estática)

Esta versão no GitHub Pages é uma **demonstração interativa**. Você pode explorar a interface, trocar o tema (Light/Dark) e abrir o player de vídeo para ver como o front-end funciona na prática sem precisar instalar nada.

---

**Tecnologias**: Python (Flask), Docker, SQLite, HTML5 Semântico, CSS Industrial, JavaScript.
**Desenvolvido para Máxima Produtividade.** 🌑⚙️📈
