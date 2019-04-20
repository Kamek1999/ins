import os
import seaborn as sns
from actualfollowers import GetFollower
import csv
import datetime
sns.set(style="darkgrid")
pathdir = os.getcwd() + "\csvs"
def WriteToCSV(twriteh, twritem):
    now = datetime.datetime.now()
    name = now.strftime("%B%d")

    if twritem == 0 \
            or twritem == 10\
            or twritem == 20\
            or twritem == 30\
            or twritem == 40\
            or twritem == 50:
        print("writing into CSV!")
        followers = GetFollower()
        header = ['hour', 'min', 'followers', 'hchart']
        hchart = str(twriteh+(twritem*(1/60)))
        row = [twriteh, twritem, followers, hchart]
        try:
            with open(name+'.csv', 'r', newline=''):
                pass
        except FileNotFoundError:
            with open(name+'.csv', 'a', newline='') as csv_file:
                csvwriter = csv.writer(csv_file)
                csvwriter.writerow(header)
        with open(name+'.csv', 'a', newline='') as csv_file:
            csvwriter = csv.writer(csv_file)
            csvwriter.writerow(row)
