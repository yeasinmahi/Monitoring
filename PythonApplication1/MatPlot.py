import matplotlib.pyplot as plt
import numpy as np


class MatPlot(object):
    species = "Diagram"

    def Line(self,data):

        for row in data:
            print(str(row[0]) + " " + str(row[1]))
        plt.plot(data[0], data[1])
        plt.show()
        #xpoints = np.array([1, 8])
        #ypoints = np.array([3, 10])

        #plt.plot(xpoints, ypoints)
        #plt.show()



