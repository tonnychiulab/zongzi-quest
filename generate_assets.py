"""生成粽情冒險版像素風格素材"""
from PIL import Image, ImageDraw, ImageFont
import os, math

BASE = "assets/items"
ICON_BASE = "assets/icons"
os.makedirs(f"{BASE}/north-zongzi", exist_ok=True)
os.makedirs(f"{BASE}/south-zongzi", exist_ok=True)
os.makedirs(f"{BASE}/alkaline-zongzi", exist_ok=True)
os.makedirs(f"{BASE}/sugar-animated", exist_ok=True)
os.makedirs(f"{BASE}/soysauce-animated", exist_ok=True)


def make_canvas(size=90, bg=(0,0,0,0)):
    img = Image.new("RGBA", (size, size), bg)
    return img, ImageDraw.Draw(img)


# ── 粽子共用形狀：倒三角形金字塔 ────────────────────────────────────────────

def draw_zongzi(draw, size, body_color, leaf_color, highlight, label_color, wrap_lines=True):
    """畫一個三角形粽子"""
    cx = size // 2
    top_y = int(size * 0.08)
    bot_y = int(size * 0.88)
    half_w = int(size * 0.38)

    # 竹葉（底層，稍微大一點）
    leaf_pts = [
        (cx, top_y - 4),
        (cx - half_w - 6, bot_y + 4),
        (cx + half_w + 6, bot_y + 4),
    ]
    draw.polygon(leaf_pts, fill=leaf_color)

    # 粽身
    body_pts = [
        (cx, top_y + 6),
        (cx - half_w, bot_y),
        (cx + half_w, bot_y),
    ]
    draw.polygon(body_pts, fill=body_color)

    # 高光
    hl_pts = [
        (cx, top_y + 8),
        (cx - int(half_w * 0.35), top_y + int(size * 0.28)),
        (cx + int(half_w * 0.1), top_y + int(size * 0.28)),
    ]
    draw.polygon(hl_pts, fill=highlight)

    if wrap_lines:
        # 綁繩紋路
        for t in [0.35, 0.62]:
            lx_l = cx - int(half_w * t)
            lx_r = cx + int(half_w * t)
            ly = top_y + int((bot_y - top_y) * t)
            draw.line([(lx_l, ly), (lx_r, ly)], fill=(80,40,10,200), width=2)

    # 頂端小節（繩結）
    draw.ellipse([(cx-5, top_y-2), (cx+5, top_y+8)], fill=(80,40,10,255))

    return body_pts


# ── 北部粽：清蒸，米粒外露感，草綠色 ─────────────────────────────────────────

def make_north_zongzi(frame=0, size=90):
    img, draw = make_canvas(size)
    leaf_green = (72, 140, 60, 255)
    body_col = (220, 205, 160, 255)  # 米白偏黃
    highlight = (240, 230, 190, 200)
    draw_zongzi(draw, size, body_col, leaf_green, highlight, None)
    # 頂端加「北」字小標
    draw.text((size//2 - 6, size//2 - 2), "北", fill=(100,60,20,200))
    # 動畫：輕微搖擺偏移
    if frame > 0:
        offset = int(math.sin(frame * 1.2) * 2)
        img = img.transform(img.size, Image.AFFINE, (1,0,offset,0,1,0))
    return img


# ── 南部粽：油光飽滿，深棕色，深竹葉 ─────────────────────────────────────────

def make_south_zongzi(frame=0, size=90):
    img, draw = make_canvas(size)
    leaf_green = (40, 90, 35, 255)   # 深墨綠
    body_col = (130, 80, 30, 255)    # 深棕色（滷汁）
    highlight = (170, 115, 55, 200)
    draw_zongzi(draw, size, body_col, leaf_green, highlight, None)
    # 南標
    draw.text((size//2 - 6, size//2 - 2), "南", fill=(220,180,100,220))
    # 油光效果：小圓點
    cx = size // 2
    draw.ellipse([(cx-3, size*0.4), (cx+5, size*0.5)], fill=(200,150,60,120))
    if frame > 0:
        offset = int(math.sin(frame * 1.0) * 2)
        img = img.transform(img.size, Image.AFFINE, (1,0,offset,0,1,0))
    return img


# ── 鹼粽：半透明黃金色，神秘光暈 ─────────────────────────────────────────────

def make_alkaline_zongzi(frame=0, size=90):
    img, draw = make_canvas(size)
    # 光暈（動畫用，隨 frame 呼吸）
    glow_r = int(size * 0.42 + math.sin(frame * 0.7) * 3)
    cx, cy = size // 2, size // 2
    for r in range(glow_r, glow_r - 10, -2):
        alpha = int(30 + (glow_r - r) * 12)
        draw.ellipse([(cx-r, cy-r), (cx+r, cy+r)], fill=(255, 215, 0, alpha))

    leaf_green = (100, 160, 60, 200)
    body_col = (255, 215, 80, 230)   # 黃金半透明
    highlight = (255, 240, 180, 200)
    draw_zongzi(draw, size, body_col, leaf_green, highlight, None, wrap_lines=False)
    # 鹼字
    draw.text((size//2 - 6, size//2 - 2), "鹼", fill=(180,100,10,240))
    # 閃光
    star_alpha = int(180 + math.sin(frame * 1.5) * 75)
    draw.text((size//2 + 12, size//4), "✦", fill=(255,255,200,star_alpha))
    return img


# ── 砂糖：白色圓形小包裝 ──────────────────────────────────────────────────────

def make_sugar(frame=0, size=120):
    img, draw = make_canvas(size)
    cx, cy = size // 2, size // 2

    # 袋子底部半圓
    draw.ellipse([(cx-28, cy), (cx+28, cy+38)], fill=(245,245,240,255))
    # 袋子主體
    draw.rectangle([(cx-28, cy-25), (cx+28, cy+20)], fill=(245,245,240,255))
    # 封口
    draw.rectangle([(cx-22, cy-32), (cx+22, cy-25)], fill=(220,220,215,255))
    draw.rectangle([(cx-18, cy-40), (cx+18, cy-32)], fill=(200,200,195,255))

    # 糖粒紋路
    for i in range(5):
        px = cx - 12 + i * 6
        py = cy - 10
        draw.ellipse([(px,py), (px+4,py+4)], fill=(255,255,255,180))

    # "砂糖" 文字
    draw.text((cx - 14, cy + 4), "砂糖", fill=(100,100,100,220))

    # 動畫：輕微漂浮
    if frame > 0:
        offset = int(math.sin(frame * 0.8) * 3)
        img = img.transform(img.size, Image.AFFINE, (1,0,0,0,1,offset))
    return img


# ── 醬油：深色長方形玻璃瓶 ────────────────────────────────────────────────────

def make_soysauce(frame=0, size=164):
    img, draw = make_canvas(size, bg=(0,0,0,0))
    cx = size // 2

    # 瓶身
    bottle_w, bottle_h = 40, 90
    bx = cx - bottle_w // 2
    by = size // 2 - bottle_h // 2 + 10

    # 主瓶體
    draw.rounded_rectangle([(bx, by), (bx+bottle_w, by+bottle_h)],
                           radius=6, fill=(60, 30, 10, 255))
    # 高光
    draw.rectangle([(bx+5, by+8), (bx+12, by+bottle_h-10)],
                   fill=(100, 60, 30, 150))

    # 瓶頸
    neck_w = 18
    nx = cx - neck_w // 2
    draw.rectangle([(nx, by-20), (nx+neck_w, by)], fill=(60,30,10,255))
    # 瓶蓋
    draw.rectangle([(nx-3, by-28), (nx+neck_w+3, by-20)], fill=(180,30,20,255))

    # 標籤
    draw.rectangle([(bx+4, by+20), (bx+bottle_w-4, by+60)],
                   fill=(230,210,150,255))
    draw.text((bx+5, by+24), "醬油", fill=(80,30,10,220))

    # 液體色澤
    draw.rectangle([(bx+4, by+bottle_h//2), (bx+bottle_w-4, by+bottle_h-4)],
                   fill=(40,15,5,200))

    if frame > 0:
        offset = int(math.sin(frame * 0.7) * 2)
        img = img.transform(img.size, Image.AFFINE, (1,0,0,0,1,offset))
    return img


# ── 圖示（小型，用於 UI）─────────────────────────────────────────────────────

def make_zongzi_icon(size=48):
    """粽子圖示 for UI"""
    img, draw = make_canvas(size, bg=(0,0,0,0))
    leaf_green = (72, 140, 60, 255)
    body_col = (220, 180, 80, 255)
    highlight = (240, 220, 140, 200)
    draw_zongzi(draw, size, body_col, leaf_green, highlight, None, wrap_lines=False)
    return img


def make_condiment_icon(size=48):
    """沾醬圖示 for UI（砂糖+醬油混合）"""
    img, draw = make_canvas(size, bg=(0,0,0,0))
    # 小碗
    draw.ellipse([(8, 20), (40, 40)], fill=(240,230,200,255))
    draw.arc([(8, 20), (40, 40)], 0, 180, fill=(180,150,100,255), width=2)
    # 碗裡液體
    draw.ellipse([(12, 22), (36, 36)], fill=(80,40,10,220))
    # 小粽子符號
    draw.polygon([(24,8),(18,20),(30,20)], fill=(72,140,60,220))
    return img


# ── 生成所有幀 ───────────────────────────────────────────────────────────────

print("生成素材...")

# 北部粽（4幀動畫）
for i in range(4):
    img = make_north_zongzi(frame=i, size=90)
    img.save(f"{BASE}/north-zongzi/{i}.png")
print("  北部粽 OK")

# 南部粽（4幀）
for i in range(4):
    img = make_south_zongzi(frame=i, size=90)
    img.save(f"{BASE}/south-zongzi/{i}.png")
print("  南部粽 OK")

# 鹼粽（8幀，有呼吸光暈）
for i in range(8):
    img = make_alkaline_zongzi(frame=i, size=90)
    img.save(f"{BASE}/alkaline-zongzi/{i}.png")
print("  鹼粽 OK")

# 砂糖（8幀）
for i in range(8):
    img = make_sugar(frame=i, size=120)
    img.save(f"{BASE}/sugar-animated/{i}.png")
print("  砂糖 OK")

# 醬油（8幀）
for i in range(8):
    img = make_soysauce(frame=i, size=164)
    img.save(f"{BASE}/soysauce-animated/{i}.png")
print("  醬油 OK")

# UI 圖示
os.makedirs(ICON_BASE, exist_ok=True)
make_zongzi_icon(48).save(f"{ICON_BASE}/zongzi-icon.png")
make_condiment_icon(48).save(f"{ICON_BASE}/condiment-icon.png")
print("  UI 圖示 OK")

print("全部素材生成完畢！")
