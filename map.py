import math as m

class Map:
    def __init__(self, x_length, y_length):
        self.x_length = x_length
        self.y_length = y_length
        self.grids = [[' ' for x in range(0, x_length, 1)] for y in range(0, y_length, 1)]

    #becareful of indexing, it is y, x.
    def display_map(self):
        for y in range(0, self.y_length, 1):
            
            for x in range(0, self.x_length, 1):
                print('|' + str(self.grids[self.y_length - 1 - y][x]), end = '')
            
                if x == (self.x_length - 1):
                    print('|')
        
                    
    def mark_location(self, x, y, icon):
        self.grids[int(y)][int(x)] = icon

    def mark_relative_location(self, currentX, currentY, distance, angle, icon):
        angle_rad = angle * (m.pi/180)
        locationX = int(currentX + distance*m.cos(angle_rad))
        locationY = int(currentY + distance*m.sin(angle_rad))
        print(locationX, locationY)
        self.mark_location(locationX, locationY, icon)
