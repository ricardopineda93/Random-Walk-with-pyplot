import matplotlib.pyplot as plt
from statistics import median

from random_walk import RandomWalk

while True: #keep making new walks as long as the program is active
    #make a random walk and plot the points
    rw = RandomWalk(10000) #the input here is basically running the class with this number of points since it
    #is feeding the 'point numbers' attribute for the class
    rw.fill_walk(rw.get_step)
    point_numbers= list(range(rw.num_points))#make a list from 0-the number of points we set in the call to the class
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds , s=5) #we plot the scatter points and we use
    #the 'point number' to gradually darken the scatter as the number of points plotted increases to show the path of the walk

    #settings for the axes and title of graph
    plt.title('Random Walk', fontsize = 14)
    plt.xlabel('X Values', fontsize = 10)
    plt.ylabel('Y Values', fontsize = 10)

    #this is to hide the axes to get a pure view of our scatter
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    #marking the origin step as a gren dot to see where we start
    plt.scatter(0, 0, c='green', edgecolors='none', s=25, label='Origin Step')
    #marking the median step taken in the step, e.g. the mid-step as a blue dot
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none',
                s=25, label="Final Step")
    #mark the final step taken as a yellow dot
    plt.scatter(rw.x_values[int(median(rw.x_values))], rw.y_values[int(median(rw.y_values))],
                c='yellow', s=25, label='Median Step')
    #create a legend and have it show at a set position in the graph
    plt.legend(loc='upper left', fontsize=8)
    plt.show()

    keep_running = input("Want to make another walk? (Y/N)")
    if keep_running == 'n':
        break

