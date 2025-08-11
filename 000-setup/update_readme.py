import os, re, pathlib, datetime, subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

TOPIC_MAP = {
    "01-arrays_hashing": "Arrays & Hashing",
    "02-two_pointers": "Two Pointers",
    "03-sliding_window": "Sliding Window",
    "04-stack": "Stack",
    "05-binary_search": "Binary Search",
    "06-linked_list": "Linked List",
    "07-trees": "Trees",
    "08-heap": "Heap / Priority Queue",
    "09-backtracking": "Backtracking",
    "10-tries": "Tries",
    "11-graphs": "Graphs",
    "12-advanced-graphs": "Advanced Graphs",
    "13-dp_1d": "Dynamic Programming 1D",
    "14-dp_2d": "Dynamic Programming 2D",
    "15-greedy": "Greedy",
    "16-intervals": "Intervals",
    "17-math_geometry": "Math & Geometry",
    "18-bit_manipulation": "Bit Manipulation",
}

DIFF_RE = re.compile(r"Difficulty:\s*(Easy|Medium|Hard)", re.I)

def detect_language(path: pathlib.Path) -> str:
    return {
        ".py": "Python", ".cpp": "C++", ".java": "Java",
        ".js": "JavaScript", ".ts": "TypeScript", ".go": "Go", ".rs": "Rust",
    }.get(path.suffix.lower(), path.suffix.lstrip("."))

def parse_id_name(filename: str):
    m = re.match(r"LC(\d{3})-([a-z0-9-]+)", filename, re.I)
    if not m:
        return None, None
    return m.group(1), m.group(2).replace("-", " ").title()

def extract_difficulty(path: pathlib.Path) -> str:
    try:
        txt = path.read_text(encoding="utf-8", errors="ignore")
        m = DIFF_RE.search(txt)
        return m.group(1).title() if m else ""
    except Exception:
        return ""

def last_git_date(path: pathlib.Path) -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(ROOT), "log", "-1", "--format=%cs", "--", str(path)],
            stderr=subprocess.DEVNULL,
        ).decode().strip()
        if out:
            return out  # YYYY-MM-DD
    except Exception:
        pass
    return datetime.date.fromtimestamp(path.stat().st_mtime).isoformat()

def build_rows():
    rows = []
    for topic_dir in TOPIC_MAP:
        tdir = ROOT / topic_dir
        if not tdir.exists():
            continue
        for p in sorted(tdir.iterdir()):
            if p.is_file() and p.name.startswith("LC"):
                pid, pname = parse_id_name(p.stem)
                if not pid:
                    continue
                rows.append((
                    int(pid),
                    pid,
                    pname,
                    TOPIC_MAP[topic_dir],
                    extract_difficulty(p),
                    detect_language(p),
                    p,
                    last_git_date(p),
                ))
    rows.sort()
    return rows

def render_table(rows):
    header = (
        "\n\n| # | Problem | Topic | Difficulty | Language | Date | File |\n"
        "|---|---------|-------|------------|----------|------|------|\n"
    )
    lines = []
    for _, pid, pname, topic, diff, lang, path, date in rows:
        link = f"[link]({path.relative_to(ROOT).as_posix()})"
        lines.append(f"| {pid} | {pname} | {topic} | {diff} | {lang} | {date} | {link} |")
    return header + "\n".join(lines) + "\n"

def rewrite_readme(rows):
    table = render_table(rows)
    if not README.exists():
        README.write_text("# NeetCode 150 — Daily Solutions\n\n", encoding="utf-8")

    content = README.read_text(encoding="utf-8")
    start_tag = "<!-- AUTOGEN:START -->"
    end_tag = "<!-- AUTOGEN:END -->"

    if start_tag in content and end_tag in content:
        before = content.split(start_tag, 1)[0]
        after = content.split(end_tag, 1)[1]
        new_content = before + start_tag + table + end_tag + after
    else:
        # append markers if missing
        new_content = content.rstrip() + "\n\n" + start_tag + table + end_tag + "\n"

    README.write_text(new_content, encoding="utf-8")

if __name__ == "__main__":
    rows = build_rows()
    rewrite_readme(rows)
    print(f"Updated README with {len(rows)} solutions on {datetime.date.today()}")
