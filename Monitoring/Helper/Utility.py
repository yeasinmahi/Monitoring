import os

class Utility(object):
    species = "Utility"
    def CreateFilePath(self,path):

        isExist = os.path.exists(path)
        #print(isExist)
        
        if not isExist:
          os.makedirs(path)


