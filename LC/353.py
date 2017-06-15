class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.w=width
        self.h=height
        self.food=collections.deque(food)
        self.coor_dif={'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
        self.snake=collections.deque([(0,0)])
        self.score=0
        
    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        
        x,y=self.snake[-1]
        dx,dy=self.coor_dif[direction]
        nx,ny=x+dx,y+dy
        # print self.snake, (nx,ny), self.food
        
        # fail check
        t=self.snake.popleft()
        if 0<=nx<self.h and 0<=ny<self.w and (nx,ny) not in self.snake:
            if self.food and self.food[0]==[nx,ny]:
                self.score+=1
                self.food.popleft()
                self.snake.appendleft(t)
            self.snake.append((nx,ny))
            return self.score
        return -1
        
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)