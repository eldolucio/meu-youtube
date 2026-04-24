# meu **youtube** 🌑 v2.2
> O seu dock de monitoramento ultra-rápido, livre de distrações e focado em alta performance (2026).

![Preview do Dashboard](screenshot.png)

## ⚙️ O que é este projeto?

O **meu-youtube** não é apenas mais um leitor de vídeos; é um **Monitor Tecnológico Industrial** feito para editores de vídeo, criadores e profissionais que precisam de referências sem o ruído do algoritmo do YouTube. 

Ele elimina anúncios, shorts e recomendações viciantes, entregando um feed puro, preto absoluto (OLED) e totalmente sob seu controle.

---

## 🚀 Novas Funcionalidades (v2.2)

### 🌓 Monitor de Edição (Auto-Refresh)
O dashboard agora conta com um **Auto-Refresh Assíncrono**. Uma linha de progresso finíssima no topo indica a próxima varredura de vídeos. Ele atualiza seu feed em segundo plano sem interromper o que você está assistindo no player. Ideal para deixar um monitor de lado enquanto você trabalha em outra tela.

### 👤 Gestão Multi-Perfil & Segurança
Agora a casa inteira pode usar! Implementamos uma gestão completa de perfis baseada em idade:
- **Adulto (18+)**: Acesso total, focado em monitoramento profissional.
- **Adolescente**: Filtros de conteúdo moderados.
- **Criança**: Filtro restritivo automático (remove vídeos de política, violência, etc).
*Cada perfil tem seu próprio histórico e biblioteca de vídeos salvos.*

### 🎨 Estética Industrial OLED
Fundo em **#000000** real, tipografia **Barlow Condensed** e acentos em **Verde Limão Neon**. O dashboard foi desenhado para ser esteticamente premium e economizar energia em telas OLED.

---

## 🛠️ Como usar (Guia Rápido 2026)

### 1. Traga seus inscritos (Google Takeout)
O YouTube agora usa o formato CSV. Veja como importar:
1. Vá ao **[Google Takeout](https://takeout.google.com/)**, marque apenas **YouTube** e selecione a pasta **subscriptions**.
2. Baixe o arquivo **`subscriptions.csv`**.
3. No dashboard, abra a **Engrenagem ⚙️** e faça o upload.

### 2. Configure seu Perfil
Ao entrar pela primeira vez, crie seu perfil. Se quiser gerenciar outros usuários ou trocar de conta, clique no seu nome na barra lateral ou vá em **Gerenciar Usuários** nas configurações.

---

## 📦 Instalação e Deploy

**Deploy na Vercel (Recomendado)**:
Conecte este repositório e clique em Deploy. O sistema já está configurado para o ambiente Vercel.

**Rodando Localmente**:
1. Instale: `pip install -r requirements.txt`
2. Execute: `python app.py` (Porta padrão: `5005`)

---

**Tecnologias**: Python (Flask/Antigravity), SQLite (Perfis), AJAX/Fetch (SPA), CSS Modular Industrial.
**Desenvolvido para Máxima Produtividade.** 🌑⚙️📈
