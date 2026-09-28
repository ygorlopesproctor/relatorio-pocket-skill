# Score de Presença Digital · rubrica (0–100)

Nota única da página 1. Nove itens, quatro grupos (as barras do medidor). Pontue cada item pela evidência coletada, some e salve em `auditorias/score.json` com a evidência de cada linha.

**A cor do score é sempre vermelha. O número nunca é maquiado.** A rubrica já é dura de propósito, porque cobra conversão e Google, onde quase todo médico prospect zera. Se o total passar de 60, avise o gestor antes de enviar: o prospect está maduro e o ângulo da reunião muda para comercial/atendimento.

| Faixa | Selo no medidor |
|---|---|
| 0–39 | Zona crítica |
| 40–59 | Zona de risco |
| 60–100 | Abaixo do potencial |

## Perfil · 20 pts

Rode a rubrica da skill `ig-profile` (`~/.claude/skills/ig-profile/rubric.json`, 12 itens, 100 pts) sobre os dados do scraping e multiplique por 0,20 (arredonde). A mesma análise gera o "Reposicionado" da página 1: nome ≤30 caracteres, bio, rótulo do link, destaques e 3 fixados.

## Conteúdo · 20 pts

**Consistência de postagem (10).** Posts cronológicos por semana nos últimos 60 dias, sem contar os fixados.

| ≥4/sem e postou nos últimos 7 dias | 3/sem | 2/sem | 1/sem | <1/sem |
|---|---|---|---|---|
| 10 | 7 | 5 | 2 | 1 |

Teto de 1 se estiver parado há mais de 21 dias. Zero se estiver parado há mais de 60.

**Formato de conteúdo (10).** Participação de reels nos últimos 12 posts.

| Reels 40–70% + carrossel no mix | 100% reels | 25–39% | 10–24% | <10% | nenhum vídeo |
|---|---|---|---|---|---|
| 10 | 7 | 6 | 3 | 1 | 0 |

## Conversão · 20 pts

**Automação (10).** Procure CTA de palavra-chave nas legendas dos últimos 12 posts ("comente X", "comenta", "digite", "manda X no direct").

| ≥3 posts com CTA de palavra-chave | 1–2 posts | nenhum |
|---|---|---|
| 8 (10 se um teste no direct respondeu sozinho) | 4 | 0 |

No card, escreva o que foi observado ("nenhuma chamada de palavra-chave nos últimos 12 posts"), nunca "não tem automação" sem ter testado.

**Captação de pacientes (10).** Para onde o link da bio leva.

| LP, quiz ou formulário que guarda nome + WhatsApp | site próprio só com botão de WhatsApp | agregador (Linktree, bio.site) ou wa.me direto | sem link |
|---|---|---|---|
| 10 | 4 | 1 | 0 |

## Google · 40 pts

**Site próprio (10).** No ar, no celular, com página do tratamento-bandeira: 10. No ar, mas genérico: 5. Fora do ar ou quebrado: 1. Não existe: 0.

**Google Meu Negócio (10).** Perfil próprio, reivindicado e completo (fotos, horário, categoria certa, site): 10. Existe, mas incompleto ou não reivindicado: 4. Só aparece a ficha da clínica ou do prédio: 2. Não existe: 0.

**Avaliações no Google (10).**

| ≥100 | 50–99 | 20–49 | 5–19 | 1–4 | 0 |
|---|---|---|---|---|---|
| 10 | 7 | 5 | 3 | 1 | 0 |

Nota média abaixo de 4,5 tira 2 pontos (mínimo 0).

**Top 10 do Google (10).** Três buscas: `<especialidade> <cidade>`, `<tratamento-bandeira> <cidade>` e `<dor que a paciente digita> <cidade>`. Em cada uma, confira o top 10 do Maps (Apify `compass/crawler-google-places`, `maxCrawledPlacesPerSearch: 10`) e o top 10 orgânico. Conta como "aparece" se estiver em qualquer um dos dois.

| 3/3 | 2/3 | 1/3 | 0/3 |
|---|---|---|---|
| 10 | 6 | 3 | 0 |

## Barras do medidor

`--v` de cada barra = pontos do grupo ÷ máximo do grupo (Perfil ÷20 · Conteúdo ÷20 · Conversão ÷20 · Google ÷40).
Arco vermelho do medidor = `414.7 × score ÷ 100`.

## `auditorias/score.json`

```json
{
  "total": 11, "zona": "Zona crítica",
  "grupos": {"perfil": 8, "conteudo": 2, "conversao": 1, "google": 0},
  "itens": {
    "perfil":        {"pts": 8, "ig_profile": 42, "evidencia": "nome 'Médica', bio com 4 identidades, 0 destaques, nada fixado"},
    "consistencia":  {"pts": 1, "evidencia": "1,03 post/sem em 61 dias; 32 dias sem postar"},
    "formato":       {"pts": 1, "evidencia": "1 reel em 12 posts (8%)"},
    "automacao":     {"pts": 0, "evidencia": "nenhum CTA de palavra-chave nos últimos 12 posts"},
    "captacao":      {"pts": 1, "evidencia": "bio.site com WhatsApp fixo"},
    "site":          {"pts": 0, "evidencia": "sem domínio próprio"},
    "gmb":           {"pts": 0, "evidencia": "link de localização abre endereço cru"},
    "avaliacoes":    {"pts": 0, "evidencia": "0 avaliações"},
    "top10":         {"pts": 0, "evidencia": "0/3 buscas"}
  }
}
```
