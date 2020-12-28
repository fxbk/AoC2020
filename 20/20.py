import copy


file = open('input.txt', 'r')
input = file.read()
tiles = input.split('\n\n')


class Tile:
    def __init__(self, tile_string):
        self.id = tile_string[5:9]
        self.data = tile_string[11:].split('\n')
        self.top = self.data[0]
        self.bottom = self.data[-1]
        left = ''
        right = ''
        for row in self.data:
            left += row[0]
            right += row[-1]
        self.left = left
        self.right = right
        self.transformation = []

    def rotate_clockwise(self):
        tmp_top = copy.copy(self.top)
        self.top = self.left[::-1]
        self.left = self.bottom
        self.bottom = self.right[::-1]
        self.right = tmp_top
        self.transformation.append('rotation_clockwise')

    def flip_horizontally(self):
        tmp_top = copy.copy(self.top)
        self.top = self.bottom
        self.bottom = tmp_top
        self.transformation.append('flip_horizontally')

    def flip_vertically(self):
        self.bottom = self.bottom[::-1]
        self.top = self.top[::-1]
        tmp_right = copy.copy(self.right)
        self.right = self.left
        self.left = tmp_right
        self.transformation.append('flip_vertically')


tiles = [Tile(tile_string) for tile_string in tiles]

corner_tiles = []
result = 1
for base_tile in tiles:
    matching_tiles = 0
    for tile in tiles:
        if base_tile.id == tile.id:
            continue
        for rotation in range(4):
            for flip in range(2):
                if base_tile.top == tile.top or base_tile.top == tile.right or base_tile.top == tile.bottom or \
                        base_tile.top == tile.left:
                    matching_tiles += 1
                base_tile.flip_vertically()
            base_tile.rotate_clockwise()
    if matching_tiles == 2:
        corner_tiles.append(base_tile.id)
        result *= int(base_tile.id)

print(corner_tiles)
print(f'Solution part 1: {result}')
