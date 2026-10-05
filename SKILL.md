---
name: relatorio-pocket
description: Use quando alguém da equipe Black Sales pedir "relatório pocket", "pré-diagnóstico", "diagnóstico pocket", "isca de diagnóstico", "relatório pro SDR mandar", "prévia pro médico antes da reunião", ou quando um SDR coletou o @ do Instagram de um médico prospect e precisa do material que vende a reunião com os sócios. NÃO usar para o deck completo da call — isso é a skill plano-de-acao.
---

# Relatório Pocket · Pré-diagnóstico de 2 páginas

> Transforma o @ de um médico prospect em um **pré-diagnóstico de DUAS páginas** (PDF + 2 PNGs) que o SDR manda no WhatsApp. **Página 1** alarma com prova: score vermelho, antes e depois do perfil, pontos críticos. **Página 2** vende a reunião com os sócios com a promessa fixa da Black Sales.

Formato definido pelo Ygor na reunião comercial de 24/09/2026, ajustado em 28/09 e calibrado em 05/10/2026 depois de relatórios ruins em campo (nome sem "Dra.", cidade no nome, médico reduzido a uma área só, link escondido).

**REQUIRED SUB-SKILL:** `ig-profile` (invocar pela Skill tool). A nota de Perfil e o antes e depois saem dela, **com as regras do perfil médico abaixo por cima**. Onde as duas divergirem, vale esta skill.

## As duas páginas

| Página 1 · O raio-x (preto + vermelho) | Página 2 · A reunião (branco + lime) |
|---|---|
| Headline = leitura do **posicionamento** (ativo real + o furo) | **Promessa fixa** (texto do molde, não reescreva): agenda cheia de consultas particulares e mais vendas do tratamento que ele vende, com internet + atendimento + comercial, secretária treinada |
| **Score 0–100** em medidor sempre vermelho + 4 barras | **Ingresso**: "com os sócios, ao vivo" · 40 min · Google Meet · Ygor + Sodré |
| **Antes × depois do perfil** em 2 celulares | Objetivo: plano de 90 dias nas 3 frentes |
| **6–10 pontos críticos** (Instagram · Google e internet) | Como vai funcionar: 4 partes em 40 min |
| O que já funciona (1 elogio com número) | O que vai ver ao vivo (cadeado) · prova · preparo ("vai ser uma verdadeira aula") · próximo passo |

**Na página 2 não entra:** data e hora da reunião (a equipe não sabe quando o pocket é gerado) nem case de cliente. **Datas só com mês e ano** ("setembro de 2026"), nunca o dia.

Arquivos: molde `assets/modelo-relatorio-pocket.html` (folha fixa 900×1800 px, instruções `IA:` em comentário) · rubrica `references/score-presenca.md` · coleta `references/coleta-instagram.md` e `references/coleta-google.md` · render + checagem `scripts/render.py` · exemplo pronto em `exemplo/`.

## O perfil reposicionado · regras do perfil médico

Valem pro celular "Reposicionado", pra reescrita da `ig-profile` e pras notas embaixo dos celulares.

**1. Nome = `Dr.`/`Dra.` + nome pelo qual a paciente conhece + `|` + posicionamento amplo.**
- Título **com ponto**, sempre, pra médico com CRM. O nome é o mesmo do perfil atual ou da ficha Google (nome e sobrenome). Profissional sem CRM segue o próprio conselho (quiropraxista nunca vira "Dr.").
- O limite do campo Nome do Instagram é **64 caracteres**. A `ig-profile` fala em 30, mas 30 é o limite do @. Os perfis coletados chegam a 64. Mire em **até 48** (cabe numa linha). Se não couber, encurte o posicionamento. Título e sobrenome ficam.

**2. Localização não vai no nome.** Cidade, bairro e UF vão no campo **Endereço** da conta comercial (Editar perfil → Opções de contato), que o Instagram mostra com 📍. O celular "Reposicionado" mostra essa linha com o endereço real (ficha Google, site ou bio), em até 40 caracteres ("Quadra 401 Sul, Centro · Palmas - TO"). Nome atual sem cidade **não é problema** e não vira nota.

**3. Posicionamento amplo cobre tudo o que ele faz.** Antes de escrever o nome, monte o mapa de atuação (Fase 2). Se o mapa tem **uma área só**, o nome usa essa área. Se tem **duas ou mais**, o nome usa um guarda-chuva que cubra todas. As áreas específicas vão na linha 2 da bio e nos destaques, e nenhuma área que dá receita fica de fora.

| O mapa mostra | Nome |
|---|---|
| só endometriose | `Dra. Nome Sobrenome \| Endometriose` |
| menopausa + reposição + mama + estética íntima | `Dra. Rafaela Resende \| Saúde da Mulher` (exemplo/) |
| nutrologia + emagrecimento + hormônio masculino | `Dr. Nome Sobrenome \| Emagrecimento e Hormônios` |

**4. Link explícito.** A linha do link do celular mostra o **endereço do link**, como o Instagram mostra (`linktr.ee/handle`, `doctoralia.com.br/...`), nunca só um rótulo. Destino: o agendamento online, se ele tiver (Doctoralia, sistema próprio, site com página de agendar). Se não tiver, Linktree com "Agendar consulta" no 1º botão, "Como chegar" no 2º e o tratamento-bandeira no 3º. A **última linha da bio chama pro link** ("📅 Agende pelo link abaixo").

**5. Bio (≤150 caracteres, contando as quebras), 4 linhas curtas (≤45 cada):** pra quem + o que muda (na voz dele) · as áreas do mapa · especialidade com RQE + CRM-UF nº + RQE nº completos · chamada pro link.

**CFM:** título de especialidade ("Ginecologista", "Mastologista") só com RQE dela. Sem RQE, use a área ("Saúde da Mulher", "Menopausa").

| ❌ Saiu em campo | Por quê |
|---|---|
| `Dra Rafaela \| Menopausa Palmas` | sem ponto, sem sobrenome, cidade no nome e uma área só (ela também faz mama e íntimo) |
| `Rafaela \| Reposição Hormonal` | tirou o "Dra." |
| Nota "Nome longo e sem a cidade" | cidade não é critério. Nome de 48 caracteres não corta |
| Linha de link "Agende sua consulta" | rótulo sem link. A paciente não vê pra onde vai |

## Pipeline · 7 fases (~30 min)

### Fase 1 · Identificação
Pasta `clientes/Prospecções/<slug>/` com `auditorias/` e `pre-call/`. O slug é o handle sem `@`, `_` e `.`. O scraping usa o handle original.

### Fase 2 · Instagram, mapa de atuação e `ig-profile` → `references/coleta-instagram.md`
Apify (perfil + 15 posts), contas (frequência sem os fixados, % vídeo, engajamento, chamadas pra consulta, palavras-chave, destino do link), foto + 9 primeiros do grid baixados, print sem login pra ver destaques e stories.

**Mapa de atuação** → `auditorias/mapa-atuacao.md`. Liste **toda** área e tratamento que ele oferece, com a fonte de cada um: bio, nomes dos destaques, legendas dos 15 posts, menu e páginas do site, categorias da ficha Google, Doctoralia/CatalogoMed. Marque os que ele vende (high-ticket). Registre também: título (Dr./Dra.) e nome que a paciente conhece, CRM e RQE completos (CFM ou CatalogoMed, porque a bio pode estar cortada) e endereço do consultório.

**Depois, invoque a skill `ig-profile`** com os dados, o mapa e a seção "O perfil reposicionado" acima colada no pedido. Ela devolve a nota de 12 itens, as reescritas (nome, bio, link, 5 destaques com nome de pergunta, 3 fixados: história · como funciona o tratamento-bandeira · prova com número real) e o re-score honesto. Ao pontuar, siga os ajustes de `references/score-presenca.md`.

Passe as reescritas no `ig-human`, como a `ig-profile` manda. Salve tudo em `auditorias/ig-profile.md`. O celular "Reposicionado" é **cópia literal** dessa saída.

### Fase 3 · Google e internet → `references/coleta-google.md`
Apify Google Places com 5 buscas, incluindo o **nome completo do registro**: a ficha pode estar com outro sobrenome. Mede GMB (nome, categoria, site, nota, avaliações, **endereço**), busca pelo nome, top 10 em 3 buscas e site próprio.

### Fase 4 · Score → `references/score-presenca.md`
9 itens, 4 grupos. Perfil = nota `ig-profile` × 0,2. Salve `auditorias/score.json` com a evidência de cada item. **A cor é sempre vermelha; o número nunca é maquiado.** Acima de 60, avise o gestor antes de enviar.

### Fase 5 · Montar o HTML
Copie o molde para `pre-call/relatorio-pocket.html`. Preencha todo `{{PLACEHOLDER}}` e todo token de imagem (`__FOTO_B64__`, `__THUMB_n__`, `__FIXADO_n__`). Siga cada comentário `IA:`. **Não mexa no CSS e não apague os atributos `data-check`** (a checagem do render lê por eles).
Pontos críticos: o padrão são 8, sempre em número par. Card de item que está bom **sai** e entra outro problema real (ex.: "Alcance travado", "Chamada pra consulta", "Busca pelo seu nome", "RQE cortado").
Página 2: a promessa (H1 + abertura) e o objetivo são texto fixo. Só preencha o nome e o(s) tratamento(s) que ele vende de verdade (do mapa, 1 ou 2).

### Fase 6 · Render + checagem automática
```bash
python -X utf8 <pasta-da-skill>/scripts/render.py "clientes/Prospecções/<slug>/pre-call/relatorio-pocket.html"
```
Gera `relatorio-pocket.pdf` (2 páginas), `pocket-pagina-1.png` e `pocket-pagina-2.png`. **Reprova** se: o PDF não tiver 2 páginas, algo estourar a folha, sobrar placeholder, o nome do depois não começar com "Dr."/"Dra." (médico), tiver a cidade no nome, passar de 64 caracteres, a bio passar de 150, a linha do link não for um endereço, faltar a linha de endereço, os números do perfil divergirem entre os celulares, a promessa da página 2 tiver sido mexida ou houver aspas retas. Precisa de Chrome ou Edge.
Reprovou? Corrija o HTML e rode de novo. Nunca aumente a folha: estourou, **corte texto**.

### Fase 7 · Double check (obrigatório antes de entregar)
O render pega o que é mecânico. O resto é julgamento, e quem montou não confere sozinho. Responda em `pre-call/double-check.md`, cada item com ✅ + a evidência (arquivo e trecho):

1. O nome tem "Dr."/"Dra." com ponto + o nome que a paciente conhece, igual ao perfil atual ou à ficha?
2. O posicionamento do nome cobre **todas** as áreas do `mapa-atuacao.md`? Alguma que dá receita ficou de fora?
3. Nenhuma localização no nome. O endereço do depois é o real da ficha, do site ou da bio?
4. A linha do link mostra o endereço do link e a última linha da bio chama pra ele?
5. CRM e RQE completos e conferidos. Nenhum título de especialidade sem RQE (nome, bio, notas)?
6. As notas do "Hoje" só apontam problema que existe e nenhuma reclama de falta de cidade?
7. Posts, seguidores e seguindo iguais ao scraping do dia, nos dois celulares?
8. Cada ponto crítico tem a evidência em `auditorias/` e o número certo? Nenhum card de item que está bom?
9. Score = soma da rubrica, zona e arco certos (414,7 × score ÷ 100)?
10. A promessa da página 2 está intacta e o tratamento citado é um que ele vende (do mapa)?
11. Sem nome de concorrente, sem data e hora de reunião, sem case de cliente, datas só com mês e ano?
12. Você **abriu os 2 PNGs e olhou**: nada cortado, bio sem empurrar o grid, capas legíveis, títulos sem quebra feia?

**Revisor independente:** se houver Agent tool, mande um subagente novo (sem o contexto da montagem) ler `auditorias/`, o HTML, os 2 PNGs e esta checklist, e responder aprovado ou reprovado item por item. Reprovou algum? Corrija, rode o render e revise de novo. Depois de 2 rodadas com reprovação, pare e leve ao gestor.

**Entrega ao SDR:** o PDF (ou os 2 PNGs, que aparecem direto na conversa) + esta mensagem:
> "Doutor(a), como combinado, fiz um pré-diagnóstico do seu Instagram e do seu Google. Te mando uma prévia pra você já chegar sabendo do que a gente vai falar. Na reunião os sócios aprofundam tudo."

Reporte: caminho dos arquivos + score + os 3 pontos críticos mais fortes + "double check: 12/12".

## Regras de copy

- Headline da página 1 = posicionamento com fato real e específico ("No Instagram, você é a médica da menopausa. No Google, ainda é “Rafaela Morais, mastologista”."). Nunca genérico. Aspas curvas.
- 1 elogio verdadeiro com número. Diagnóstico 100% pancada perde o médico.
- Alertas: evidência em 1 linha (≤42 caracteres) + o número que dói à direita.
- Sem cara de IA: nada de "jornada", "melhor versão", tríades em série. Frases curtas, voz de quem fala.
- Card sem evidência não entra. Automação: "nenhum comentário vira conversa sozinho", baseado nas legendas.

## Anti-padrões

| ❌ | ✅ |
|---|---|
| Bio do "depois" improvisada | Saída literal da `ig-profile` com as regras do perfil médico |
| Cortar "Dra." ou sobrenome pra caber em 30 | O limite do Nome é 64. Encurte o posicionamento |
| Cidade no nome | Campo Endereço (linha 📍) |
| Uma área só quando ele faz várias | Guarda-chuva que cubra o mapa de atuação |
| Rótulo no lugar do link | Endereço do link visível + bio chamando pra ele |
| Reescrever a promessa da página 2 | Texto fixo do molde, só nome e tratamento mudam |
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
| Entregar sem double check | Render aprovado + 12/12 + revisor independente |
| Rodar o pipeline inteiro da plano-de-acao | Pocket = coleta enxuta + ig-profile + score + 1 HTML |

## Defaults (não pergunte)

| | |
|---|---|
| Pontos críticos | 8 (4 Instagram + 4 Google), par, entre 6 e 10 |
| Buscas do top 10 | 3 (+ 2 buscas de nome pra achar a ficha) |
| Posts analisados | 15 (12 cronológicos + fixados) |
| Link do depois | Agendamento online se existir; senão `linktr.ee/<handle>` com "Agendar consulta" no 1º botão |
| Reunião | 40 min, Google Meet, Ygor Lopes + Sodré Monteiro |
| Gancho do cadeado | O mês seguinte (Outubro Rosa, Novembro Azul, Black Friday…) casado com a especialidade |
| Deploy | Não. Arquivos locais |
