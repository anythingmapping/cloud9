import csv
import time
import datetime
import calendar

print datetime.datetime.now().time()
print calendar.day_name[datetime.datetime.today().weekday()]

#currentDay = "Sunday" + "Collect"
#currentDay = calendar.day_name[datetime.datetime.today().weekday()] + "Collect"
#print

"""

days = ['MondayCollect',
        'TuesdayCollect',
        'WednesdayCollect',
        'ThursdayCollect',
        'FridayCollect',
        'SaturdayCollect',
        'SundayCollect']
values = {"parks":[11,55,41,11,55,99,77], 
        "roading":[11,55,41,11,55,99,77],
        "private":[11,55,41,11,55,99,77]}
        
print len(values)

f = open("testoutput.csv", 'wt')

try:
    writer = csv.writer(f)
    writer.writerow(days)
    writer.writerow(values['parks'])
    writer.writerow(values['roading'])
    writer.writerow(values['private'])
finally:
    f.close()

#print open(testoutput.csv, 'rt').read()"""