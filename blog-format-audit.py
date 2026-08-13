#!/usr/bin/env python3
"""Audit all README.md for consistent blog-style format."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKIP = {".cursor", ".git", "node_modules"}

VISUAL = re.compile(r"^## 📊 Visual")
SUMMARY = re.compile(r"^## 🎯 (?:At a Glance|What You'll Master|Overview)")
NAV = re.compile(r"^## 🧭 Navigation")
THEORY = re.compile(r"^## 📐")
CODE = re.compile(r"^## (?:💻|🎯 Key|🎯 Core|📦 Core|🔧 Core|⚡ Core|🛠️)")
HIGHLIGHT = re.compile(r"\{: \.highlight \}")

issues: list[dict] = []


def section_indices(lines: list[str]) -> dict[str, int]:
    idx = {}
    for i, line in enumerate(lines):
        s = line.strip()
        if VISUAL.match(s):
            idx.setdefault("visual", i)
        if SUMMARY.match(s):
            idx.setdefault("summary", i)
        if NAV.match(s):
            idx.setdefault("nav", i)
        if THEORY.match(s):
            idx.setdefault("theory", i)
        if CODE.match(s):
            idx.setdefault("code", i)
    return idx


def has_nav_table(lines: list[str], start: int) -> bool:
    chunk = "\n".join(lines[start:start + 8])
    return bool(re.search(r"\| ⬅️ Previous.*\n\|[^\n]+\n\| \[", chunk, re.S))


def audit(path: Path) -> None:
    rel = str(path.relative_to(ROOT))
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    # Skip examples folder readme
    if "/examples/" in rel.replace("\\", "/"):
        return

    fm = text.startswith("---\n") and "layout:" in text[:400]
    if not fm and rel != "README.md":
        issues.append({"id": "FM", "file": rel, "msg": "Missing Jekyll frontmatter (layout: default)"})

    has_center = "<div align=\"center\">" in text[:2500]
    h1_in_center = False
    if has_center:
        m = re.search(r"<div align=\"center\">(.*?)</div>", text[:3000], re.S)
        if m and re.search(r"^#\s+", m.group(1), re.M):
            h1_in_center = True

    if not has_center and rel != "README.md":
        issues.append({"id": "HDR", "file": rel, "msg": "Missing centered header <div align=\"center\">"})

    if has_center and not h1_in_center and rel != "README.md":
        issues.append({"id": "HDR2", "file": rel, "msg": "H1 title not inside centered header div"})

    subtitle = bool(re.search(r"^### \*[^*]+\*", text[:2500], re.M))
    if not subtitle and rel != "README.md":
        issues.append({"id": "SUB", "file": rel, "msg": "Missing subtitle (### *...*) under title"})

    si = section_indices(lines)
    if "visual" not in si and rel != "README.md":
        if not re.search(r"^## 📊 Visual", text, re.M):
            if not re.search(r"!\[.*\]\(\./images/", text):
                issues.append({"id": "VIS", "file": rel, "msg": "Missing ## 📊 Visual Overview/Diagrams section"})

    if "summary" not in si and rel != "README.md":
        issues.append({"id": "SUM", "file": rel, "msg": "Missing summary section (At a Glance / What You'll Master / Overview)"})

    if not HIGHLIGHT.search(text) and rel != "README.md":
        issues.append({"id": "CAL", "file": rel, "msg": "Missing {: .highlight } callout block"})

    # Subtopics: parent in frontmatter -> expect navigation
    parent = re.search(r"^parent:\s*[\"']?([^\"'\n]+)", text, re.M)
    if parent and "nav" in si:
        if not has_nav_table(lines, si["nav"]):
            issues.append({"id": "NAV", "file": rel, "line": si["nav"] + 1, "msg": "Navigation section missing prev/next table"})
    elif parent and rel != "README.md" and not re.search(r"has_children:\s*true", text[:500]):
        issues.append({"id": "NAV2", "file": rel, "msg": "Subtopic missing ## 🧭 Navigation section"})

    # Canonical order: visual < summary < nav < theory < code (when all present)
    order = ["visual", "summary", "nav", "theory", "code"]
    present = [k for k in order if k in si]
    for a, b in zip(present, present[1:]):
        if si[a] > si[b]:
            issues.append({
                "id": "ORD",
                "file": rel,
                "line": si[b] + 1,
                "msg": f"Section order: {a} (line {si[a]+1}) should come before {b} (line {si[b]+1})",
            })

    # Visual before theory globally
    if "visual" in si and "theory" in si and si["visual"] > si["theory"]:
        issues.append({
            "id": "ORD2",
            "file": rel,
            "line": si["visual"] + 1,
            "msg": f"Visual section after theory (visual {si['visual']+1}, theory {si['theory']+1})",
        })


def main() -> None:
    files = sorted(
        p for p in ROOT.rglob("README.md")
        if not any(s in p.parts for s in SKIP)
    )
    for f in files:
        audit(f)

    by_type: dict[str, int] = {}
    for iss in issues:
        by_type[iss["id"]] = by_type.get(iss["id"], 0) + 1

    report = {"totalFiles": len(files), "issueCount": len(issues), "byType": by_type, "issues": issues}
    out = ROOT / "blog-format-audit.json"
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(json.dumps({"total": len(files), "issues": len(issues), "byType": by_type}, indent=2))
    for iss in issues[:50]:
        print(f"  [{iss['id']}] {iss['file']}: {iss['msg']}")
    if len(issues) > 50:
        print(f"  ... and {len(issues) - 50} more (see blog-format-audit.json)")


if __name__ == "__main__":
    main()
