import pandas as pd
import numpy as np
import os
import shutil
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from sendmail import em
sns.set(style="darkgrid")
dirname = "Archives\\"
pngname = "Charts\\"




def PrintChart(): #wyzwalane o 23:50
    now = datetime.datetime.now()
    name = now.strftime("%B%d")
    if now.hour == 15 and now.minute == 11 : #23:50
        with open(name+'.csv', 'r', newline='', encoding='utf-8') as csv_file:
            mean = 0
            val = 0
            sample_data = pd.read_csv(csv_file)
            for n in sample_data.followers:
                if n > 0:
                    val = val + 1
                    mean = mean + n
            min_val=int(((mean/val)*0.95))
            max_val=int(((mean/val)*1.05))
            plt.plot(sample_data.hchart, sample_data.followers)
            plt.ylabel("Followers")
            plt.xlabel("Time [h]")
            plt.xticks(np.arange(0, 24, step=1))
            plt.yticks(np.arange(min_val, max_val, step=10))
            plt.savefig(name)
            try:
                em(name)
            except:
                print("Couldn't send it! :c")
            os.remove(name + '.png')
    if now.hour == 23 and now.minute == 50 : #23:50
        with open(name+'.csv', 'r', newline='', encoding='utf-8') as csv_file:
            mean = 0
            val = 0
            sample_data = pd.read_csv(csv_file)
            for n in sample_data.followers:
                if n > 0:
                    val = val + 1
                    mean = mean + n
            min_val=int(((mean/val)*0.95))
            max_val=int(((mean/val)*1.05))
            plt.plot(sample_data.hchart, sample_data.followers)
            plt.ylabel("Followers")
            plt.xlabel("Time [h]")
            plt.xticks(np.arange(0, 24, step=1))
            plt.yticks(np.arange(min_val, max_val, step=10))
            plt.savefig(name)
            try:
                em(name)
            except:
                print("Couldn't send it! :c")
        shutil.copyfile(name+'.csv', dirname + name+'.csv')
        shutil.copyfile(name+'.png', pngname + name+'.png')
        os.remove(name + '.csv')
        os.remove(name + '.png')
