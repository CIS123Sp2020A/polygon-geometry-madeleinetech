#Madeleine Brown
#Polygon Geometry

#parent class
class Polygon():
    def __init__(self, num_of_sides, sidesList):
        self.n = num_of_sides
        self.sides = sidesList
    #finds and returns the perimeter
    def findPerimeter(self):
        perimeter = 0
        for i in range(self.n):
            perimeter += self.sides[i]
        return perimeter
    #displays the value of each side    
    def dispSide(self):
        for i in range(self.n):
            print("Side", i+1, 'is', self.sides[i])

#class for any triangle
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3, sidesList)
    #finds the area of the triangle
    def findArea(self):
        a, b, c = self.sides
        p = (a + b + c)/2
        triArea = (p * (p - a) * (p - b) * (p - c)) **.5
        print('The area of the Triangle is %.2f' % (triArea))

#class for any rectangle
class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 4, sidesList)
    #finds the area of the rectangle
    def findArea(self):
        temp_sides = set(self.sides)
        sides = list(temp_sides)
        rectArea = sides[0] * sides[1]
        print('The area of the Rectangle is %.2f.' % (rectArea))

#class for any irregular Polygon        
class n_gon(Polygon):
    def __init__(self, num_of_sides, sidesList):
        Polygon.__init__(self, num_of_sides, sidesList)
    #finds the area of an irregular polygon
    def findArea(self):
        apothem = int(input('Enter the apothem:'))
        n_gonArea = .5 * Polygon.findPerimeter(self) * apothem
        print('The area of this polygon is %.2f.' % (n_gonArea))
        

def main():
    #user inputs number of sides
    num_of_sides = int(input('Enter the number of sides: '))
    #empty list for sides
    sidesList = []
    #user inputs the side values
    for i in range(num_of_sides):
        sidesList.append(int(input('Enter the length of a side: ')))
    
#Enter test cases here
        
main()
