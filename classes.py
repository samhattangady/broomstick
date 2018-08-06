'''
classes.py
Contains all datastructures for broomstick
'''

class Minefield:
    def __init__(self, width, height, tiles):
        self.width = width
        self.height = height
        self.tiles = tiles

class Tile:
    def __init__(self, index, position, value):
        self.index = index
        self.position = position
        self.value = value
