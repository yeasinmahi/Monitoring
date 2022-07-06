from os import name
import matplotlib.pyplot as plt
import numpy as np


class MatPlot(object):
    species = "Diagram"

    def Line(self,data,name):
        x = []
        y = []
        try:
            for row in data:
                x.append(row[0])
                y.append(row[1])
                #print(str(row[0]) + " " + str(row[1]))
            plt.plot(x, y)
            plt.savefig('Data/Images/'+name+'.png', bbox_inches='tight')
            return True
        except:
            return False;
        #plt.show()



