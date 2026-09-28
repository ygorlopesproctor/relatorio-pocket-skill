"""Renderiza o relatório pocket: PDF de 2 páginas + 1 PNG por página + checagem de estouro.

Uso:  python -X utf8 render.py <caminho/relatorio-pocket.html>
Saída (mesma pasta do HTML): relatorio-pocket.pdf · pocket-pagina-1.png · pocket-pagina-2.png
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CANDIDATOS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome", "chromium", "chromium-browser",
]


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


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    html = Path(sys.argv[1]).resolve()
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

    # 1) estouro de folha (o script do molde marca data-overflow="1")
    dom = rodar(chrome, perfil, "--dump-dom", url).stdout
    dom = re.sub(r"<!--.*?-->", "", dom, flags=re.S)  # instruções <!-- IA: --> não contam
    estouros = re.findall(r'id="(p[12])"[^>]*data-overflow="1"|data-overflow="1"[^>]*id="(p[12])"', dom)
    tokens = sorted(set(re.findall(r"\{\{[^}]+\}\}|__[A-Z0-9_]+__|SEU_NUMERO_AQUI", dom)))

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
    if problemas:
        print("\n⚠ PRÉ-FLIGHT REPROVADO:")
        for p in problemas:
            print("  -", p)
        sys.exit(1)
    print("\n✓ Pré-flight técnico ok: 2 páginas, nada estourado, nenhum placeholder.")


if __name__ == "__main__":
    main()
