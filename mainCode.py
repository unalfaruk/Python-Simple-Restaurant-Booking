import datetime
from allFunctions import *

prepareDB()

currentDT=datetime.datetime.now()
print ("Today: %s\nYou can select a date in the next 10 days." % str(currentDT))

while 1:
    choosing=whishChoosing()
    processChoosing(choosing)
