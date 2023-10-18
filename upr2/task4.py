class Vector3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        print(self.x, self.y, self.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):

        if isinstance(other, int):
            return (self.x + other, self.y + other, self.z + other)
        else:
            return (self.x + other.x, self.y + other.y, self.z + other.z)
    