from Helper.Data_Populate import Data_Populate

config = None
class Settings:
    species = "Configurations"
    global config
    config = Data_Populate.GetConfig()

    def GetConfig(self):
        return config

    def GetConnectionString(self,connectionName):
        for x in config["ConnectionStrings"]:
            if x["name"] == connectionName:
                obj= x
                break
            else:
                x = None
        return x;
    def GetQueries(self):
        return config["queries"]