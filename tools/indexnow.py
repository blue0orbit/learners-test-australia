"""Submits the site's URLs to IndexNow (Bing, Yandex, Seznam, Naver, Yep share submissions).

    python tools/indexnow.py            # every URL in sitemap.xml
    python tools/indexnow.py URL [URL]  # only these

Run it after the changes are live on the site. The key file (<key>.txt at the site root) is written by build.py.
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from sitelib import BASE, INDEXNOW_KEY  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def main(urls: list[str]) -> int:
    if not urls:
        urls = re.findall(r"<loc>([^<]+)</loc>", (ROOT / "sitemap.xml").read_text(encoding="utf-8"))
    host = BASE.split("//")[1].rstrip("/")
    body = {"host": host, "key": INDEXNOW_KEY, "keyLocation": f"{BASE}{INDEXNOW_KEY}.txt", "urlList": urls}
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f"IndexNow: HTTP {r.status} for {len(urls)} URLs")
            return 0
    except urllib.error.HTTPError as e:
        print(f"IndexNow: HTTP {e.code} {e.read()[:200]!r}")
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
