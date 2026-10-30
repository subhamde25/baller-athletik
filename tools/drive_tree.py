"""List every file in public Google Drive folders (recursively) into a JSON manifest.

python -I tools/drive_tree.py tools/drive_manifest.json "<folder id>=<label>" ...

Uses Drive's public embedded folder view, so no API key or sign-in is needed. The Drive
connector can't list folders that were only shared by link; this can.
"""
import sys, json, re, html, urllib.request
from concurrent.futures import ThreadPoolExecutor

ENTRY = re.compile(r'id="entry-([^"]+)".*?href="([^"]+)".*?flip-entry-title">([^<]*)<', re.S)


def fetch(fid):
    u = f"https://drive.google.com/embeddedfolderview?id={fid}"
    return urllib.request.urlopen(u, timeout=60).read().decode("utf-8", "ignore")


out, pool = [], ThreadPoolExecutor(16)
queue = [tuple(a.split("=", 1)) for a in sys.argv[2:]]
while queue:  # breadth-first, one Drive request per folder
    batch, queue = queue, []
    for (fid, path), page in zip(batch, pool.map(lambda x: fetch(x[0]), batch)):
        for eid, href, name in ENTRY.findall(page):
            name = html.unescape(name)
            if "/folders/" in href:
                queue.append((eid, f"{path}/{name}"))
            else:
                out.append({"id": eid, "path": f"{path}/{name}"})
json.dump(out, open(sys.argv[1], "w"), indent=1)
print(len(out), "files")
