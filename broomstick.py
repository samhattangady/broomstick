'''
A broomstick is a good tool for sweeping things.
Even mines apparently.
'''

import pyautogui
from PIL import Image

TILES = {
          '_': Image.open('tiles/none.png'),
          0: Image.open('tiles/0.png'),
          1: Image.open('tiles/1.png'),
          2: Image.open('tiles/2.png'),
          3: Image.open('tiles/3.png'),
          4: Image.open('tiles/4.png'),
          5: Image.open('tiles/5.png'),
          6: Image.open('tiles/6.png'),
          7: Image.open('tiles/7.png'),
          8: Image.open('tiles/8.png'),
          'M': Image.open('tiles/mine.png')
        }

all_tiles = []
for tile in TILES:
    positions = pyautogui.locateAllOnScreen(TILES[tile])
    for p in positions:
        all_tiles.append({'value': tile, 'position': p})
all_tiles = sorted(all_tiles, key=lambda x: (x['position'][1], x['position'][0]))

width = len(set([x['position'][0] for x in all_tiles]))
for i, tile in enumerate(all_tiles):
    print(tile['value'], end=' ')
    if (i+1)%width == 0:
        print()

