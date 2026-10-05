"""Renderiza o relatório pocket: PDF de 2 páginas + 1 PNG por página + checagem automática.

Uso:  python -X utf8 render.py <caminho/relatorio-pocket.html>
Saída (mesma pasta do HTML): relatorio-pocket.pdf · pocket-pagina-1.png · pocket-pagina-2.png

A checagem reprova (exit 1): PDF ≠ 2 páginas, folha estourada, placeholder sobrando e as regras
do perfil médico lidas pelos atributos data-check do molde (nome com Dr./Dra., sem cidade, ≤64;
bio ≤150; link visível; endereço; números iguais nos 2 celulares; promessa da página 2 intacta;
aspas retas). Não substitui a Fase 7 (double check) do SKILL.md.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from html.parser import HTMLParser
from pathlib import Path

CANDIDATOS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome", "chromium", "chromium-browser",
]

# limites reais do Instagram (o campo Nome aceita 64; 30 é o limite do @)
NOME_MAX, NOME_UMA_LINHA, BIO_MAX = 64, 48, 150

# texto fixo da página 2 (Ygor, 05/10/2026). Mudou o molde? Mude aqui também.
PROMESSA = ["consultas particulares", "procedimentos e tratamentos", "estratégias de internet mais avançadas",
            "bom atendimento", "comercial que converte", "secretária treinada"]
OBJETIVO = ["plano de 90 dias", "internet, atendimento e comercial"]

CAMPOS = ["cidade", "registro", "nome-novo", "bio-nova", "endereco-novo", "link-novo",
          "stats-hoje", "stats-novo", "promessa", "objetivo"]
VAZIAS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
          "param", "source", "track", "wbr"}


def achar_chrome():
    for c in CANDIDATOS:
        if os.path.isfile(c) or shutil.which(c):
            return c
    sys.exit("Chrome/Edge não encontrado — instale o Chrome ou ajuste CANDIDATOS.")


def rodar(chrome, perfil, *args):
    base = [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            f"--user-data-dir={perfil}", "--virtual-time-budget=9000",
            "--window-size=900,1800"]
    return subprocess.run(base + list(args), capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=180)


class Coletor(HTMLParser):
    """Junta o texto de cada elemento com data-check (sem as bolinhas .mk) e todo o texto visível."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pilha = []      # (tag, data-check, fora_do_campo, invisivel)
        self.campos = {}     # data-check -> [texto de cada elemento]
        self.visivel = []

    def handle_starttag(self, tag, attrs):
        if tag in VAZIAS:
            return
        a = dict(attrs)
        classes = (a.get("class") or "").split()
        check = a.get("data-check")
        for _, aberto, _, _ in self.pilha:   # separa blocos internos ("395 posts 7.243 seguidores")
            if aberto:
                self.campos[aberto][-1] += " "
        self.pilha.append((tag, check, "mk" in classes, tag in ("script", "style", "title")))
        if check:
            self.campos.setdefault(check, []).append("")

    def handle_endtag(self, tag):
        for i in range(len(self.pilha) - 1, -1, -1):
            if self.pilha[i][0] == tag:
                del self.pilha[i:]
                return

    def handle_data(self, data):
        if any(p[3] for p in self.pilha):
            return
        self.visivel.append(data)
        if any(p[2] for p in self.pilha):
            return
        for _, check, _, _ in self.pilha:
            if check:
                self.campos[check][-1] += data


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


def tamanho(s):
    """Conta como o Instagram (UTF-16): emoji vale 2."""
    return len(s.encode("utf-16-le")) // 2


def checar_conteudo(dom):
    c = Coletor()
    c.feed(dom)
    campo = {k: [re.sub(r"[ \t]+", " ", t).strip() for t in v] for k, v in c.campos.items()}
    problemas, avisos = [], []

    faltando = [k for k in CAMPOS if k not in campo]
    if faltando:
        return ["molde antigo ou data-check apagado (" + ", ".join(faltando) +
                "): copie assets/modelo-relatorio-pocket.html de novo"], avisos

    nome = campo["nome-novo"][0]
    registro = campo["registro"][0]
    cidade = re.sub(r"[\s\-–/,]+[A-Za-z]{2}$", "", campo["cidade"][0]).strip()

    if "CRM" in registro.upper() and not re.match(r"(Dr|Dra)\. \S", nome):
        problemas.append(f'nome do depois sem "Dr."/"Dra." com ponto no começo: "{nome}"')
    if cidade and re.search(r"\b" + re.escape(sem_acento(cidade)) + r"\b", sem_acento(nome)):
        problemas.append(f'cidade no nome do depois ("{cidade}"): localização vai na linha de endereço')
    if tamanho(nome) > NOME_MAX:
        problemas.append(f"nome do depois com {tamanho(nome)} caracteres (o Instagram aceita {NOME_MAX})")
    elif tamanho(nome) > NOME_UMA_LINHA:
        avisos.append(f"nome do depois com {tamanho(nome)} caracteres: confira no PNG se coube em 1 linha")
    if "|" not in nome:
        avisos.append("nome do depois sem posicionamento depois do nome (formato: Dra. Nome | área)")

    linhas = [l.strip() for l in campo["bio-nova"][0].splitlines() if l.strip()]
    bio = "\n".join(linhas)
    if tamanho(bio) > BIO_MAX:
        problemas.append(f"bio do depois com {tamanho(bio)} caracteres (máximo {BIO_MAX}, contando as quebras)")
    if "CRM" in registro.upper() and "CRM" not in bio.upper():
        problemas.append("bio do depois sem o CRM")

    link = campo["link-novo"][0]
    if not re.fullmatch(r"(https?://)?[\w-]+(\.[\w-]+)+(/\S*)?", link):
        problemas.append(f'linha do link mostra "{link}": tem que ser o endereço do link (ex.: linktr.ee/handle)')

    endereco = campo["endereco-novo"][0]
    if len(endereco) < 5:
        problemas.append("linha de endereço (📍) do depois vazia: a localização vai ali")
    elif tamanho(endereco) > 42:
        avisos.append(f"endereço com {tamanho(endereco)} caracteres: deve quebrar em 2 linhas, encurte (bairro + cidade - UF)")

    hoje, novo = (re.sub(r"\s+", " ", campo[k][0]) for k in ("stats-hoje", "stats-novo"))
    if hoje != novo:
        problemas.append(f"números do perfil diferentes nos 2 celulares: hoje [{hoje}] × depois [{novo}]")

    promessa = sem_acento(" ".join(campo["promessa"]))
    if any(sem_acento(t) not in promessa for t in PROMESSA):
        problemas.append("promessa da página 2 (H1 + abertura) foi mexida: é texto fixo do molde")
    objetivo = sem_acento(" ".join(campo["objetivo"]))
    if any(sem_acento(t) not in objetivo for t in OBJETIVO):
        problemas.append("objetivo da página 2 foi mexido: é texto fixo do molde")

    if '"' in "".join(c.visivel):
        problemas.append('aspas retas (") no texto: use aspas curvas “assim”')
    return problemas, avisos


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    html = Path(sys.argv[1]).resolve()
    if not html.is_file():
        sys.exit(f"Arquivo não encontrado: {html}")
    pasta = html.parent
    url = html.as_uri()
    chrome = achar_chrome()
    pdf = pasta / "relatorio-pocket.pdf"
    pngs = [pasta / f"pocket-pagina-{n}.png" for n in (1, 2)]
    # apaga as saídas antigas: se um PDF/PNG velho estiver aberto num leitor, o Chrome
    # não consegue sobrescrever e o pré-flight aprovaria o arquivo antigo
    for f in [pdf, *pngs]:
        try:
            f.unlink(missing_ok=True)
        except PermissionError:
            sys.exit(f"{f.name} está aberto em outro programa. Feche e rode de novo.")
    perfil = tempfile.mkdtemp(prefix="pocket-chrome-")

    # 1) estouro de folha (o script do molde marca data-overflow="1") + conteúdo
    dom = rodar(chrome, perfil, "--dump-dom", url).stdout
    dom = re.sub(r"<!--.*?-->", "", dom, flags=re.S)  # instruções <!-- IA: --> não contam
    estouros = re.findall(r'id="(p[12])"[^>]*data-overflow="1"|data-overflow="1"[^>]*id="(p[12])"', dom)
    tokens = sorted(set(re.findall(r"\{\{[^}]+\}\}|__[A-Z0-9_]+__|SEU_NUMERO_AQUI", dom)))
    conteudo, avisos = checar_conteudo(dom)

    # 2) PDF
    rodar(chrome, perfil, "--no-pdf-header-footer", f"--print-to-pdf={pdf}", url)
    paginas = len(re.findall(rb"/Type\s*/Page(?!s)", pdf.read_bytes())) if pdf.exists() else 0

    # 3) PNG de cada página (2x, nítido no WhatsApp)
    for n, png in enumerate(pngs, 1):
        rodar(chrome, perfil, "--force-device-scale-factor=2", f"--screenshot={png}", f"{url}#p{n}")

    shutil.rmtree(perfil, ignore_errors=True)

    print(f"PDF: {pdf}  ({paginas} páginas)")
    for png in pngs:
        print(f"PNG: {png}")
    problemas = [f"{f.name} não foi gerado" for f in pngs if not f.exists()]
    if paginas != 2:
        problemas.append(f"PDF saiu com {paginas} páginas (tem que ser 2)")
    for a, b in estouros:
        problemas.append(f"conteúdo estourou a folha {a or b} — corte texto, não aumente a folha")
    if tokens:
        problemas.append("placeholder sem preencher: " + ", ".join(tokens[:12]))
    problemas += conteudo
    for a in avisos:
        print("  aviso:", a)
    if problemas:
        print("\n⚠ PRÉ-FLIGHT REPROVADO:")
        for p in problemas:
            print("  -", p)
        sys.exit(1)
    print("\n✓ Checagem automática ok. Agora a Fase 7: abra os 2 PNGs e faça o double check.")


if __name__ == "__main__":
    main()
