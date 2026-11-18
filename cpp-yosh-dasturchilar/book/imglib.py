"""Picture helpers for the C++ kids book (matplotlib)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch, Ellipse, Polygon
import os

OUT = os.environ.get("IMG_OUT") or os.path.join(os.path.dirname(__file__), "img")
if os.environ.get("ALIFBO") == "new":           # yangi alifbo: rasm matnlarini o'giramiz (kod matnidan tashqari)
    import matplotlib.text as _mt
    from alifbo import convert as _conv
    _orig_draw = _mt.Text.draw
    def _draw(self, renderer):
        fam = [f.lower() for f in self.get_fontfamily()]
        if not any("mono" in f for f in fam) and self._text:
            old = self._text; self._text = _conv(old)
            try: return _orig_draw(self, renderer)
            finally: self._text = old
        return _orig_draw(self, renderer)
    _mt.Text.draw = _draw
PAL = ["#4F8EF7", "#F2A900", "#2EAD5B", "#E5484D", "#8A5CF6", "#12B5CB", "#FF7A45", "#E64980"]
LIGHT = ["#E3EDFF", "#FFF4D6", "#E3F7EA", "#FFE3E3", "#EEE6FF", "#DDF6FA", "#FFEADF", "#FFE3EF"]
plt.rcParams["font.family"] = "DejaVu Sans"


def canvas(w=10, h=4):
    fig, ax = plt.subplots(figsize=(w, h), dpi=150)
    ax.set_xlim(0, w); ax.set_ylim(0, h); ax.axis("off")
    ax.set_aspect("equal")
    return fig, ax


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight", pad_inches=0.12, facecolor="white")
    plt.close(fig)


def box(ax, x, y, w, h, text="", fc="#E3EDFF", ec="#4F8EF7", fs=12, bold=False, color="#1F2328", r=0.15, lw=2, mono=False, va="center"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec, lw=lw))
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha="center", va=va, fontsize=fs, color=color,
                fontweight="bold" if bold else "normal", family="DejaVu Sans Mono" if mono else "DejaVu Sans", wrap=True)


def arrow(ax, x1, y1, x2, y2, color="#495057", lw=2.2, style="-|>", rad=0.0, ms=18):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=ms, color=color, lw=lw,
                                 connectionstyle=f"arc3,rad={rad}"))


def text(ax, x, y, s, fs=12, color="#1F2328", bold=False, ha="center", va="center", mono=False, **kw):
    ax.text(x, y, s, fontsize=fs, color=color, fontweight="bold" if bold else "normal", ha=ha, va=va,
            family="DejaVu Sans Mono" if mono else "DejaVu Sans", **kw)


def robot(ax, x, y, s=1.0, color="#4F8EF7", mood="happy", wave=False):
    """Kodi the robot. (x, y) = bottom-centre; s = scale (height ~ 2.2*s)."""
    # legs
    ax.add_patch(Rectangle((x - 0.35 * s, y), 0.18 * s, 0.35 * s, fc="#868E96", ec="none"))
    ax.add_patch(Rectangle((x + 0.17 * s, y), 0.18 * s, 0.35 * s, fc="#868E96", ec="none"))
    # body
    ax.add_patch(FancyBboxPatch((x - 0.6 * s, y + 0.35 * s), 1.2 * s, 0.85 * s, boxstyle=f"round,pad=0,rounding_size={0.15*s}", fc=color, ec="#1F2328", lw=1.5))
    ax.add_patch(FancyBboxPatch((x - 0.3 * s, y + 0.55 * s), 0.6 * s, 0.35 * s, boxstyle=f"round,pad=0,rounding_size={0.06*s}", fc="white", ec="#1F2328", lw=1))
    ax.text(x, y + 0.725 * s, "C++", ha="center", va="center", fontsize=9 * s, fontweight="bold", color=color)
    # arms
    ax.plot([x - 0.6 * s, x - 0.9 * s], [y + 0.95 * s, y + 0.6 * s], color="#1F2328", lw=3 * s)
    if wave:
        ax.plot([x + 0.6 * s, x + 0.95 * s], [y + 0.95 * s, y + 1.35 * s], color="#1F2328", lw=3 * s)
        ax.add_patch(Circle((x + 0.98 * s, y + 1.42 * s), 0.09 * s, fc="#F2A900", ec="#1F2328", lw=1))
    else:
        ax.plot([x + 0.6 * s, x + 0.9 * s], [y + 0.95 * s, y + 0.6 * s], color="#1F2328", lw=3 * s)
    ax.add_patch(Circle((x - 0.92 * s, y + 0.57 * s), 0.08 * s, fc="#F2A900", ec="#1F2328", lw=1))
    if not wave:
        ax.add_patch(Circle((x + 0.92 * s, y + 0.57 * s), 0.08 * s, fc="#F2A900", ec="#1F2328", lw=1))
    # head
    ax.add_patch(FancyBboxPatch((x - 0.5 * s, y + 1.25 * s), 1.0 * s, 0.75 * s, boxstyle=f"round,pad=0,rounding_size={0.2*s}", fc="#DDE6F5", ec="#1F2328", lw=1.5))
    # eyes
    for dx in (-0.2, 0.2):
        ax.add_patch(Circle((x + dx * s, y + 1.68 * s), 0.11 * s, fc="white", ec="#1F2328", lw=1))
        ax.add_patch(Circle((x + dx * s + 0.02 * s, y + 1.68 * s), 0.05 * s, fc="#1F2328", ec="none"))
    # mouth
    if mood == "happy":
        t = [i / 20 for i in range(21)]
        import math
        ax.plot([x - 0.18 * s + 0.36 * s * k for k in t], [y + 1.45 * s - 0.08 * s * math.sin(math.pi * k) for k in t], color="#1F2328", lw=2 * s)
    elif mood == "wow":
        ax.add_patch(Circle((x, y + 1.43 * s), 0.07 * s, fc="#1F2328"))
    else:
        ax.plot([x - 0.15 * s, x + 0.15 * s], [y + 1.43 * s, y + 1.43 * s], color="#1F2328", lw=2 * s)
    # antenna
    ax.plot([x, x], [y + 2.0 * s, y + 2.2 * s], color="#1F2328", lw=2 * s)
    ax.add_patch(Circle((x, y + 2.25 * s), 0.08 * s, fc="#E5484D", ec="#1F2328", lw=1))


def bubble(ax, x, y, w, h, s, fs=12, tail=(-0.4, -0.4), fc="white", ec="#495057"):
    """Speech bubble with bottom-left (x, y). tail = offset of tail tip from bottom-left corner + 0.4."""
    box(ax, x, y, w, h, "", fc=fc, ec=ec, r=0.25, lw=1.8)
    tx, ty = x + 0.45, y
    ax.add_patch(Polygon([[tx, ty + 0.02], [tx + 0.35, ty + 0.02], [tx + tail[0], ty + tail[1]]], closed=True, fc=fc, ec=ec, lw=1.8))
    ax.add_patch(Rectangle((tx + 0.02, ty - 0.01), 0.31, 0.06, fc=fc, ec="none"))
    ax.text(x + w / 2, y + h / 2, s, ha="center", va="center", fontsize=fs, color="#1F2328", wrap=True)


def flow(ax, items, y, h=1.0, x0=0.2, gap=0.5, w=None, total=None, fs=11, colors=None):
    n = len(items)
    total = total or ax.get_xlim()[1] - 2 * x0
    w = w or (total - gap * (n - 1)) / n
    xs = []
    for i, it in enumerate(items):
        x = x0 + i * (w + gap)
        c = (colors or list(range(n)))[i] % len(PAL)
        box(ax, x, y, w, h, it, fc=LIGHT[c], ec=PAL[c], fs=fs, bold=True)
        if i:
            arrow(ax, x - gap + 0.05, y + h / 2, x - 0.05, y + h / 2)
        xs.append(x)
    return xs, w


def cells(ax, x, y, values, w=0.9, h=0.8, labels=None, top=None, fc="#E3EDFF", ec="#4F8EF7", fs=14, lfs=10, mono=True, colors=None):
    for i, v in enumerate(values):
        f = fc if not colors else LIGHT[colors[i] % 8]
        e = ec if not colors else PAL[colors[i] % 8]
        box(ax, x + i * w, y, w, h, str(v), fc=f, ec=e, fs=fs, mono=mono, r=0.05, bold=True)
        if labels:
            text(ax, x + i * w + w / 2, y - 0.25, str(labels[i]), fs=lfs, color="#5A6270", mono=True)
        if top:
            text(ax, x + i * w + w / 2, y + h + 0.25, str(top[i]), fs=lfs, color="#5A6270", mono=True)
