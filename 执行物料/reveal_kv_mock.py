#!/usr/bin/env python3
"""【08】Reveal 三句 · LP Hero 平面稿
Cyber Wabi-sabi: 近黑底 + LED 矩阵点阵 + 冷青光,文字为绝对主角。
"""
import math, random, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.insert(0, str(Path(sys.executable).parent.parent.parent))

W, H = 1920, 1080
SCALE = 2  # supersampling
w, h = W * SCALE, H * SCALE

# ---------- 字体 ----------
def find_cjk_font():
    cands = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
    ]
    for c in cands:
        if Path(c).exists():
            return c
    # fallback: managed runtime bundled CJK
    rt = Path(sys.executable).parent.parent.parent
    for p in rt.rglob("*.ttf"):
        if any(k in p.name.lower() for k in ("cjk", "noto", "sc")):
            return str(p)
    raise RuntimeError("no CJK font found")

CJK = find_cjk_font()
LATIN = "/System/Library/Fonts/HelveticaNeue.ttc"
if not Path(LATIN).exists():
    LATIN = CJK

def font(path, size, index=0):
    return ImageFont.truetype(path, size * SCALE, index=index)

# ---------- 底色:近黑,微微的冷色渐变 ----------
img = Image.new("RGB", (w, h))
px = img.load()
for y in range(h):
    t = y / h
    r = int(8 + 6 * t)
    g = int(10 + 8 * t)
    b = int(16 + 14 * t)
    for x in range(w):
        px[x, y] = (r, g, b)

# 远处一团很克制的冷青辉光(左上)
glow = Image.new("RGB", (w, h), (0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([w*0.05, -h*0.35, w*0.75, h*0.45], fill=(10, 40, 48))
glow = glow.filter(ImageFilter.GaussianBlur(260 * SCALE))
img = Image.blend(img, Image.blend(img, glow, 0.9), 0.55)

d = ImageDraw.Draw(img)

# ---------- LED 矩阵点阵:下半部,渐次隐没,唯有一颗 AI 键亮着 ----------
random.seed(6)
dot_area_top = int(h * 0.62)
cols, rows = 60, 12
gx = w * 0.82 / cols
gy = (h * 0.34) / rows
x0 = w * 0.09
for r_ in range(rows):
    for c_ in range(cols):
        x = x0 + c_ * gx
        y = dot_area_top + r_ * gy
        fade = 1 - (r_ / rows) * 0.85          # 越往下越暗
        fade *= 0.35 + 0.65 * random.random()  # 随机熄灭感
        v = int(70 * fade)
        if v > 6:
            rad = 2.2 * SCALE
            d.ellipse([x-rad, y-rad, x+rad, y+rad], fill=(v//3, v, v))

# 那颗亮着的 AI 键(点阵黄金位置)
ai_x, ai_y = x0 + 42 * gx, dot_area_top + 3.5 * gy
halo = Image.new("RGB", (w, h), (0, 0, 0))
hd = ImageDraw.Draw(halo)
hd.ellipse([ai_x-70*SCALE, ai_y-70*SCALE, ai_x+70*SCALE, ai_y+70*SCALE], fill=(30, 160, 175))
halo = halo.filter(ImageFilter.GaussianBlur(40 * SCALE))
img = Image.blend(img, Image.blend(img, halo, 0.95), 0.5)
d = ImageDraw.Draw(img)
d.ellipse([ai_x-6*SCALE, ai_y-6*SCALE, ai_x+6*SCALE, ai_y+6*SCALE], fill=(160, 245, 250))

# ---------- 文字 ----------
CYAN = (126, 231, 240)
WHITE = (235, 240, 242)
DIM = (128, 138, 146)
FAINT = (88, 96, 104)

def draw_center(text, f, y, fill, spacing=0):
    if spacing:
        # manual letter spacing
        widths = [d.textlength(ch, font=f) for ch in text]
        total = sum(widths) + spacing * SCALE * (len(text) - 1)
        x = (w - total) / 2
        for ch, cwid in zip(text, widths):
            d.text((x, y), ch, font=f, fill=fill)
            x += cwid + spacing * SCALE
        return
    tw = d.textlength(text, font=f)
    d.text(((w - tw) / 2, y), text, font=f, fill=fill)

# 左上:品牌/型号字标
f_brand = font(LATIN, 22)
d.text((w*0.06, h*0.06), "CYBERBOARD R6", font=f_brand, fill=WHITE)
d.text((w*0.06, h*0.06 + 34*SCALE), "INVISIBLE AI IO", font=font(LATIN, 13), fill=FAINT)
# 右上:AM 单字母标(以点阵方块暗示 monogram 物理存在)
mx, my, ms = w*0.915, h*0.058, 7*SCALE
for i in range(3):
    for j in range(3):
        if (i, j) in [(0,0),(1,0),(2,0),(0,1),(2,1),(0,2),(1,2),(2,2)]:
            d.rectangle([mx+i*ms*1.6, my+j*ms*1.6, mx+i*ms*1.6+ms, my+j*ms*1.6+ms], fill=DIM)

# 过线问句(序幕资产,小字,灰色)
f_q = font(CJK, 24)
f_q_en = font(LATIN, 16, index=1)
draw_center("AI 已经可以聆听你。但为什么，今天的键盘还不行？", f_q, h*0.175, DIM)
draw_center("AI is listening to you. So why isn't your keyboard?", f_q_en, h*0.175 + 46*SCALE, FAINT)

# 分隔细线
lw_ = w * 0.06
d.line([(w-lw_)/2, h*0.30, (w+lw_)/2, h*0.30], fill=(50, 58, 64), width=SCALE)

# Pivot 句
f_pivot = font(CJK, 40)
draw_center("因为到今天为止，还没有一把键盘，", f_pivot, h*0.345, (190, 198, 204))
draw_center("为 AI 时代而生。", f_pivot, h*0.345 + 64*SCALE, (190, 198, 204))
draw_center("Because no keyboard has ever been built for the AI era.", font(LATIN, 17, index=1), h*0.345 + 130*SCALE, FAINT)

# Solution 句(主角)
f_sol_brand = font(LATIN, 64)
f_sol = font(CJK, 76)
draw_center("CYBERBOARD R6", f_sol_brand, h*0.565, WHITE, spacing=6)
draw_center("第一把学会聆听的键盘", f_sol, h*0.565 + 108*SCALE, CYAN)
draw_center("The first keyboard that listens.", font(LATIN, 19, index=1), h*0.565 + 224*SCALE, DIM)

# 底部:D Day 信息条
d.line([(w-w*0.24)/2, h*0.905, (w+w*0.24)/2, h*0.905], fill=(50, 58, 64), width=SCALE)
draw_center("INVISIBLE AI IO · COMING", font(LATIN, 15), h*0.925, FAINT, spacing=4)

# ---------- 输出 ----------
img = img.resize((W, H), Image.LANCZOS)
out = Path("/Users/linan/Documents/Kimi/Workspaces/CBR6/CB-R6_08_Reveal三句_LP-Hero_平面稿_v1.png")
img.save(out, "PNG")
print("saved:", out)
