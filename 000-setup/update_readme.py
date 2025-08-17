import os, re, pathlib, datetime, subprocess
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

TOPIC_MAP = {
    "01-arrays_hashing": ("📦 Arrays & Hashing", 9),
    "02-two_pointers": ("🔄 Two Pointers", 5),
    "03-sliding_window": ("🪟 Sliding Window", 6),
    "04-stack": ("📚 Stack", 7),
    "05-binary_search": ("🔍 Binary Search", 7),
    "06-linked_list": ("🔗 Linked List", 11),
    "07-trees": ("🌳 Trees", 15),
    "08-heap": ("⏫ Heap / Priority Queue", 7),
    "09-backtracking": ("🔙 Backtracking", 9),
    "10-tries": ("📖 Tries", 3),
    "11-graphs": ("🗺️ Graphs", 13),
    "12-advanced-graphs": ("⚡ Advanced Graphs", 6),
    "13-dp_1d": ("🧮 DP 1D", 12),
    "14-dp_2d": ("📊 DP 2D", 11),
    "15-greedy": ("💡 Greedy", 8),
    "16-intervals": ("⏱️ Intervals", 6),
    "17-math_geometry": ("📐 Math & Geometry", 8),
    "18-bit_manipulation": ("💾 Bit Manipulation", 7),
}

DIFF_RE = re.compile(r"Difficulty:\s*(Easy|Medium|Hard)", re.I)

DIFF_EMOJI = {
    "Easy": "🟢 Easy",
    "Medium": "🟡 Medium",
    "Hard": "🔴 Hard",
}

def detect_language(p: pathlib.Path) -> str:
    return {
        ".py": "Python", ".cpp": "C++", ".java": "Java",
        ".js": "JavaScript", ".ts": "TypeScript", ".go": "Go", ".rs": "Rust",
    }.get(p.suffix.lower(), p.suffix.lstrip("."))

def parse_id_name(stem: str):
    m = re.match(r"LC(\d{3})-([a-z0-9-]+)", stem, re.I)
    if not m: return None, None
    return m.group(1), m.group(2).replace("-", " ").title()

def extract_difficulty(p: pathlib.Path) -> str:
    try:
        m = DIFF_RE.search(p.read_text(encoding="utf-8", errors="ignore"))
        return m.group(1).title() if m else ""
    except Exception:
        return ""

def last_git_date(p: pathlib.Path) -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(ROOT), "log", "-1", "--format=%cs", "--", str(p)],
            stderr=subprocess.DEVNULL,
        ).decode().strip()
        if out: return out
    except Exception:
        pass
    return datetime.date.fromtimestamp(p.stat().st_mtime).isoformat()

def build_rows():
    rows = []
    for td, (topic_name, total_count) in TOPIC_MAP.items():
        tdir = ROOT / td
        if not tdir.exists(): continue
        for p in sorted(tdir.iterdir()):
            if not (p.is_file() and p.name.startswith("LC")): continue
            pid, pname = parse_id_name(p.stem)
            if not pid: continue
            diff = extract_difficulty(p)
            rows.append({
                "topic_key": td,
                "pid": int(pid),
                "pid_str": pid,
                "pname": pname,
                "topic_name": topic_name,
                "total_count": total_count,
                "diff": diff,
                "lang": detect_language(p),
                "path": p,
                "date": last_git_date(p),
            })
    return sorted(rows, key=lambda r: (list(TOPIC_MAP).index(r["topic_key"]), r["pid"]))

def render_grouped_table(rows):
    total_solved = len(rows)
    total_target = sum(v[1] for v in TOPIC_MAP.values())
    progress_bar_len = 20
    filled_len = int(progress_bar_len * total_solved / total_target)
    progress_bar = "█" * filled_len + "░" * (progress_bar_len - filled_len)

    out = []
    out.append(f"**Total Solved:** {total_solved} / {total_target} ✅")
    out.append(f"**Progress:** {progress_bar} {int((total_solved/total_target)*100)}%")
    out.append("\n---\n")

    # group by topic
    grouped = defaultdict(list)
    for r in rows:
        grouped[r["topic_key"]].append(r)

    for topic_key, (topic_name, total_count) in TOPIC_MAP.items():
        solved = grouped.get(topic_key, [])
        if not solved:
            continue  

        # 🔥 sort rows by date (latest first)
        solved.sort(key=lambda r: r["date"], reverse=False)

        out.append(f"## {topic_name} ({len(solved)}/{total_count})")
        out.append("| # | Problem | Difficulty | Language | Date | File |")
        out.append("|---|---------|------------|----------|------|------|")
        for r in solved:
            diff_disp = DIFF_EMOJI.get(r["diff"], r["diff"])
            link = f"[link]({r['path'].relative_to(ROOT).as_posix()})"
            out.append(f"| {r['pid_str']} | {r['pname']} | {diff_disp} | {r['lang']} | {r['date']} | {link} |")
        out.append("")  # blank line after each table

    return "\n".join(out)



def rewrite_readme(rows):
    table = render_grouped_table(rows)
    if not README.exists():
        README.write_text("# NeetCode 150 — Daily Solutions\n\n", encoding="utf-8")

    content = README.read_text(encoding="utf-8")
    start_tag = "<!-- AUTOGEN:START -->"
    end_tag   = "<!-- AUTOGEN:END -->"

    if start_tag in content and end_tag in content:
        before, rest = content.split(start_tag, 1)
        _, after = rest.split(end_tag, 1)
        new_content = before + start_tag + "\n" + table + "\n" + end_tag + after
    else:
        new_content = content.rstrip() + "\n\n" + start_tag + "\n" + table + "\n" + end_tag + "\n"

    README.write_text(new_content, encoding="utf-8")

if __name__ == "__main__":
    rows = build_rows()
    rewrite_readme(rows)
    print(f"Updated README with {len(rows)} solutions on {datetime.date.today()}")
