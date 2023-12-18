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
        "L": ((-1, 0), (0, +1)), 
        "J": ((-1, 0), (0, -1)), 
        "7": ((+1, 0), (0, -1)), 
        "F": ((+1, 0), (0, +1)), 
        ".": ((0, 0), (0, 0)),            # ground tile
        "S": ((0, 0), (0, 0))             # starting tile
    }

    def __init__(self, file):
        self.S_COORDS = None
        self.map_matrix = self.open(file)
        self.NROWS = len(self.map_matrix)
        self.NCOLS = len(self.map_matrix[0])
        self.visited_matrix = [[0 for j in range(self.NCOLS)] for i in range(self.NROWS)]
        self.count = 0

        self.walk_map()

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
    

    def check_connected(self, i, j, i1, j1):
        # check if (i1, j1) points to (i, j) 
        tile = self.get_tile(i1, j1)
        (dy1, dx1), (dy2, dx2) = self.symbol_coords[tile]
        if (i1+dy1, j1+dx1) == (i, j) or (i1+dy2, j1+dx2) == (i, j):
            return True
        return False

    def starting_points(self):
        # get all the points that are connected to S
        iS, jS = self.S_COORDS
        self.visited_matrix[iS][jS] = self.count
        self.count += 1
        dr = (
            (0, -1), (-1, 0), 
            (0, +1), (+1, 0)
        )
        next_steps = []
        for dy, dx in dr:
            i1, j1 = iS+dy, jS+dx
            if self.check_coords(i1, j1) and self.check_connected(iS, jS, i1, j1):
                next_steps.append((i1, j1))
                self.visited_matrix[i1][j1] = self.count
        self.count += 1

        return next_steps
    
    def next(self, i, j):
        # given (i, j) return next such that both point at each other
        tile = self.get_tile(i, j)
        dr1, dr2 = self.symbol_coords[tile]
        for dy, dx in (dr1, dr2):
            i1, j1 = i+dy, j+dx
            if self.check_coords(i1, j1) and not self.visited_matrix[i1][j1] and self.check_connected(i,j, i1,j1):
                # valid coord and not visited already and (i1, j1) points to (i, j)
                self.visited_matrix[i1][j1] = self.count
                return i1, j1
        return None
        
    def check_finish(self, coords):
        # check if every position is again in the begining S_COORD
        bool_coords = [c == self.S_COORDS for c in coords]
        return bool_coords

    def walk_map(self):
        start_coords = self.starting_points()
        next_coords = []
        aux = True
        while aux:
            next_coords = []
            for start in start_coords:
                next_coord = self.next(*start)
                if next_coord is None:
                    # closed path
                    continue
                next_coords.append(next_coord)
            self.count += 1
            start_coords = next_coords
            if not next_coord:
                # the list is empty
                aux = False

    def get_furthest(self):
        flatten_map = [elem for row in self.visited_matrix for elem in row]
        return max(flatten_map)
            
    
obj = PipesMap("day-10/input.txt")

print(obj.get_furthest())

