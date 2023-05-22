class Figure:
    figures = [
        [[1,5,9,13], [4,5,6,7]],
        [[1,2,5,9], [0,4,8,9], [1,5,9,8], [4,5,6,10]],
        [[1,2,6,10], [0,4,5,6], [2,6,10,11], [3,5,6,7]],
        [[1,4,5,6], [1,4,5,9], [4,5,6,9], [1,5,6,9]],
    ]
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1 )
        self.color = random.randint(1, len(color) -1)
        self.rotation = 0