'''
A broomstick is a good tool for sweeping things.
Even mines apparently.
'''

import pyautogui
from PIL import Image

unclicked_tile = Image.open('tiles/none.png')
tiles = pyautogui.locateAllOnScreen(unclicked_tile)
tiles = list(tiles)

print(len(tiles))

tiles = sorted(tiles, key=lambda x: (x[1], x[0]))
x,y = tiles[0][0]+5, tiles[0][1]+5

pyautogui.click(x,y)
