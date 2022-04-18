from random import randint, choice

class Room:

    def __init__(self, coords) -> None:
        self.coords = coords
        self.connections = []
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def __str__(self):
        return f'<^v>'

    def __repr__(self) -> str:
        return self.__str__()

    def connect(self, room):
        self.connections.append(room)



class Maze:

    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
        self.maze = self.build_maze()
        self.user_location = (0,0)

    def __str__(self) -> str:
        return_string = ''
        for row in self.maze:
            return_string += '  '.join([str(room) for room in row])+'\n\n'
        return return_string

    def build_maze(self):
        grid = [[Room((h,w)) for w in range(self.width)] for h in range(self.height)]

        for h in range(self.height):
            for w in range(self.width):
                # make connections here?
                pass
        return grid
                

    def begin_game(self):
        pass


print('Welcome to Maze Game')
print('What dimension do you want the maze to be?')
height = int(input('Height: '))
width = int(input('Width: '))

maze = Maze(height, width)

print(maze)