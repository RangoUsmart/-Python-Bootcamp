from cmath import sqrt


class Line(object):
    
    def __init__(self,coor1,coor2,coor3,coor4):
        self.coor1=coor1
        self.coor2=coor2
        self.coor3=coor3
        self.coor4=coor4
    
    def distance(self):
        result=sqrt((self.coor3-self.coor1)**2+(self.coor4-self.coor2)**2)
        return result
    
    def slope(self,coor1,coor2,coor3,coor4):
        result=(coor4 - coor2) / (coor3 - coor1)
        return result
x1 = int(input("Введіть координату x для першої точки: "))
y1 = int(input("Введіть координату y для першої точки: "))   

x2 = int(input("Введіть координату x для другої точки: "))
y2 = int(input("Введіть координату y для другої точки: "))

result = Line(x1,y1,x2,y2)
print(result.distance())
print(result.slope(x1,y1,x2,y2))