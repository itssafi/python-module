import calendar
#import os
import sys

data = calendar.TextCalendar(calendar.SUNDAY).formatyear(2014, 2, 1, 1, 4)
with open(sys.argv[1], 'w') as fileobject:
    fileobject.write(data)
    print 'Succefully writted data'
