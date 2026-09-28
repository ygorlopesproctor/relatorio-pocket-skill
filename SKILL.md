---
name: relatorio-pocket
description: Use quando alguém da equipe Black Sales pedir "relatório pocket", "pré-diagnóstico", "diagnóstico pocket", "isca de diagnóstico", "relatório pro SDR mandar", "prévia pro médico antes da reunião", ou quando um SDR coletou o @ do Instagram de um médico prospect e precisa do material que vende a reunião com os sócios. NÃO usar para o deck completo da call — isso é a skill plano-de-acao.
---

# Relatório Pocket · Pré-diagnóstico de 2 páginas

> Transforma o @ de um médico prospect em um **pré-diagnóstico de DUAS páginas** (PDF + 2 PNGs) que o SDR manda no WhatsApp. **Página 1** alarma com prova: score vermelho, antes e depois do perfil, pontos críticos. **Página 2** vende a reunião com os sócios e faz o médico chegar preparado.

Formato definido pelo Ygor na reunião comercial de 24/09/2026 e ajustado em 28/09/2026. Palavras dele: *"relatório de duas páginas só: a primeira traz os pontos críticos e uma nota de 0 a 100, sempre vermelha; a segunda gera desejo pela reunião: como funciona, qual o objetivo, o que a gente vai apresentar."*

**REQUIRED SUB-SKILL:** `ig-profile` (invocar pela Skill tool). O antes e depois do perfil e a nota de Perfil saem dela, nunca de improviso.

## As duas páginas

| Página 1 · O raio-x (preto + vermelho) | Página 2 · A reunião (branco + lime) |
|---|---|
| Headline = leitura do **posicionamento** (ativo real + o furo) | Promessa: sair da zona vermelha em 90 dias |
| **Score 0–100** em medidor sempre vermelho + 4 barras | **Ingresso**: "com os sócios, ao vivo" · 40 min · Google Meet · Ygor + Sodré |
| **Antes × depois do perfil** em 2 celulares (`ig-profile`) | Objetivo da reunião em 1 frase |
| **6–10 pontos críticos** (Instagram · Google e internet) | Como vai funcionar: 4 partes em 40 min |
| O que já funciona (1 elogio com número) | O que vai ver ao vivo (cadeado) · prova · preparo ("vai ser uma verdadeira aula") · próximo passo |

**Na página 2 não entra:** data e hora da reunião (a equipe não sabe quando o pocket é gerado) nem case de cliente. **Datas só com mês e ano** ("setembro de 2026"), nunca o dia.

Arquivos: molde `assets/modelo-relatorio-pocket.html` (folha fixa 900×1800 px, instruções `IA:` em comentário) · rubrica `references/score-presenca.md` · coleta `references/coleta-instagram.md` e `references/coleta-google.md` · render `scripts/render.py` · exemplo pronto em `exemplo/`.

## Pipeline · 6 fases (~25 min)

### Fase 1 · Identificação
Pasta `clientes/Prospecções/<slug>/` com `auditorias/` e `pre-call/`. O slug é o handle sem `@`, `_` e `.`. O scraping usa o handle original.

### Fase 2 · Instagram → `references/coleta-instagram.md`
Apify (perfil + 15 posts), contas (frequência sem os fixados, % vídeo, engajamento, chamadas pra consulta, palavras-chave, destino do link), foto + 9 primeiros do grid baixados, print sem login pra ver destaques e stories.

**Depois, invoque a skill `ig-profile`** com esses dados. Ela devolve:
- a nota de 12 itens (0–100);
- o **nome** recomendado (≤30 caracteres, termo buscado + cidade);
- a **bio** reescrita (≤150, na voz do médico, com **CRM e RQE completos**);
- o **rótulo do link**, **5 destaques** com nome de pergunta, **3 fixados** (história · como funciona o tratamento-bandeira · prova com número real);
- o re-score honesto.

Passe as reescritas no `ig-human`, como a `ig-profile` manda. Salve tudo em `auditorias/ig-profile.md`. O celular "Reposicionado" da página 1 é **cópia literal** dessa saída.

### Fase 3 · Google e internet → `references/coleta-google.md`
Apify Google Places com 5 buscas, incluindo o **nome completo do registro**: a ficha pode estar com outro sobrenome. Mede GMB (nome, categoria, site, nota, avaliações), busca pelo nome, top 10 em 3 buscas e site próprio.

### Fase 4 · Score → `references/score-presenca.md`
9 itens, 4 grupos. Perfil = nota `ig-profile` × 0,2. Salve `auditorias/score.json` com a evidência de cada item. **A cor é sempre vermelha; o número nunca é maquiado.** Acima de 60, avise o gestor antes de enviar.

### Fase 5 · Montar o HTML
Copie o molde para `pre-call/relatorio-pocket.html`. Preencha todo `{{PLACEHOLDER}}` e todo token de imagem (`__FOTO_B64__`, `__THUMB_n__`, `__FIXADO_n__`). Siga cada comentário `IA:`. **Não mexa no CSS.**
Pontos críticos: o padrão são 8, sempre em número par. Card de item que está bom **sai** e entra outro problema real (ex.: "Alcance travado", "Chamada pra consulta", "Busca pelo seu nome", "RQE cortado").

### Fase 6 · Render + pré-flight
```bash
python -X utf8 <pasta-da-skill>/scripts/render.py "clientes/Prospecções/<slug>/pre-call/relatorio-pocket.html"
```
Gera `relatorio-pocket.pdf` (2 páginas), `pocket-pagina-1.png` e `pocket-pagina-2.png`. Reprova se o PDF não tiver 2 páginas, se algo estourar a folha ou se sobrar placeholder. Precisa de Chrome ou Edge.
Depois **abra os 2 PNGs e olhe**: palavra estourando capa de fixado, bio empurrando o grid, título quebrando feio, aspas retas. Estourou? **Corte texto.** Nunca aumente a folha.

**Entrega ao SDR:** o PDF (ou os 2 PNGs, que aparecem direto na conversa) + esta mensagem:
> "Doutor(a), como combinado, fiz um pré-diagnóstico do seu Instagram e do seu Google. Te mando uma prévia pra você já chegar sabendo do que a gente vai falar. Na reunião os sócios aprofundam tudo."

Reporte: caminho dos arquivos + score + os 3 pontos críticos mais fortes.

## Regras de copy

- Headline da página 1 = posicionamento com fato real e específico ("No Instagram, você é a médica da menopausa. No Google, ainda é “Rafaela Morais, mastologista”."). Nunca genérico. Aspas curvas.
- 1 elogio verdadeiro com número. Diagnóstico 100% pancada perde o médico.
- Alertas: evidência em 1 linha (≤42 caracteres) + o número que dói à direita.
- Sem cara de IA: nada de "jornada", "melhor versão", tríades em série. Frases curtas, voz de quem fala.
- Card sem evidência não entra. Automação: "nenhum comentário vira conversa sozinho", baseado nas legendas.
- CFM: o "depois" não anuncia especialidade sem RQE. Na dúvida, use a área de atuação ("Menopausa"), não o título ("Ginecologista").

## Anti-padrões

| ❌ | ✅ |
|---|---|
| Bio do "depois" improvisada | Saída literal da `ig-profile` |
| Dado velho de auditoria anterior | Scraping do dia. O perfil muda (caso Rafaela: jun → set/2026, mudou quase tudo) |
| Procurar a ficha só pelo nome do Instagram | Buscar também pelo nome completo do registro |
| Data e hora da reunião, dia do diagnóstico | Só mês e ano |
| Case de cliente na página 2 | Números oficiais Black Sales + o método |
| Score inflado ou rebaixado | Rubrica. Cor vermelha, número real |
| "Depois" com números inventados | Mesmos posts, seguidores e seguindo nos dois celulares |
| Nome de concorrente no pocket | "Quem está ocupando as suas buscas" fica no cadeado |
| Foto ou capa por URL do CDN | Base64 embutido |
| `-->` dentro de comentário HTML | Quebra o comentário e vaza texto na página |
| Aumentar a folha quando estoura | Cortar texto |
| Mandar sem olhar os PNGs | Pré-flight visual obrigatório |
| Rodar o pipeline inteiro da plano-de-acao | Pocket = coleta enxuta + ig-profile + score + 1 HTML |

## Defaults (não pergunte)

| | |
|---|---|
| Pontos críticos | 8 (4 Instagram + 4 Google), par, entre 6 e 10 |
| Buscas do top 10 | 3 (+ 2 buscas de nome pra achar a ficha) |
| Posts analisados | 15 (12 cronológicos + fixados) |
| Reunião | 40 min, Google Meet, Ygor Lopes + Sodré Monteiro |
| Gancho do cadeado | O mês seguinte (Outubro Rosa, Novembro Azul, Black Friday…) casado com a especialidade |
| Deploy | Não. Arquivos locais |
