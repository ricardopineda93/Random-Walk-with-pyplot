from random import choice

class RandomWalk():
    '''A class used to generate random walks'''

    def __init__(self, num_points=5000):
        '''Initializing attributes of a walk'''
        self.num_points = num_points

        #Every walk starts at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        self.direction = choice([-1, 1])
        self.distance = choice([0, 1, 2, 3, 4])
        self.step = self.direction * self.distance
        return self.step


    def fill_walk(self, get_step):
        '''Calculating all points in the walk'''

        #Keep taking steps until walk reaches desired length
        while len(self.x_values) < self.num_points:
            #decide which direction to go and how far in that direction
            x_step = get_step()
            y_step = get_step()

            #rejecting moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            #calculating the next move
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)