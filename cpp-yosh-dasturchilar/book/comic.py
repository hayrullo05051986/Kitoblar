"""Comic strips with Malika (12-year-old girl) and Kodi (robot)."""
from imglib import *
import textwrap, math
from matplotlib.patches import Arc, Wedge

SKIN = "#F5C9A6"; HAIR = "#4A2C1A"; DRESS = "#E64980"


def girl(ax, x, y, s=1.0, mood="happy", arm=None, dress=DRESS):
    """Malika. (x,y) bottom-centre, height ~2.3*s."""
    # legs + shoes
    for dx in (-0.17, 0.07):
        ax.add_patch(Rectangle((x + dx * s, y + 0.1 * s), 0.1 * s, 0.45 * s, fc=SKIN, ec="none"))
        ax.add_patch(Ellipse((x + (dx + 0.05) * s, y + 0.08 * s), 0.26 * s, 0.13 * s, fc="#343A40"))
    # dress
    ax.add_patch(Polygon([[x - 0.48 * s, y + 0.5 * s], [x + 0.48 * s, y + 0.5 * s], [x + 0.25 * s, y + 1.35 * s], [x - 0.25 * s, y + 1.35 * s]], fc=dress, ec="#1F2328", lw=1.3))
    ax.add_patch(Rectangle((x - 0.25 * s, y + 1.05 * s), 0.5 * s, 0.07 * s, fc="white", ec="none"))
    # arms
    ax.plot([x - 0.24 * s, x - 0.5 * s], [y + 1.25 * s, y + 0.85 * s], color=SKIN, lw=5 * s, solid_capstyle="round")
    if arm == "up":
        ax.plot([x + 0.24 * s, x + 0.55 * s], [y + 1.25 * s, y + 1.75 * s], color=SKIN, lw=5 * s, solid_capstyle="round")
    elif arm == "point":
        ax.plot([x + 0.24 * s, x + 0.7 * s], [y + 1.25 * s, y + 1.3 * s], color=SKIN, lw=5 * s, solid_capstyle="round")
    else:
        ax.plot([x + 0.24 * s, x + 0.5 * s], [y + 1.25 * s, y + 0.85 * s], color=SKIN, lw=5 * s, solid_capstyle="round")
    # neck + head
    ax.add_patch(Rectangle((x - 0.06 * s, y + 1.33 * s), 0.12 * s, 0.12 * s, fc=SKIN, ec="none"))
    # hair back + ponytails
    ax.add_patch(Circle((x, y + 1.78 * s), 0.42 * s, fc=HAIR, ec="none"))
    for sgn in (-1, 1):
        ax.add_patch(Ellipse((x + sgn * 0.48 * s, y + 1.6 * s), 0.22 * s, 0.5 * s, angle=sgn * 20, fc=HAIR, ec="none"))
        ax.add_patch(Circle((x + sgn * 0.4 * s, y + 1.88 * s), 0.06 * s, fc="#F2A900", ec="none"))
    ax.add_patch(Circle((x, y + 1.72 * s), 0.34 * s, fc=SKIN, ec="#1F2328", lw=1.2))
    # fringe
    ax.add_patch(Wedge((x, y + 1.78 * s), 0.38 * s, 15, 165, fc=HAIR, ec="none"))
    # eyes
    for dx in (-0.12, 0.12):
        if mood == "wow":
            ax.add_patch(Circle((x + dx * s, y + 1.7 * s), 0.055 * s, fc="white", ec="#1F2328", lw=1))
            ax.add_patch(Circle((x + dx * s, y + 1.7 * s), 0.025 * s, fc="#1F2328"))
        else:
            ax.add_patch(Circle((x + dx * s, y + 1.7 * s), 0.035 * s, fc="#1F2328"))
    # cheeks
    for dx in (-0.2, 0.2):
        ax.add_patch(Circle((x + dx * s, y + 1.6 * s), 0.04 * s, fc="#FF8FA3", ec="none", alpha=0.7))
    # mouth
    if mood == "happy":
        ax.add_patch(Arc((x, y + 1.6 * s), 0.16 * s, 0.1 * s, theta1=200, theta2=340, color="#1F2328", lw=1.6))
    elif mood == "wow":
        ax.add_patch(Ellipse((x, y + 1.55 * s), 0.07 * s, 0.09 * s, fc="#1F2328"))
    elif mood == "think":
        ax.plot([x - 0.05 * s, x + 0.07 * s], [y + 1.56 * s, y + 1.58 * s], color="#1F2328", lw=1.6)
        ax.text(x + 0.48 * s, y + 2.2 * s, "?", fontsize=22 * s, fontweight="bold", color=PAL[4])
    elif mood == "sad":
        ax.add_patch(Arc((x, y + 1.52 * s), 0.14 * s, 0.08 * s, theta1=20, theta2=160, color="#1F2328", lw=1.6))


def speech(ax, x, y, w, h, s, tip, fs=12.5, fc="white", ec="#495057", width=None):
    """Speech bubble; tip=(tx,ty) absolute point it points to."""
    width = width or max(10, int(w * 7.6 * 12.5 / fs))
    s = "\n".join(textwrap.fill(p, width) for p in s.split("\n"))
    cx = min(max(tip[0], x + 0.35), x + w - 0.35)
    by = y if tip[1] < y else y + h
    ax.add_patch(Polygon([[cx - 0.18, by], [cx + 0.18, by], tip], closed=True, fc=fc, ec=ec, lw=1.6, zorder=4))
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.22", fc=fc, ec=ec, lw=1.6, zorder=5))
    ax.add_patch(Rectangle((cx - 0.16, by - 0.03), 0.32, 0.06, fc=fc, ec="none", zorder=6))
    ax.text(x + w / 2, y + h / 2, s, ha="center", va="center", fontsize=fs, color="#1F2328", zorder=7, linespacing=1.25)


PW, PH = 5.0, 4.9


def comic(name, panels, cols=2):
    """panels: list of dicts {m: text or None, k: text or None, mm: mood, km: mood, prop: fn(ax,x0,y0) or None,
    first: 'm'|'k' (who speaks on top), bg: colour index}"""
    rows = math.ceil(len(panels) / cols)
    W = cols * PW + (cols - 1) * 0.2
    H = rows * PH + (rows - 1) * 0.2
    fig, ax = plt.subplots(figsize=(W, H), dpi=150)
    ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off"); ax.set_aspect("equal")
    for i, p in enumerate(panels):
        r, c = divmod(i, cols)
        x0 = c * (PW + 0.2); y0 = H - (r + 1) * PH - r * 0.2
        bg = LIGHT[p.get("bg", i * 3) % 8]
        ax.add_patch(FancyBboxPatch((x0, y0), PW, PH, boxstyle="round,pad=0,rounding_size=0.15", fc=bg, ec="#1F2328", lw=2))
        ax.add_patch(Rectangle((x0 + 0.02, y0 + 0.02), PW - 0.04, 0.32, fc="#FFFFFF", ec="none", alpha=0.55))
        prop = p.get("prop")
        s = 0.74 if prop else 0.95
        gx, rx = x0 + 0.7, x0 + PW - 0.75
        girl(ax, gx, y0 + 0.2, s, mood=p.get("mm", "happy"), arm=p.get("arm"))
        robot(ax, rx, y0 + 0.2, s * 0.92, mood=p.get("km", "happy"), wave=p.get("wave", False))
        if prop:
            prop(ax, x0 + 1.45, y0 + 0.25)   # prop area ~ 2.1 x 1.6
        top_y = y0 + 0.2 + 2.3 * s + 0.15
        order = [p.get("first", "m"), "k" if p.get("first", "m") == "m" else "m"]
        texts = [(who, p.get(who)) for who in order if p.get(who)]
        avail = y0 + PH - 0.12 - top_y
        if len(texts) == 2:
            fs_ = p.get("fs", 12.5); wd = int((PW - 0.6) * 7.6 * 12.5 / fs_)
            n1 = len(textwrap.wrap(texts[0][1], wd)) + 0.8; n2 = len(textwrap.wrap(texts[1][1], wd)) + 0.8
            h1 = (avail - 0.12) * n1 / (n1 + n2); h2 = avail - h1 - 0.12
            boxes = [(y0 + PH - 0.12 - h1, h1), (top_y, h2)]
        else:
            fs_ = p.get("fs", 12.5); wd = int((PW - 0.6) * 7.6 * 12.5 / fs_)
            n1 = len(textwrap.wrap(texts[0][1], wd)) if texts else 1
            hh = min(avail, n1 * 0.33 * fs_ / 12.5 + 0.55)
            boxes = [(y0 + PH - 0.12 - hh, hh)]
        for (who, t), (by, bh) in zip(texts, boxes):
            if who == "m":
                speech(ax, x0 + 0.15, by, PW - 0.6, bh, t, tip=(gx + 0.1, y0 + 0.2 + 2.3 * s + 0.02), fc="#FFFFFF", ec=PAL[7], fs=p.get("fs", 12.5))
            else:
                speech(ax, x0 + 0.45, by, PW - 0.6, bh, t, tip=(rx - 0.05, y0 + 0.2 + 2.3 * s * 0.92 + 0.05), fc="#FFFFFF", ec=PAL[0], fs=p.get("fs", 12.5))
        ax.text(x0 + 0.18, y0 + 0.18, str(i + 1), fontsize=10, fontweight="bold", color="#868E96", va="center")
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight", pad_inches=0.08, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    def jars(ax, x, y):
        for i, (lab, c) in enumerate([("int", 0), ("char", 1), ("bool", 2)]):
            ax.add_patch(FancyBboxPatch((x + i * 0.72, y), 0.6, 0.9 + 0.2 * (i == 0), boxstyle="round,pad=0,rounding_size=0.1", fc=LIGHT[c], ec=PAL[c], lw=2))
            ax.text(x + i * 0.72 + 0.3, y + 0.4, lab, ha="center", fontsize=9, family="DejaVu Sans Mono", fontweight="bold")
    comic("test_comic.png", [
        dict(m="Kodi, nega oshxonada shakar, tuz va sut har xil idishda turadi?", k=None, mm="think"),
        dict(k="Har bir narsaga mos idish kerak! Kompyuter xotirasida ham xuddi shunday — har xil ma'lumot uchun har xil 'idish' bor.", m="Voy, ularning nomi nima?", first="k", prop=jars, km="happy", mm="wow"),
    ])
    print("ok")
