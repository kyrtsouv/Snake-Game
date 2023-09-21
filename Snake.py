class Snake():
    
    def __init__(self,X,Y,size):
        self.size = size
        self.length = 2
        self.head = [X,Y]
        self.blocks = [[X,Y],[X,Y-1]]

    def add(self,block):
        self.length += 1
        self.blocks.append(block)

    def move(self,direction):
        if direction == "R":
            self.head[0] += 1
        elif direction == "L":
            self.head[0] -= 1
        elif direction == "U":
            self.head[1] -= 1
        elif direction == "D":
            self.head[1] += 1
        for i in range(1,self.length):
            self.blocks[self.length-i] = self.blocks[self.length-i-1]

        self.blocks[0] = [self.head[0],self.head[1]]