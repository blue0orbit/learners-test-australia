"""Generate the site's raster images from the learner-plate mark and the bundled fonts.

Outputs (in assets/img):
  icon-512.png, icon-192.png, apple-touch-icon.png  - plate on ink, like the launcher icon
  favicon.ico (site root)                           - plate filling the square (reads at 16 px)
  og-image.png                                      - 1200 x 630 social card
  logo-plate.png                                    - transparent plate mark (used in JSON-LD)

Run from the site root:  python tools/make_images.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "img"
FONTS = ROOT / "assets" / "fonts"

INK = (0x12, 0x16, 0x1D)
BITUMEN = (0x0C, 0x0F, 0x14)
PAPER = (0xF3, 0xF4, 0xF6)
AMBER = (0xFF, 0xA4, 0x1B)
PLATE = (0xFF, 0xC7, 0x2C)
MUTED = (0xB8, 0xBF, 0xCA)

SS = 4  # supersampling factor


def plate(size: int, background=None) -> Image.Image:
    """Draw the plate mark on a 64-unit grid (same geometry as assets/img/logo.svg)."""
    s = size * SS / 64
    im = Image.new("RGBA", (size * SS, size * SS), background or (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([2 * s, 2 * s, 62 * s, 62 * s], radius=12 * s, fill=PLATE)
    d.rounded_rectangle([6 * s, 6 * s, 58 * s, 58 * s], radius=8.5 * s, outline=INK, width=round(3 * s))
    d.polygon([(20 * s, 15 * s), (29 * s, 15 * s), (29 * s, 40.5 * s), (44 * s, 40.5 * s),
               (44 * s, 49 * s), (20 * s, 49 * s)], fill=INK)
    return im.resize((size, size), Image.LANCZOS)


def app_icon(size: int) -> Image.Image:
    """Plate at about 60% of an ink square, matching the Play icon."""
    base = Image.new("RGBA", (size, size), INK + (255,))
    mark = plate(round(size * 0.62))
    off = (size - mark.width) // 2
    base.alpha_composite(mark, (off, off))
    return base.convert("RGB")


def font(name: str, px: int, weight: int) -> ImageFont.FreeTypeFont:
    f = ImageFont.truetype(str(FONTS / name), px)
    try:
        f.set_variation_by_axes([weight])
    except Exception:  # static fallback if FreeType lacks variation support
        pass
    return f


def og_image() -> Image.Image:
    w, h = 1200, 630
    im = Image.new("RGBA", (w * SS, h * SS), INK + (255,))
    d = ImageDraw.Draw(im)
    # Road-lane motif along the bottom: a dashed amber centre line.
    y = (h - 58) * SS
    for x in range(0, w * SS, 120 * SS):
        d.rounded_rectangle([x, y, x + 64 * SS, y + 8 * SS], radius=4 * SS, fill=AMBER + (90,))
    im = im.resize((w, h), Image.LANCZOS)
    mark = plate(250)
    im.alpha_composite(mark, (88, 150))
    d = ImageDraw.Draw(im)
    x0 = 390
    d.text((x0, 150), "Learners Test", font=font("overpass.ttf", 88, 800), fill=PAPER)
    d.text((x0, 245), "Australia", font=font("overpass.ttf", 88, 800), fill=AMBER)
    d.text((x0, 364), "Learner test practice for every state and territory", font=font("atkinson_hyperlegible_next.ttf", 32, 500), fill=PAPER)
    d.text((x0, 414), "Real test formats · Every answer explained · Android app",
           font=font("atkinson_hyperlegible_next.ttf", 28, 400), fill=MUTED)
    d.text((88, 488), "Independent study app. Not affiliated with any government agency.",
           font=font("atkinson_hyperlegible_next.ttf", 24, 400), fill=MUTED)
    return im.convert("RGB")


def main() -> None:
    IMG.mkdir(parents=True, exist_ok=True)
    app_icon(512).save(IMG / "icon-512.png", optimize=True)
    app_icon(192).save(IMG / "icon-192.png", optimize=True)
    app_icon(180).save(IMG / "apple-touch-icon.png", optimize=True)
    plate(512).save(IMG / "logo-plate.png", optimize=True)
    plate(64).save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    og_image().save(IMG / "og-image.png", optimize=True)
    for p in sorted(IMG.glob("*.png")) + [ROOT / "favicon.ico"]:
        print(f"{p.relative_to(ROOT)}  {p.stat().st_size:,} bytes  {Image.open(p).size}")


if __name__ == "__main__":
    main()
