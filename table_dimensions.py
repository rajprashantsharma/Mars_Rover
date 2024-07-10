class TableDimensions:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height

    def is_on_table(self, x, y):
        """Check if the position (x, y) is on the tabletop."""
        return 0 <= x < self.width and 0 <= y < self.height

