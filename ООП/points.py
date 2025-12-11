class point:
    """класс для работы  с координатами точек"""
    x=0
    y=0
    points=[]
    def __init__(self, x: int = 0, y: int = 0):
        self.x=x
        self.y=y
        point.points.append([self.x,self.y])
    def show(self):
        print(point.points)
    def __add__(self, other):
         point=self.x+other.x,self.y+other.y
         return point
    def __sub__(self, other):
        point=self.x-other.x,self.y-other.y
        return point
    def __mul__(self, other):
        point = self.x * other.x, self.y * other.y
        return point
    def __truediv__(self, other):
        point = self.x / other.x, self.y / other.y
        return point
    def __lt__(self, other):
        return self.x<other.x and self.y<other.y
    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y
    def __gt__(self, other):
        return self.x>other.x and self.y>other.y
    def __ge__(self, other):
        return self.x>=other.x and self.y>=other.y
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
    def __ne__(self, other):
        return self.x!=other.x and self.y!=other.y











