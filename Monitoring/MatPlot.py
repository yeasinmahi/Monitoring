from os import name
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class MatPlot(object):
    species = "Diagram"

   

    def Line(self,data,name):
        x = []
        y = []
        try:
            for row in data:
                x.append(row[0])
                y.append(row[1])
            date_time = pd.to_datetime(x)
            DF = pd.DataFrame()
            DF['value'] = y
            DF = DF.set_index(date_time.day)

            plt.plot(DF)
            plt.savefig('Data/Images/'+name+'.png', bbox_inches='tight')
            plt.clf()
            return True
        except:
            return False;
        #plt.show()



