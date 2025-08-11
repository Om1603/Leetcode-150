import os, re, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
TABLE_START = "Auto-generates the table below from your files:"
README = ROOT / "README.md"

TOPIC_MAP = {
    "01-arrays_hashing": "Arrays & Hashing",
    "02-two_pointers": "Two Pointers",
    "03-sliding_window": "Slid`ing Window",
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


DIFF_HINTS = {
    # "001": "Easy",
}

def detect_language(path: pathlib.Path) -> str:
    ext = path.suffix.lower()
    return {
        ".py": "Python",
        ".cpp": "C++",
        ".java": "Java",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".go": "Go",
        ".rs": "Rust",
    }.get(ext, ext.lstrip("."))

def parse_id_name(filename: str):
    m = re.match(r"LC(\d{3})-([a-z0-9-]+)", filename, re.I)
    if not m:
        return None, None
    return m.group(1), m.group(2).replace("-", " ").title()

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
                diff = DIFF_HINTS.get(pid, "")
                lang = detect_language(p)
                rows.append((int(pid), pid, pname, TOPIC_MAP[topic_dir], diff, lang, p))
    rows.sort()
    return rows

def rewrite_readme(rows):
    with open(README, "r", encoding="utf-8") as f:
        content = f.read()

    head, sep, tail = content.partition(TABLE_START)
    if not sep:
        raise SystemExit("README anchor not found")

    table_header = (
        "\n\n| # | Problem | Topic | Difficulty | Language | File |\n"
        "|---|---------|-------|------------|----------|------|\n"
    )

    table_rows = []
    for _, pid, pname, topic, diff, lang, path in rows:
        link = f"[link]({path.relative_to(ROOT).as_posix()})"
        table_rows.append(f"| {pid} | {pname} | {topic} | {diff} | {lang} | {link} |")

    new_content = head + sep + table_header + "\n".join(table_rows) + "\n"
    with open(README, "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    rows = build_rows()
    rewrite_readme(rows)
    print(f"Updated README with {len(rows)} solutions on {datetime.date.today()}")