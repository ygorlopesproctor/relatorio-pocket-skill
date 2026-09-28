# Coleta · Instagram

Mesma base da Fase 2 da skill `plano-de-acao`, enxugada pro pocket. Tudo cai em `clientes/Prospecções/<slug>/auditorias/`.

## Token Apify

Use a variável de ambiente `APIFY_TOKEN`. **Nunca** escreva o token em arquivo, commit ou mensagem. Sem token? Peça ao Ygor.

```powershell
$env:APIFY_TOKEN = '<token>'   # só na sessão
```

Se a resposta vier `Monthly usage hard limit exceeded` (ou vazia, 3 bytes), troque pro token reserva e rode de novo. Se os dois falharem, **pare e peça um token novo**. Nunca invente seguidor, curtida ou engajamento.

## 1 · Perfil + posts (Apify, em paralelo)

```powershell
$h = '<handle_sem_arroba>'   # o handle ORIGINAL, com _ e .
$out = "clientes\Prospecções\<slug>\auditorias"
$pb = @{ usernames=@($h); resultsType='details'; resultsLimit=1; addParentData=$false } | ConvertTo-Json -Depth 4
$qb = @{ username=@($h); resultsLimit=15 } | ConvertTo-Json -Depth 4
$j1 = Start-Job { param($b,$t,$o) $r=Invoke-WebRequest -Uri "https://api.apify.com/v2/acts/apify~instagram-profile-scraper/run-sync-get-dataset-items?token=$t&memory=512&timeout=300" -Method POST -Headers @{'Content-Type'='application/json'} -Body $b -UseBasicParsing; [IO.File]::WriteAllText($o,$r.Content,[Text.UTF8Encoding]::new($false)) } -ArgumentList $pb,$env:APIFY_TOKEN,"$out\instagram-profile.json"
$j2 = Start-Job { param($b,$t,$o) $r=Invoke-WebRequest -Uri "https://api.apify.com/v2/acts/apify~instagram-post-scraper/run-sync-get-dataset-items?token=$t&memory=1024&timeout=600" -Method POST -Headers @{'Content-Type'='application/json'} -Body $b -UseBasicParsing; [IO.File]::WriteAllText($o,$r.Content,[Text.UTF8Encoding]::new($false)) } -ArgumentList $qb,$env:APIFY_TOKEN,"$out\instagram-posts.json"
Wait-Job $j1,$j2 -Timeout 600 | Out-Null; Remove-Job $j1,$j2 -Force
```
Custo: centavos de dólar. Tempo: ~2 min.

**Do perfil:** `fullName` (é o campo "nome" que a busca lê), `biography` (literal, com quebras e emojis), `externalUrl`, `followersCount`, `followsCount`, `postsCount`, `businessCategoryName`, `profilePicUrlHD`.
**Dos posts:** `isPinned`, `type` (Video/Sidecar/Image), `timestamp`, `likesCount`, `commentsCount`, `videoPlayCount` (reproduções, o número que o Instagram mostra), `caption`, `displayUrl`.

## 2 · Contas

- **Frequência:** só os posts **não fixados** (os fixados têm data antiga). Posts ÷ semanas da janela; dias desde o último post.
- **Formato:** % de vídeos entre os 12 cronológicos.
- **Engajamento:** média de (curtidas + comentários) ÷ seguidores dos 12 cronológicos.
- **Chamada pra consulta:** quantas legendas pedem agendamento ou consulta.
- **Automação:** quantas legendas pedem palavra-chave ("comente X", "comenta", "digite", "manda X no direct").
- **Destino do link:** siga o redirecionamento (`curl -s -o NUL -w "%{redirect_url}" <link>`). WhatsApp direto, agregador ou encurtador não guardam contato.
- **Melhor post:** o de maior engajamento (história pessoal costuma ganhar), mais o reel clínico com mais reproduções.

## 3 · Imagens (base64 no HTML, nunca URL do CDN)

Baixe a foto e os **9 primeiros do grid na ordem real**: fixados primeiro, depois os cronológicos do mais novo pro mais velho. Monte uma folha 3×3 pra pontuar a legibilidade das capas (item da `ig-profile`).

```python
import json, urllib.request
from PIL import Image
posts = json.load(open('instagram-posts.json', encoding='utf-8'))
grid = sorted([p for p in posts if p.get('isPinned')], key=lambda p: p['timestamp'], reverse=True) \
     + sorted([p for p in posts if not p.get('isPinned')], key=lambda p: p['timestamp'], reverse=True)
for i, p in enumerate(grid[:9], 1):
    req = urllib.request.Request(p['displayUrl'], headers={'User-Agent': 'Mozilla/5.0'})
    open(f'grid/{i:02d}-{p["type"]}.jpg', 'wb').write(urllib.request.urlopen(req, timeout=30).read())
```

## 4 · Destaques e stories (o scraping não traz)

Tire um print do perfil sem login com o Chrome headless. Aparece um modal de login, mas a fileira de destaques e o anel de story ficam visíveis por trás:

```bash
chrome --headless=new --window-size=430,1400 --virtual-time-budget=12000 \
  --user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Version/17.0 Mobile/15E148 Safari/604.1" \
  --screenshot=auditorias/perfil-sem-login.png https://www.instagram.com/<handle>/
```

Se não der pra ver, peça ao SDR um print do topo do perfil no celular. É a entrada que a `ig-profile` pede. **Nunca invente nome de destaque.**

## Fallback sem Apify

O endpoint público `i.instagram.com/api/v1/users/web_profile_info/?username=<handle>` (header `x-ig-app-id: 936619743392459`) funcionou em jun/2026 e devolveu **401 em 28/09/2026**. Tente uma vez. Se falhar, use o print do SDR e declare a fonte no JSON.

## Saída

`auditorias/instagram-analise.json` com fonte, data, os números acima e o texto literal de nome, bio e link.
