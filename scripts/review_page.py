#!/usr/bin/env python3
"""Build a self-contained review page from a round of proposals.

The page shows each proposal (location, original, proposed, reason), an approve
checkbox, a comment box, optional variants, and local persistence. It exports
decisions as JSON with one button, so the person reviewing can return a single
file instead of transcribing answers.

Usage:
    review_page.py round.json -o round.html [--title "..."] [--note "..."]

round.json:
{
  "round": "sec5_r1",
  "title": "Section 5 polish, round 1",
  "note": "Ticked = apply exactly this text. Commented = do not apply; redraft.",
  "items": [
    {"id": "S5-01", "where": "5.2 P1, sentence 3",
     "original": "...", "proposed": "...", "reason": "topic sentence did not cover the second point",
     "variants": ["...", "..."],
     "kind": "edit"},
    {"id": "Q1", "where": "decision", "question": "Keep the literal counts?",
     "reason": "layout costs one line", "kind": "decision"}
  ]
}

`kind` is "edit" (original/proposed) or "decision" (a question with options).
No external assets, no network. Data stays in the browser until exported.
"""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
:root {{
  --bg: #ffffff; --fg: #16181d; --muted: #5b6270; --line: #d8dce4;
  --accent: #1f5fa8; --ok: #157347; --warn: #a15c00; --panel: #f6f8fb;
}}
@media (prefers-color-scheme: dark) {{
  :root {{ --bg:#131519; --fg:#e8eaee; --muted:#9aa3b2; --line:#2c313a;
           --accent:#79a9e0; --ok:#56c98b; --warn:#e0a552; --panel:#1a1d23; }}
}}
* {{ box-sizing: border-box; }}
body {{ margin:0; background:var(--bg); color:var(--fg);
  font: 15px/1.55 -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }}
header {{ position: sticky; top:0; z-index:5; background:var(--bg);
  border-bottom:1px solid var(--line); padding:14px 20px; }}
h1 {{ font-size:18px; margin:0 0 4px; }}
.sub {{ color:var(--muted); font-size:13px; }}
.bar {{ display:flex; gap:10px; flex-wrap:wrap; align-items:center; margin-top:10px; }}
button {{ font:inherit; padding:6px 12px; border-radius:8px; border:1px solid var(--line);
  background:var(--panel); color:var(--fg); cursor:pointer; }}
button.primary {{ border-color:var(--accent); color:var(--accent); font-weight:600; }}
button:hover {{ border-color:var(--accent); }}
main {{ max-width: 980px; margin: 0 auto; padding: 18px 20px 60px; }}
.card {{ border:1px solid var(--line); border-radius:12px; padding:14px 16px; margin:16px 0;
  background:var(--panel); }}
.card h2 {{ font-size:14px; margin:0 0 8px; letter-spacing:.02em; }}
.tag {{ display:inline-block; font-size:12px; color:var(--muted); border:1px solid var(--line);
  border-radius:999px; padding:1px 8px; margin-right:6px; }}
.block {{ margin:10px 0; }}
.block b {{ font-size:12px; letter-spacing:.04em; color:var(--muted); text-transform:uppercase; }}
.orig, .prop {{ white-space:pre-wrap; padding:10px 12px; border-radius:8px; margin-top:4px;
  border-left:3px solid var(--line); background:var(--bg); }}
.orig {{ color:var(--muted); }}
.prop {{ border-left-color: var(--accent); }}
del {{ background: rgba(200,40,40,.12); text-decoration: line-through; }}
ins {{ background: rgba(20,140,80,.14); text-decoration: none; }}
.reason {{ color:var(--muted); font-size:14px; }}
.controls {{ display:flex; gap:16px; align-items:center; flex-wrap:wrap; margin-top:12px;
  padding-top:10px; border-top:1px dashed var(--line); }}
label.approve {{ display:flex; gap:8px; align-items:center; font-weight:600; }}
textarea {{ width:100%; min-height:64px; font:inherit; padding:8px 10px; border-radius:8px;
  border:1px solid var(--line); background:var(--bg); color:var(--fg); margin-top:6px; }}
.state {{ font-size:12px; color:var(--muted); }}
.state.applied {{ color: var(--ok); }}
.state.commented {{ color: var(--warn); }}
.variant {{ margin-top:6px; }}
footer {{ color:var(--muted); font-size:12px; text-align:center; padding:20px; }}
</style></head><body>
<header>
  <h1>{title}</h1>
  <div class="sub">{note}</div>
  <div class="bar">
    <span class="state" id="count"></span>
    <button class="primary" id="export">Export decisions (JSON)</button>
    <button id="copy">Copy JSON</button>
    <button id="clear">Clear local state</button>
  </div>
</header>
<main id="items"></main>
<footer>Local page. Nothing is uploaded; decisions stay in this browser until exported.</footer>
<script>
const ROUND = {data};
const KEY = "review_page_" + JSON.stringify([location.pathname, ROUND]);
const store = (() => {{
  try {{ return Object.assign(Object.create(null), JSON.parse(localStorage.getItem(KEY) || "{{}}")); }} catch (e) {{ return Object.create(null); }}
}})();
function save() {{
  try {{ localStorage.setItem(KEY, JSON.stringify(store)); }} catch (e) {{}}
}}
function diff(a, b) {{
  const aw = a.split(/(\\s+)/), bw = b.split(/(\\s+)/);
  let i = 0; while (i < aw.length && i < bw.length && aw[i] === bw[i]) i++;
  let j = 0; while (j < aw.length - i && j < bw.length - i &&
                    aw[aw.length-1-j] === bw[bw.length-1-j]) j++;
  const mid = aw.slice(i, aw.length - j).join("");
  return esc(bw.slice(0, i).join("")) + "<del>" + esc(mid) + "</del><ins>" +
    esc(bw.slice(i, bw.length - j).join("")) + "</ins>" + esc(bw.slice(bw.length - j).join(""));
}}
function esc(s) {{ return s.replace(/[&<>]/g, c => ({{"&":"&amp;","<":"&lt;",">":"&gt;"}}[c])); }}
function render() {{
  const root = document.getElementById("items");
  root.innerHTML = "";
  ROUND.items.forEach((it, index) => {{
    const st = store[it.id] || {{}};
    const card = document.createElement("section");
    card.className = "card";
    let body = `<h2><span class="tag">${{esc(it.id)}}</span>${{esc(it.where || "")}}</h2>`;
    if (it.kind === "decision") {{
      body += `<div class="block"><b>Question</b><div class="prop">${{esc(it.question || "")}}</div></div>`;
    }} else {{
      body += `<div class="block"><b>Original</b><div class="orig">${{esc(it.original || "")}}</div></div>`;
      body += `<div class="block"><b>Proposed</b><div class="prop">${{diff(it.original || "", it.proposed || "")}}</div></div>`;
      body += `<div class="block"><b>Proposed, plain</b><div class="prop">${{esc(it.proposed || "")}}</div></div>`;
    }}
    if (it.reason) body += `<div class="block reason">${{esc(it.reason)}}</div>`;
    if (it.variants && it.variants.length) {{
      it.variants.forEach((v, k) => {{
        body += `<div class="block variant"><label><input type="radio" name="v_${{index}}" value="${{k}}"
          ${{String(st.variant) === String(k) ? "checked" : ""}}> Variant ${{k + 1}}</label>
          <div class="prop">${{esc(v)}}</div></div>`;
      }});
    }}
    body += `<div class="controls">
      <label class="approve"><input type="checkbox" id="a_${{index}}" ${{st.agree ? "checked" : ""}}>
        ${{it.kind === "decision" ? "Approve this decision" : "Apply exactly this text"}}</label>
      <span class="state ${{st.agree ? "applied" : (st.comment ? "commented" : "")}}"
        id="s_${{index}}">${{st.agree ? "approved" : (st.comment ? "commented" : "open")}}</span>
    </div>
    <textarea id="c_${{index}}" placeholder="Comment: do not apply; redraft from here">${{esc(st.comment || "")}}</textarea>`;
    card.innerHTML = body;
    root.appendChild(card);
    const box = card.querySelector("#a_" + index);
    const txt = card.querySelector("#c_" + index);
    const tag = card.querySelector("#s_" + index);
    box.disabled = Boolean(txt.value.trim());
    function sync() {{
      box.disabled = Boolean(txt.value.trim());
      if (box.disabled) box.checked = false;
      store[it.id] = {{ agree: box.checked, comment: txt.value.trim(),
                        variant: (card.querySelector('input[type=radio]:checked') || {{}}).value ?? null }};
      save();
      tag.textContent = box.checked ? "approved" : (txt.value.trim() ? "commented" : "open");
      tag.className = "state " + (box.checked ? "applied" : (txt.value.trim() ? "commented" : ""));
      count();
    }}
    box.addEventListener("change", sync);
    txt.addEventListener("input", sync);
    card.querySelectorAll('input[type=radio]').forEach(r => r.addEventListener("change", sync));
  }});
  count();
}}
function count() {{
  const total = ROUND.items.length;
  const done = ROUND.items.filter(i => (store[i.id] || {{}}).agree || (store[i.id] || {{}}).comment).length;
  document.getElementById("count").textContent = `${{done}} of ${{total}} decided`;
}}
document.getElementById("export").onclick = () => {{
  const payload = JSON.stringify({{ round: ROUND.round, title: ROUND.title, decisions: store }}, null, 1);
  const url = URL.createObjectURL(new Blob([payload], {{type: "application/json"}}));
  const a = document.createElement("a");
  a.href = url; a.download = ROUND.round + "_decisions.json"; a.click();
  URL.revokeObjectURL(url);
}};
document.getElementById("copy").onclick = async () => {{
  const payload = JSON.stringify({{ round: ROUND.round, decisions: store }});
  try {{ await navigator.clipboard.writeText(payload); alert("Copied."); }}
  catch (e) {{ alert("Copy failed; use Export."); }}
}};
document.getElementById("clear").onclick = () => {{
  if (confirm("Clear the decisions stored in this browser?")) {{
    try {{ localStorage.removeItem(KEY); }} catch (e) {{}}
    location.reload();
  }}
}};
render();
</script></body></html>
"""


def main() -> int:
    ap = argparse.ArgumentParser(description="Build a review page for a round of proposals.")
    ap.add_argument("round", help="JSON file with the round definition")
    ap.add_argument("-o", "--out", required=True, help="output .html path")
    ap.add_argument("--title", default=None)
    ap.add_argument("--note", default=None)
    a = ap.parse_args()
    data = json.loads(Path(a.round).read_text())
    data.setdefault("round", Path(a.round).stem)
    data.setdefault("items", [])
    ids = [item.get("id") if isinstance(item, dict) else None for item in data["items"]]
    if any(not isinstance(key, str) or not key.strip() for key in ids) or len(set(ids)) != len(ids):
        ap.error("each item needs a unique, nonempty string id")
    title = a.title or data.get("title") or f"Review round: {data['round']}"
    note = a.note or data.get("note") or \
        "Ticked = apply exactly this text. Commented = do not apply; redraft from the comment."
    html_out = PAGE.format(title=html.escape(title), note=html.escape(note),
                           data=json.dumps(data).replace("<", r"\u003c"))
    Path(a.out).write_text(html_out)
    print(f"wrote {a.out} ({len(data['items'])} items)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
