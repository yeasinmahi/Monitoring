import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
from Helper.Utility import Utility

class MatPlot(object):
    species = "Diagram"

   
    def Chart(self,data,name,chart,titel):
        if(chart=="line"):
            self.Line(data,name,titel)
        if(chart=="pie"):
            self.Pie(data,name,titel)

    def Line(self,data,name,titel):
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

            fig, ax = plt.subplots()
            ax.plot(x_date_time, y,linestyle='--', marker='o', color='b', label='line with marker')

            plt.title(titel)
            plt.xlabel("Date")
            plt.ylabel("Count")

            plt.ylim(min,max)
           
           
            plt.grid()
           
            myFmt = mdates.DateFormatter('%d')
            ax.xaxis.set_major_formatter(myFmt)
            fig.autofmt_xdate()

            
            
            Utility().CreateFilePath('Data/Images')
            plt.savefig('Data/Images/'+name+'.png', bbox_inches='tight')
            plt.clf()
            return True
        except:
            return False;
        plt.show()

    def Pie(self,data,name,titel):
        x = []
        y = []
        try:
            for row in data:
                x.append(row[0])
                y.append(row[1])
            
            plt.title(titel)
            
            plt.pie(y,labels=x)
            Utility().CreateFilePath('Data/Images')
            plt.savefig('Data/Images/'+name+'.png', bbox_inches='tight')
            plt.clf()
            return True
        except:
            return False;



