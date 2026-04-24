# meu **youtube** 🌑
> Dashboard industrial focado em subscrições, privacidade e produtividade.

![Preview do Dashboard](screenshot.png)

## ⚙️ O que é este projeto?

O **meu-youtube** é um dashboard privado e ultra-leve projetado para quem usa o YouTube como ferramenta de trabalho e estudo. Ele elimina o ruído algorítmico, anúncios e distrações, mantendo o foco apenas no conteúdo que você escolheu seguir.

---

## 🚀 Destaques (Features)

- **Estética Industrial**: Design minimalista com foco em alto contraste e tipografia **Barlow**.
- **OLED Black Mode**: Fundo em preto absoluto (`#000000`) para máxima imersão e economia de energia.
- **No-Ads Player**: Utiliza `youtube-nocookie.com` para evitar rastreamento e publicidade.
- **Filtro de Ruído**: Opções integradas para ocultar *Shorts*, *Live Streams* e palavras-chave específicas.
- **SPA Experience**: Navegação rápida via AJAX para Histórico, Biblioteca e Inscrições.
- **Privacidade Total**: Seus dados de navegação e preferências são salvos apenas no seu navegador (`localStorage`).

---

## 🛠️ Como importar seu feed

Para carregar suas inscrições sem precisar de APIs complexas, siga este processo:

1. Acesse o [Gerenciador de Inscrições do YouTube](https://www.youtube.com/subscription_manager).
2. Vá até o final da página e clique em **Exportar Inscrições**.
3. No seu Dashboard, clique no ícone de **Engrenagem** na barra lateral.
4. Escolha o arquivo `.xml` baixado e o sistema carregará seu feed instantaneamente.

---

## 📦 Instalação e Deploy

### Deploy na Vercel (Recomendado)
Este projeto está otimizado para a **Vercel**. 
1. Conecte seu repositório GitHub à Vercel.
2. O sistema detectará automaticamente o `vercel.json` e o `requirements.txt`.
3. Clique em **Deploy** e seu dashboard estará online.

### Rodando Localmente
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Execute: `python app.py`.
4. Acesse `http://localhost:8000`.

---

## 🌑 Sobre o Design "2016"
O layout foi inspirado na era de ouro da interface do YouTube, onde a simplicidade e a lista de vídeos eram o centro da experiência, antes da saturação de recomendações algorítmicas. Combinado com o **OLED Black**, ele oferece uma leitura limpa e técnica para o MacBook Air.

---

**Tecnologias**: Python (Antigravity/Flask), Vercel, JavaScript Vanilla, CSS Industrial.
