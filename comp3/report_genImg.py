import csv
import random
import os
import textwrap
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Rectangle

# -----------------------------
# Config
# -----------------------------
CSV_PATH = "testdataset.csv"
BASE_DIR = "inference"
EPOCH_PREFIX = "epoch_040_noise"
NUM_NOISES = 6
NUM_ROWS = 5
IMG_SIZE = 64
OUTPUT_PATH = "./image_report.png"
WRAP_WIDTH = 35   # controls line breaking in caption column

# -----------------------------
# Load CSV
# -----------------------------
with open(CSV_PATH, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

selected = random.sample(rows, NUM_ROWS)
# IMAGE_ID_COL = "img_no"   # CSV header 的名字
# WIDTH = 4
# image_ids = [41, 6964, 327, 380, 5500]
# id_set = {str(i).zfill(WIDTH) for i in image_ids}
# selected = [row for row in rows if row[IMAGE_ID_COL] in id_set]

# Figure & Grid
fig = plt.figure(figsize=(14, 1.9 * (NUM_ROWS + 1)), dpi=200)

gs = GridSpec(
    NUM_ROWS + 1,
    NUM_NOISES + 1,
    figure=fig,
    width_ratios=[3.0] + [1] * NUM_NOISES,
    height_ratios=[0.6] + [1] * NUM_ROWS,
    wspace=0.0,
    hspace=0.0
)

def draw_cell_border(ax, lw=1.0):
    rect = Rectangle((0, 0), 1, 1, fill=False, lw=lw, edgecolor="black",
                     transform=ax.transAxes, clip_on=False)
    ax.add_patch(rect)

# Header row
ax = fig.add_subplot(gs[0, 0])
ax.axis("off")
draw_cell_border(ax)

for j in range(NUM_NOISES):
    ax = fig.add_subplot(gs[0, j + 1])
    ax.text(0.5, 0.5, f"Noise {j}",
            ha="center", va="center",
            fontsize=14, fontweight="bold")
    ax.axis("off")
    draw_cell_border(ax)

# Content rows
for i, row in enumerate(selected):
    img_no = row["img_no"]
    caption = row["caption"]

    wrapped_caption = "[ID {}]\n{}".format(
        img_no,
        textwrap.fill(caption, width=WRAP_WIDTH)
    )

    # Caption cell
    ax = fig.add_subplot(gs[i + 1, 0])
    ax.text(0.02, 0.5, wrapped_caption,
            ha="left", va="center",
            fontsize=14, wrap=True)
    ax.axis("off")
    draw_cell_border(ax)

    # Image cells
    for n in range(NUM_NOISES):
        ax = fig.add_subplot(gs[i + 1, n + 1])

        img_path = os.path.join(
            BASE_DIR,
            f"{EPOCH_PREFIX}{n}",
            f"inference_{img_no}.jpg"
        )

        if os.path.exists(img_path):
            img = Image.open(img_path).convert("RGB")
            img = img.resize((IMG_SIZE, IMG_SIZE), Image.BICUBIC)
            ax.imshow(img)
        else:
            ax.text(0.5, 0.5, "Missing", ha="center", va="center", fontsize=8)

        ax.axis("off")
        draw_cell_border(ax)

# Save
plt.savefig(OUTPUT_PATH, bbox_inches="tight")
plt.close()
