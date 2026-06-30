from pathlib import Path
from PIL import Image

src = Path('/data/data/com.termux/files/home/kospi-cardnews-pages/weasy_pages/page_1.png')
out = Path('/data/data/com.termux/files/home/kospi-cardnews-pages/weasy_pages/page_1_thumb.png')
img = Image.open(src)
img.thumbnail((1600, 1600))
img.save(out)
print(out)
print(Image.open(out).size)
