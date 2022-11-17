import json

class Data_Populate(object):
    species = "Data Load"

    def GetConfig():
        try:
            f= open("config.json")
            data = json.load(f)
            f.close()
            return data
        except Exception as e:
            return print(e)

    