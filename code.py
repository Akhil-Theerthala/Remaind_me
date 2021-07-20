import datetime
import csv
import pandas as pd
from plyer import notification
import numpy as np
import pdb



def notify(head,text):
    notification.notify(
        title = head,
        message = text,
        app_icon = None,
        timeout = 10,
    )

def alarm(tim,dat,heading,description):
    for i in range(len(tim)):
        hour = tim[i][0]
        min = int(tim[i][1])
        date_check =dat[i].split('-')
        now = datetime.datetime.now()
        
        if (int(date_check[0]) == now.day and int(date_check[1]) == now.month and now.year == int(date_check[2])):
            if ((hour == now.hour) 
                and (min == now.minute) 
                and (now.second == 0)
                and ((now.microsecond/1000)<1)):
                # mic_list.append(now.microsecond)
                notify(heading[i], description[i])
            # if ((hour == now.hour) 
            #     and (min == now.minute) and (now.second > 0)) :
            #     pdb.set_trace()

### To do : ###
# 1. Fix the time issue 
# 2. Fix the shell notification issue
# 3. Vectorize the time conversion or look up online for time libraries
# 4. Convert to exe and add to start up apps and verify

if __name__ == '__main__':  
    #Reading the file:
    #declaring the variables...
    time_in_file = []
    date_in_file = []
    heading = []
    description = []
    time_converted = []
    while (1):
        file_name = 'entry_log.csv'
        length = len(pd.read_csv(file_name))
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile)
            fields = next(reader)
            for row in reader:
                if row[0] not in time_in_file:
                    time_in_file.append(row[0].strip())
                    date_in_file.append(row[1].strip())
                    heading.append(row[2])
                    description.append(row[3])

        
        for i in range(len(time_in_file)):
            time_raw = time_in_file[i].split(' ')
            hr = int(time_raw[0][:2])
            
            if 'pm' == time_raw[1].casefold() and hr != 12:
                hr += 12
            if [hr,time_raw[0][3:]] not in  time_converted:
                time_converted.append([hr,time_raw[0][3:]])

        #Ringing the alarm
        alarm(time_converted,date_in_file,heading,description)