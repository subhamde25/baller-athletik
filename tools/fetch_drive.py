"""Download files listed in raw/manifest.json from public Drive folders.
usage: fetch_drive.py <manifest> <out_dir> [--psd]"""
import sys, json, os, time, urllib.request, urllib.error
sys.stdout.reconfigure(encoding="utf-8")
from concurrent.futures import ThreadPoolExecutor
man, out = sys.argv[1], sys.argv[2]
want_psd = "--psd" in sys.argv
KEEP_PSD = {"Additional Assets/Task 18.psd", "Image Dump/BAT04303 SEL-Edit new.psd"}
def get(f):
    ext = os.path.splitext(f["path"])[1].lower()
    if ext == "" or (ext == ".psd" and not want_psd and f["path"] not in KEEP_PSD):
        return None
    # Windows rejects folder names with trailing spaces/dots (e.g. "Nikhil ")
    parts = [p.rstrip(" .") for p in f["path"].split("/")]
    # keep long AI-prompt filenames under Windows MAX_PATH
    stem, e = os.path.splitext(parts[-1])
    if len(stem) > 60: parts[-1] = stem[:60] + "_" + f["id"][:6] + e
    dst = os.path.join(out, *parts)
    if os.path.exists(dst) and os.path.getsize(dst) > 0: return f"skip {f['path']}"
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    u = f"https://drive.usercontent.google.com/download?id={f['id']}&export=download&confirm=t"
    try:
        for attempt in range(4):
            try:
                with urllib.request.urlopen(u, timeout=600) as r:
                    ct = r.headers.get("Content-Type", "")
                    data = r.read()
                break
            except urllib.error.HTTPError as he:
                if he.code < 500 or attempt == 3: raise
                time.sleep(5 * (attempt + 1))
        if "text/html" in ct:
            return f"FAIL(html) {f['path']}"
        open(dst, "wb").write(data)
        return f"ok {len(data)/1e6:7.1f}MB {f['path']}"
    except Exception as e:
        return f"FAIL({e}) {f['path']}"
files = json.load(open(man))
files.sort(key=lambda f: (not f["path"].startswith("Additional"), not f["path"].startswith("Video"), f["path"]))
with ThreadPoolExecutor(6) as ex:
    for r in ex.map(get, files):
        if r: print(r, flush=True)
print("DONE")
