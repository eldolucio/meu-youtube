# MEU YOUTUBE // Dashboard de Produtividade

Um dashboard minimalista e industrial focado em **consumo de conteúdo sem ruído**. Este projeto transforma o seu YouTube em uma ferramenta de trabalho organizada, eliminando anúncios, recomendações algorítmicas e distrações.

## 🚀 Funcionalidades
- **Filtro de Ruído**: Esconda Shorts e vídeos por palavras-chave (Blacklist).
- **Player "Semi-Offline"**: Player modal usando `youtube-nocookie.com` para máxima privacidade e economia de banda.
- **Design Industrial**: Estética OLED Black com acentos industriais (`#c8f135`).
- **Navegação SPA**: Histórico, Biblioteca e Inscrições sem recarregamento de página (AJAX).
- **Gestão Local**: Seus dados de navegação ficam no seu navegador (`localStorage`), sem banco de dados externo.

## 🛠️ Stack Técnica
- **Backend**: Python (Flask/Antigravity)
- **Frontend**: JavaScript Vanilla, CSS Moderno (Variables/Grid/Flexbox)
- **Parsing**: Feedparser para leitura de RSS
- **Deploy**: Otimizado para Vercel

## 📦 Como Instalar (Local)
1. Clone o repositório: `git clone https://github.com/seu-user/meu-youtube.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Inicie o servidor: `python app.py`
4. Acesse: `http://localhost:8000`

## ⚙️ Configuração
Importe o seu arquivo `subscription_manager.xml` (exportado do YouTube Subscription Manager) diretamente na barra lateral de configurações para carregar o seu feed privado.

---
*Focado em performance. Sem cookies desnecessários. Sem algoritmos.*
