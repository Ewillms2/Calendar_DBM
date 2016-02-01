# P-2 MCS 260 due Monday 23 February 2015 at noon.
"""
An anydbm object stores the appointments for the day.
Appointments are stored as strings as values in the anydbm object.
The keys are the dates of the appointment, stored in the format
'YYYYMMDD' where YYYY is the year, MM the month, and DD the day.
A zero is inserted for single digit numbered months and days.
"""
import anydbm
from time import localtime
DTPL = tuple(localtime())
DATE = str(DTPL[0]) + ('%02d' % DTPL[1]) + ('%02d' % DTPL[2])
CAL = anydbm.open('caldb', 'c')
if CAL.has_key(DATE):
    print CAL[DATE]
else:
    print 'No appointments for today, ' + DATE + '.'
DAY = raw_input('Give a date to view or update (hit enter to exit) : ')
if(DAY != ''):
    if CAL.has_key(DAY):
        print 'Appointments for ' + DAY + ':'
        print CAL[DAY]
    PROMPT = 'Enter appointment for ' + DAY + ' (hit enter to exit) :\n'
    APT = raw_input(PROMPT)
    if APT != '':
        if not CAL.has_key(DAY):
            CAL[DAY] = APT
        else:
            ANSWER = raw_input('Append or replace appointment ? (a/r) ')
            if ANSWER == 'a':
                CAL[DAY] += '\n' + APT
            else:
                CAL[DAY] = APT
CAL.close()
