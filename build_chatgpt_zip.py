"""Build dist/jdmfsm-plugin.zip, the package uploaded to the ChatGPT app directory.

It is the contents of plugins/jdmfsm/ (the files at the zip root) without the Claude manifest,
which ChatGPT does not read. Run: python build_chatgpt_zip.py
"""
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent
PLUGIN = ROOT / "plugins" / "jdmfsm"
OUT = ROOT / "dist" / "jdmfsm-plugin.zip"
SKIP = {".claude-plugin"}

OUT.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted(PLUGIN.rglob("*")):
        rel = p.relative_to(PLUGIN)
        if p.is_file() and rel.parts[0] not in SKIP:
            z.write(p, rel.as_posix())
            print(rel.as_posix())
print(f"-> {OUT} ({OUT.stat().st_size:,} bytes)")
