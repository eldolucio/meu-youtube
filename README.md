# meu **youtube** 🌑
> Dashboard industrial focado em subscrições, privacidade e produtividade (Updated 2026).

![Preview do Dashboard](screenshot.png)

## ⚙️ O que é este projeto?

O **meu-youtube** é um dashboard privado e ultra-leve projetado para quem usa o YouTube como ferramenta de trabalho e estudo. Ele elimina o ruído algorítmico, anúncios e distrações, mantendo o foco apenas no conteúdo que você escolheu seguir.

---

## 🚀 Destaques (Features)

- **Estética Industrial**: Design minimalista com foco em alto contraste e tipografia **Barlow**.
- **OLED Black Mode**: Fundo em preto absoluto (`#000000`) para máxima imersão.
- **2026 Ready**: Suporte total para importação via **Google Takeout CSV** (o novo padrão do YouTube).
- **No-Ads Player**: Utiliza `youtube-nocookie.com` para evitar rastreamento e publicidade.
- **Filtro de Ruído**: Opções integradas para ocultar *Shorts*, *Live Streams* e palavras-chave.
- **SPA Experience**: Navegação rápida via AJAX.

---

## 🛠️ Como importar seu feed (Atualizado 2026)

Como o YouTube removeu a exportação direta de XML, siga estes passos oficiais:

1. Acesse o **[Google Takeout](https://takeout.google.com/)**.
2. Clique em **"Desmarcar tudo"**.
3. Marque apenas **"YouTube e YouTube Music"**.
4. Clique em **"Todos os dados do YouTube incluídos"** e deixe marcado apenas **"subscriptions"**.
5. Avance, crie a exportação e baixe o arquivo ZIP.
6. Dentro do ZIP, procure pela pasta `subscriptions` e localize o arquivo **`subscriptions.csv`**.
7. No seu Dashboard, abra a **Engrenagem** e faça o upload desse arquivo `.csv`.

---

## 📦 Instalação e Deploy

### Deploy na Vercel (Recomendado)
1. Conecte seu repositório GitHub à Vercel.
2. O sistema detectará automaticamente o `vercel.json` e o `requirements.txt`.
3. Clique em **Deploy**.

### Rodando Localmente
1. Instale as dependências: `pip install -r requirements.txt`.
2. Execute: `python app.py`.

---

**Tecnologias**: Python (Antigravity/Flask), Vercel, JavaScript Vanilla, CSS Industrial.
