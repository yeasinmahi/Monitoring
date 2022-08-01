import matplotlib.pyplot as plt
import pandas as pd
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
            x_date_time = pd.to_datetime(x)


            max= np.max(y)
            min= np.min(y)
            max = max*1.3
            min = min*.7

            plt.title(name)
            plt.xlabel("Date")
            plt.ylabel("Count")

            plt.ylim(min,max)

            plt.plot(x_date_time.day, y)

            plt.savefig('Data/Images/'+name+'.png', bbox_inches='tight')
            plt.clf()
            return True
        except:
            return False;
        #plt.show()



