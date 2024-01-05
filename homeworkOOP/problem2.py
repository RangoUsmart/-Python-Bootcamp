from cmath import sqrt


class Cilind(object):
    
    def __init__(self,heigth,radius):
        self.h=heigth
        self.r=radius
    
    def volume(self,p):
        return p * (self.r) ** 2 * self.h
    
    def surface_area(self,p):
        base_area = p * (self.r)**2
        lateral_area = 2 * p * self.r * self.h
        return 2 * base_area + lateral_area
    
h = int(input("Введіть висоту циліндру: "))
r = int(input("Введіть радіус: "))   


result = Cilind(h,r)
print(result.volume(3.14))
print(result.surface_area(3.14))