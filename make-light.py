from pathlib import Path

src = Path(__file__).parent / "index.html"
dst = Path(__file__).parent / "index-light.html"
text = src.read_text(encoding="utf-8")

start = text.index("<style>") + len("<style>")
end = text.index("</style>")
new_style = """
    :root {
      --bg: #ebebeb;
      --surface: #ffffff;
      --surface2: #ffffff;
      --border: #c5c5c5;
      --text: #1a1a1a;
      --heading: #000000;
      --muted: #5c5c5c;
      --accent: #3b82f6;
      --accent-dim: #2563eb;
      --ok: #22c55e;
      --warn: #f59e0b;
      --bad: #ef4444;
      --dash-ok: #e8f5e9;
      --dash-warn: #fff8e1;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: "Segoe UI", system-ui, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
      min-height: 100vh;
    }
    .wrap { max-width: 960px; margin: 0 auto; padding: 16px; }
    h1 { font-size: 1.35rem; margin-bottom: 4px; color: var(--heading); font-weight: 700; }
    .sub { color: var(--muted); font-size: 0.9rem; margin-bottom: 20px; }
    .theme-badge {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--muted);
      background: var(--surface);
      border: 1px solid var(--border);
      padding: 4px 10px;
      border-radius: 4px;
      margin-bottom: 12px;
    }
    .grid { display: grid; gap: 12px; }
    .grid-2 { grid-template-columns: 1fr 1fr; }
    .grid-4 { grid-template-columns: repeat(4, 1fr); }
    @media (max-width: 700px) {
      .grid-2, .grid-4 { grid-template-columns: 1fr; }
    }
    .card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 20px;
      margin-bottom: 16px;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.06);
    }
    .card h2 {
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--heading);
      font-weight: 700;
      margin-bottom: 12px;
    }
    label {
      display: block;
      font-size: 0.8rem;
      color: var(--heading);
      font-weight: 600;
      margin-bottom: 4px;
    }
    input, select, textarea {
      width: 100%;
      background: var(--surface2);
      border: 1px solid var(--border);
      border-radius: 4px;
      color: var(--text);
      padding: 10px 12px;
      font-size: 1rem;
    }
    input:focus, textarea:focus, select:focus {
      outline: 2px solid var(--accent);
      border-color: var(--accent);
    }
    textarea { min-height: 120px; resize: vertical; font-family: inherit; }
    .dash {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin-bottom: 16px;
    }
    @media (max-width: 600px) { .dash { grid-template-columns: 1fr 1fr; } }
    .dash-item {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 14px;
      text-align: center;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.06);
    }
    .dash-item .val {
      font-size: 1.5rem;
      font-weight: 700;
      margin-top: 4px;
    }
    .dash-item .sub-val {
      font-size: 0.72rem;
      color: var(--muted);
      margin-top: 6px;
      line-height: 1.35;
    }
    .dash-item .lbl { font-size: 0.75rem; color: var(--heading); font-weight: 600; text-transform: uppercase; }
    .dash-item.need .val { color: var(--accent); }
    .dash-item.collected .val { color: var(--ok); }
    .dash-item.left.deficit .val { color: var(--warn); }
    .dash-item.left.surplus .val { color: var(--ok); }
    .dash-item.left.exact .val { color: var(--ok); }
    .dash-item.debtors .val { color: var(--bad); }
    .btn-row { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }
    button {
      background: var(--heading);
      color: #fff;
      border: none;
      border-radius: 4px;
      padding: 10px 16px;
      font-size: 0.95rem;
      cursor: pointer;
      font-weight: 600;
    }
    button:hover { background: #333; }
    button.secondary {
      background: var(--surface);
      color: var(--heading);
      border: 1px solid var(--border);
    }
    button.secondary:hover { background: #f5f5f5; }
    button.danger { background: #b91c1c; }
    button.danger:hover { background: #991b1b; }
    table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
    th, td { padding: 8px 6px; border-bottom: 1px solid var(--border); text-align: left; }
    th { color: var(--heading); font-size: 0.75rem; font-weight: 700; text-transform: uppercase; }
    tr.unpaid td.name { color: var(--warn); }
    tr.paid td.name { color: var(--ok); }
    tr.empty { opacity: 0.35; }
    .chk { width: 20px; height: 20px; accent-color: var(--ok); cursor: pointer; }
    .amt { width: 90px; padding: 6px 8px; font-size: 0.9rem; }
    .cmt { width: 100%; min-width: 80px; padding: 6px 8px; font-size: 0.85rem; }
    .debtors-list {
      margin-top: 10px;
      padding: 10px 12px;
      background: var(--dash-warn);
      border: 1px solid #e8d9a8;
      border-radius: 4px;
      font-size: 0.9rem;
      color: var(--text);
    }
    .debtors-list.all-paid {
      background: var(--dash-ok);
      border-color: #a5d6a7;
    }
    .debtors-list .debtors-title { font-weight: 700; margin-right: 6px; color: var(--heading); }
    .debtors-summary {
      font-size: 0.95rem;
      margin-bottom: 12px;
      padding: 10px 12px;
      background: var(--surface);
      border-radius: 4px;
      border: 1px solid var(--border);
      border-left: 3px solid var(--warn);
    }
    .debtors-summary.all-paid { border-left-color: var(--ok); }
    .debtors-summary .count { font-weight: 700; color: var(--warn); }
    .debtors-summary.all-paid .count { color: var(--ok); }
    tr.add-row { opacity: 0.55; }
    tr.add-row input.name-inp::placeholder { color: var(--muted); font-style: italic; }
    .games-bar { display: flex; gap: 8px; flex-wrap: wrap; align-items: center; margin-bottom: 16px; }
    .games-bar select { max-width: 280px; }
    .calc-hint { font-size: 0.85rem; color: var(--muted); margin-top: 8px; line-height: 1.6; }
    .calc-hint strong { color: var(--heading); }
    .field-hint { font-size: 0.75rem; color: var(--muted); margin-top: 4px; font-weight: 400; }
    .table-wrap { overflow-x: auto; }
    .storage-note { font-size: 0.88rem; color: var(--muted); margin-bottom: 12px; line-height: 1.55; }
    .save-status { font-size: 0.8rem; color: var(--ok); margin-top: 10px; min-height: 1.2em; }
    td.due-cell { color: var(--muted); white-space: nowrap; }
"""

text = text[:start] + new_style + text[end:]
text = text.replace("<title>Учёт оплат за лёд</title>", "<title>Учёт оплат за лёд (светлая тема)</title>", 1)
text = text.replace(
    '<div class="wrap">\n    <h1>',
    '<div class="wrap">\n    <p class="theme-badge">Светлая тема — только для просмотра</p>\n    <h1>',
    1,
)
dst.write_text(text, encoding="utf-8")
print("Created", dst)
