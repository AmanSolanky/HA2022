import csv
import matplotlib.pyplot as plt
from uiManager import UiManager
from excelProcessing import csvPr
csvprobj = csvPr()
csvprobj.mappedDependencies()
print(csvprobj.iterationMapping)
#for i in range(1,(csvprobj.length[-1]-csvprobj.iterationMapping['M1'][-1])+1):
#   csvprobj.iterationMapping['M1'].append(csvprobj.iterationMapping['M1'][-1])
#plt.plot(csvprobj.length,csvprobj.iterationMapping['M1'])
#plt.ylabel("Microservice")
#plt.xlabel("Builds")
#plt.title("Build vs Microservice failure")
#plt.show()
ui = UiManager(csvprobj)
ui.mService = list(csvprobj.iterationMapping.keys())[2]
ui.render()



