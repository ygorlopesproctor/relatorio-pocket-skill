# ig-profile · @dra_rafaelaresende · 28/09/2026 (refeito com as regras do perfil médico em 05/10/2026)

Fonte: Apify (`instagram-profile-2026-09-28.json` + `instagram-posts-2026-09-28.json`), grid dos 9 primeiros em `grid-2026-09-28/`, visita sem login (`_perfil-headless.png`), ficha Google (`google-maps-2026-09-28.json`).

## Mapa de atuação (resumo do `mapa-atuacao.md`)

| Área | Tratamentos | Fonte | Vende? |
|---|---|---|---|
| Mama | mastologia, rastreio | bio ("Mastologista"), ficha Google, RQE 20112409 | consulta |
| Menopausa | reposição hormonal | nome atual, bio, 6 das 12 legendas | **sim** (bandeira) |
| Saúde íntima | rejuvenescimento íntimo estético e funcional | bio | **sim** |

Três áreas → nome com guarda-chuva: **Saúde da Mulher**. Endereço da ficha: Q. 401 Sul, Centro, Palmas - TO. Agendamento online: não tem (o link cai num WhatsApp fixo) → Linktree.

## PROFILE SCORE 56/100

| item | pts | por quê |
|---|---|---|
| nome (name field) | 9/12 | "Dra. Rafaela Resende \| Ginecologista e Menopausa": Dra. + nome ✓, termo buscado ✓, mas deixa mama e saúde íntima de fora (−3). "Ginecologista": confirmar RQE de GO (se não houver, −3 a mais) |
| bio, linha 1 | 4/12 | "De Madame para Madame 🍎": slogan forte e só dela, mas não diz pra quem é nem o que muda |
| bio, corpo | 3/8 | lista de títulos separados por barra + **RQE cortado ("RQE 2011"; o certo é 20112409)** + "Agende ⬇️" |
| 3 fixados | 5/10 | 3 fixados de 2025 (história 1.597 curtidas/125 comentários ✓, "lugar que entende", vulnerabilidade): 2 fazem o mesmo trabalho (apresentação) e **nenhum fala de menopausa**, o tratamento que ela mais posta |
| link | 6/8 | uma porta só, casando com "Agende" ✓; encurtador de terceiros (doctorcreator.short.gy) → WhatsApp fixo (63) 3322-5444, sem guardar contato |
| destaques | 0/8 | nenhum visível na visita sem login |
| legibilidade do grid | 6/8 | capas com texto, legíveis; reels com legenda no meio da frase |
| foto | 5/6 | rosto centralizado, fundo limpo |
| handle | 5/6 | dra_rafaelaresende, fácil de falar |
| categoria/contato | 3/6 | conta profissional, categoria genérica "Medical & health", sem endereço no perfil |
| atividade recente | 8/10 | 12 posts entre 07 e 24/09 (≈4,7/semana), último em 24/09 |
| stories | 2/6 | sem story ativo no momento da auditoria (não verificável sem login) |

## Reescritas (ordem: mais pontos perdidos primeiro)

**1. Nome (até 48 caracteres; o limite do Instagram é 64)** — recomendação: opção A
- A. `Dra. Rafaela Resende | Saúde da Mulher` (38)
- B. `Dra. Rafaela Resende | Mama e Menopausa` (39): deixa o íntimo de fora
- C. `Dra. Rafaela Resende | Mastologia e Hormônios` (45)
> Sem cidade no nome: Palmas vai no campo Endereço. Evitei "Ginecologista": o RQE confirmado é de Mastologia (CFM).

**2. Bio (≤150, contando quebras e emoji como 2)** — 149
```
De madame pra madame, sem sofrer calada 🍎
Mama, menopausa, hormônios e saúde íntima
Mastologista • CRM-TO 4575 • RQE 20112409
📅 Agende pelo link 👇
```

**3. Endereço (Editar perfil → Opções de contato → Endereço):** `Quadra 401 Sul, Centro · Palmas - TO` (da ficha Google)

**4. Link:** `linktr.ee/dra_rafaelaresende`, com 1º botão "Agendar consulta" (WhatsApp), 2º "Como chegar" (ficha Google) e 3º "Reposição hormonal"

**5. Os 3 fixados**
1. História: manter "Doutora das Madames" (1.597 curtidas, 125 comentários)
2. Como funciona: **post novo** "Menopausa: como eu cuido" (não existe ainda)
3. Prova: reel "O xixi pode avisar que a menopausa está chegando" (2.506 reproduções, o melhor clínico de setembro)

**6. Destaques (5), cobrindo as 3 áreas:** Consulta · Menopausa · Íntimo · Mama · Sobre mim

**7. Capas:** manter o padrão de texto; nos reels, escolher o quadro com a frase-chave em ≤4 palavras

Passado no `ig-human` (humanize.py): sem clichê detectado.

## Re-score honesto: ~83/100
Nome 12 · linha 1 10 · corpo 7 · fixados 8 · link 8 · destaques 7 · grid 6 · foto 5 · handle 5 · categoria 5 · atividade 8 · stories 2.
O que falta não é reescrita: criar o post "como eu cuido", produzir as capas dos destaques e o hábito diário de stories.
