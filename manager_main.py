from dateandtime import hours_f, minutes_f
from writetocsv import WriteToCSV
from printchart import PrintChart
import os
from time import sleep
dirname = "\Archives"
pngname = "\Charts"
while True:
    try: #Create dir for files
        actualpath = os.getcwd()
        os.mkdir(actualpath + dirname)
        print("Created")
    except:
        pass

    try: #Create dir for .png
        actualpath = os.getcwd()
        os.mkdir(actualpath + pngname)
    except:
        pass

    #time = time_f()
    twriteh = int(hours_f())
    twritem = int(minutes_f())

    WriteToCSV(twriteh, twritem)
    PrintChart()
    sleep(45)


"""
Wysylanie E-mail
Formatowanie długoczasowe
wykres tygodniowy
"""