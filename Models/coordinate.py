class coordinate:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get(self):
        return (self.x, self.y, self.z)

    def get2D(self):
        return (self.x, self.y)

    def __str__(self):
        return f'x={self.x}, y={self.y}, z={self.z}'