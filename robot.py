class Robot:
    DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]

    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None

    def place(self, x, y, facing):
        """Place the robot on the tabletop."""
        if 0 <= x <= 4 and 0 <= y <= 4 and facing in Robot.DIRECTIONS:
            self.x = x
            self.y = y
            self.facing = facing
        else:
            raise ValueError("Invalid PLACE command parameters.")

    def move(self):
        """Move the robot one unit forward in the direction it is currently facing."""
        if self.facing == "NORTH" and self.y < 4:
            self.y += 1
        elif self.facing == "SOUTH" and self.y > 0:
            self.y -= 1
        elif self.facing == "EAST" and self.x < 4:
            self.x += 1
        elif self.facing == "WEST" and self.x > 0:
            self.x -= 1

    def left(self):
        """Rotate the robot 90 degrees to the left."""
        directions = ["NORTH", "WEST", "SOUTH", "EAST"]
        self.facing = directions[(directions.index(self.facing) + 1) % 4]

    def right(self):
        """Rotate the robot 90 degrees to the right."""
        directions = ["NORTH", "EAST", "SOUTH", "WEST"]
        self.facing = directions[(directions.index(self.facing) + 1) % 4]

    def report(self):
        """Return the current position and direction of the robot."""
        return f"{self.x},{self.y},{self.facing}"