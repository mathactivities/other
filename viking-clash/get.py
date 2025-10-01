import os
import urllib.request
from urllib.parse import urljoin

BASE_URL = "https://cdn-factory.marketjs.com/en/clash-of-vikings/"
OUTPUT_DIR = ""

# The missing resource paths from your error log
MISSING_FILES = [
    "media/audio/bgm.ogg",
    "media/audio/opening/kittyopening.ogg",
    "media/audio/play/static.ogg",
    "media/audio/opening/opening.ogg",
    "media/audio/game/start-battle-long.ogg",
    "media/audio/game/click.ogg",
    "media/audio/game/sone.ogg",
    "media/audio/game/stwo.ogg",
    "media/audio/game/sthree.ogg",
    "media/audio/game/arrow-shower-f.ogg",
    "media/audio/game/wosh-fireball-a.ogg",
    "media/audio/game/berserk.ogg",
    "media/audio/game/freez.ogg",
    "media/audio/game/explode.ogg",
    "media/audio/game/earthquake-fade.ogg",
    "media/audio/game/giant-sound.ogg",
    "media/audio/game/m-aikh.ogg",
    "media/audio/game/m-argh.ogg",
    "media/audio/game/thunder.ogg",
    "media/audio/game/m-ok.ogg",
    "media/audio/game/m-yach.ogg",
    "media/audio/game/mage.ogg",
    "media/audio/game/meleweapon.ogg",
    "media/graphics/favicon.ico",
    "favicon.ico"
]

def save_file(path):
    url = urljoin(BASE_URL, path)
    local_path = os.path.join(OUTPUT_DIR, path)

    try:
        # Try to download
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                os.makedirs(os.path.dirname(local_path), exist_ok=True)
                with open(local_path, "wb") as f:
                    f.write(response.read())
                print(f"[OK] {url} -> {local_path}")
            else:
                print(f"[FAIL] {url} ({response.status})")
    except Exception as e:
        print(f"[ERR] {url} ({e})")

if __name__ == "__main__":
    for file_path in MISSING_FILES:
        save_file(file_path)
