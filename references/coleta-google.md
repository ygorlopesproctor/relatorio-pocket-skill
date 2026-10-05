# Coleta · Google e internet

Mesma base da Fase 3 da skill `plano-de-acao` (auditoria Google: GMB, site e concorrência), enxugada pro pocket.

## 1 · Google Maps (Apify `compass/crawler-google-places`)

Uma chamada com 5 buscas:

```powershell
$body = @{
  searchStringsArray = @(
    '<nome do Instagram> <cidade> <UF>',         # ex: Dra Rafaela Resende Palmas TO
    '<nome completo do registro> <cidade>',      # do CFM/CatalogoMed: ex: Rafaela Morais Palmas
    '<especialidade> <cidade> <UF>',             # ex: mastologista Palmas TO
    '<tratamento-bandeira> <cidade> <UF>',       # ex: reposição hormonal Palmas TO
    '<dor/tema do posicionamento> <cidade> <UF>' # ex: ginecologista menopausa Palmas TO
  )
  maxCrawledPlacesPerSearch = 10
  language = 'pt-BR'                             # 'pt' não é aceito
  includeImages = $false; includeReviews = $false; scrapePlaceDetailPage = $false
} | ConvertTo-Json -Depth 4
$r = Invoke-WebRequest -Uri "https://api.apify.com/v2/acts/compass~crawler-google-places/run-sync-get-dataset-items?token=$env:APIFY_TOKEN&memory=2048&timeout=600" -Method POST -Headers @{'Content-Type'='application/json'} -Body ([Text.Encoding]::UTF8.GetBytes($body)) -UseBasicParsing -TimeoutSec 600
[IO.File]::WriteAllText("$out\google-maps.json", $r.Content, [Text.UTF8Encoding]::new($false))
```

Por resultado: `searchString`, posição na lista, `title`, `categoryName`, `totalScore`, `reviewsCount`, `website`, `address`, `phone`.

### ⚠️ A ficha pode estar com OUTRO nome

Caso real (Dra. Rafaela, set/2026): no Instagram ela é "Rafaela **Resende**", e a ficha do Google é "Dra. Rafaela **Morais** - Mastologista" (4,5★, 55 avaliações). A auditoria de junho procurou só pelo nome do Instagram e concluiu, errado, que a ficha não existia. Por isso a busca 2 usa o **nome completo do registro**. Confirme pelo endereço e pelo telefone (os mesmos da bio ou do WhatsApp). Nome diferente entre Instagram e Google já é ponto crítico: a paciente procura um nome e acha outro.

## 2 · O que medir

- **Endereço do consultório:** o `address` da ficha confirmada. Vai pra linha 📍 do celular "Reposicionado" (a localização sai do nome). Sem ficha, use o endereço do site ou da bio. Sem nenhum, use bairro + cidade da Doctoralia/CatalogoMed. Nunca invente rua.

- **GMB:** existe? Com que nome? Categoria específica ou genérica ("Médico")? Tem site? Nota e nº de avaliações.
- **Busca pelo nome:** a busca 1 (nome do Instagram) acha a ficha? Se não acha, vira card.
- **Top 10:** em cada uma das buscas 3, 4 e 5, ela está entre os 10 do Maps? Registre `X/3`. Se der tempo, confira também o orgânico com WebSearch.
- **Quem domina** cada busca: fica no JSON. **No relatório não entra nome de concorrente**, porque o nome é isca da reunião.

## 3 · Site próprio (regra da plano-de-acao §3c)

Procure em: link da bio, campo `website` da ficha, WebSearch "nome + cidade" e tentativa direta (`dr<nome>.com.br`, `dra<nome>.com.br`). Abra o que achar.
**Não é site próprio:** Linktree, bio.site, encurtador, WhatsApp, Doctoralia, diretório, domínio estacionado (ex.: página "Bem-vindo a HostGator"), domínio de outra pessoa com o mesmo nome.

## Saída

`auditorias/google-analise.json`:

```json
{
  "fonte": "Apify compass/crawler-google-places · <mês/ano>",
  "gmb": {"existe": true, "nome_na_ficha": "Dra. Rafaela Morais - Mastologista", "categoria": "Médico",
          "nota": 4.5, "avaliacoes": 55, "site": null, "acha_pelo_nome_do_instagram": false},
  "site": {"existe": false, "prova": "bio → encurtador → WhatsApp; ficha sem site; drarafaela.com.br = domínio estacionado"},
  "top10": {"mastologista Palmas TO": 3, "ginecologista menopausa Palmas TO": null, "reposição hormonal Palmas TO": null},
  "top10_resumo": "1/3",
  "quem_domina": {"...": "nomes só aqui, nunca no relatório"}
}
```
