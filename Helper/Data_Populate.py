import json
import pandas as pd


class Data_Populate(object):
    species = "Data Load"

    def GetQuerys():
        try:
            f= open("datas.json")
            data = json.load(f)
            f.close()
            return data
        except:
            return ""

    def Export_Excel(self,data,name):
        df = pd.DataFrame(list(data))

        writer = pd.ExcelWriter('Data/Excels/'+name+'.xlsx')
        df.to_excel(writer, sheet_name=name, index=False)
        writer.save()

    def Excel_To_Html(self,name):
        df = pd.read_excel('Data/Excels/'+name+'.xlsx')
        return df.to_html(index=False)

      