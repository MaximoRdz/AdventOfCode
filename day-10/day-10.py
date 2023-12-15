# | is a vertical tile connecting north and south.
# - is a horizontal tile connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no tile in this tile.
# S is the starting position of the animal; 
# S is assumed to be connected to the two adjacent pipes
# directly pointing at it

class PipesMap:
    # i, j convention
    symbol_coords = {
        "|": ((-1, 0), (+1, 0)), 
        "-": ((0, -1), (0, +1)), 
        "L": ((+1, 0), (0, +1)), 
        "J": ((+1, 0), (0, -1)), 
        "7": ((-1, 0), (0, -1)), 
        "F": ((-1, 0), (0, +1)), 
        ".": ((0, 0), (0, 0)),            # ground tile
        "S": ((0, 0), (0, 0))             # starting tile
    }

    def __init__(self, file):
        self.S_COORDS = None
        self.map_matrix = self.open(file)
        self.NROWS = len(self.map_matrix)
        self.NCOLS = len(self.map_matrix[0])

    def open(self, file):
        # data into matrix and set S coordinates
        with open(file, "r") as myfile:
            data = myfile.read()
        rows = data.split("\n")
        matrix = []
        for i, row in enumerate(rows):
            matrix.append([])
            for j, c in enumerate(row):
                matrix[i].append(c)
                if c == "S":
                    self.S_COORDS = i, j
        return matrix

    def check_coords(self, i, j):
        if (0 <= i < self.NROWS) and (0 <= j < self.NCOLS):
            return True
        else:
            return False

    def get_tile(self, i, j):
        return self.map_matrix[i][j]

    def pipe_connections(self, i, j):
        tile = self.get_tile(i, j)
        (dy1, dx1), (dy2, dx2) = self.symbol_coords[tile]
        return (i+dy1, j+dx1), (i+dy2, j+dx2)
    
    def check_connected(self, i, j):
        # which of the adjacent pipes point to i, j or false
        dr = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        connections = []
        for dy, dx in dr:
            c1, c2 = self.pipe_connections(i+dy, j+dx)
            if c1 == (i, j) or c2 == (i, j):
                # adjacent pipe connected to current tile
                connections.append((i+dy, j+dx))
        if connections:
            return connections
        else:
            return False



    def close_path(self):
        # start at S and finish at S
        start_coords = self.S_COORDS
        start_sym = "S"

        (y1, x1), (y2, x2) = self.pipe_connections(start_sym, *start_coords)
        print((y1, x1), (y2, x2))


obj = PipesMap("day-10/example.txt")
print(*obj.map_matrix, sep="\n")
print(obj.check_connected(2, 1))


