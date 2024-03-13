class Robot:
    def __init__(self):
        self.directions = ["NORTH", "EAST", "SOUTH", "WEST"]
        self.limit = 5
        self.x = None
        self.y = None
        self.f = None
        self.placed = False

    def place(self, x, y, f):
        if x > self.limit or x < 0 or y > self.limit or y < 0:
            return
        self.x = x
        self.y = y
        self.f = f
        self.placed = True


    def move(self):
        if self.placed == True:
            if self.f == "NORTH" and self.y < self.limit:
                self.y += 1
            elif self.f == "SOUTH" and self.y > 0:
                self.y -= 1
            elif self.f == "WEST" and self.x > 0:
                self.x -= 1
            elif self.f == "EAST" and self.x < self.limit:
                self.x += 1
        else:
            return


    #how to wrap around: -1 % 4--> -1/4 = -0.25. round down --> -1, -1 = 4 * -1 + r --> r = 3
    def left(self):
        if self.placed == True:
            current_idx = self.directions.index(self.f)
            new_idx = (current_idx - 1) % len(self.directions)
            self.f = self.directions[new_idx]
        else:
            return

    #same wrap around principle, but in other direction
    def right(self):
        if self.placed == True:
            current_idx = self.directions.index(self.f)
            new_idx = (current_idx + 1) % len(self.directions)
            self.f = self.directions[new_idx]
        else:
            return

    def report(self):
        if self.placed == True:
            print(f"Output: {self.x},{self.y},{self.f}")
        else:
            return
