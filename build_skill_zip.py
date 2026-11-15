"""Build dist/jdmfsm-skill.zip, the SKILL.md pack for skill stores (Agensi and the like).

The zip holds one folder, jdmfsm/, named like the skill's `name`, with SKILL.md and references/.
Run: python build_skill_zip.py
"""
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent
SKILL = ROOT / "plugins" / "jdmfsm" / "skills" / "jdmfsm"
OUT = ROOT / "dist" / "jdmfsm-skill.zip"

OUT.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted(SKILL.rglob("*")):
        if p.is_file():
            arc = (pathlib.Path(SKILL.name) / p.relative_to(SKILL)).as_posix()
            z.write(p, arc)
            print(arc)
print(f"-> {OUT} ({OUT.stat().st_size:,} bytes)")
