import datetime
import sqlite3

def newBooking():
    aBooking=Booking()

    dateRaw=input("Select a date(dd-mm-yyyy): ")
    dateProcessed=datetime.datetime.strptime(dateRaw, '%d-%m-%Y')
    aBooking.setDate(dateProcessed)

    ownerRaw=str(input("Owner name(Gozde, Mehmet etc.): "))
    aBooking.setOwner(ownerRaw)

    numberOfPeople=input("Number of people(3,4,5 etc): ")
    aBooking.setPeople(numberOfPeople)

    timeRaw=input("Select a time(11,17 etc.): ")
    aBooking.setTime(timeRaw)

    bookingID=aBooking.saveToDB()
    print("\n\tYour booking ID is: %s, please note for other proceess like cancelation.\t" % str(bookingID))

class Booking:

    def setDate(self,dateOfParameter):
        self.dateOf=dateOfParameter

    def setTime(self,timeOfParameter):
        self.timeOf=timeOfParameter

    def setPeople(self,numberOfPeopleParameter):
        self.numberOfPeople=numberOfPeopleParameter

    def setOwner(self,ownerParameter):
        self.owner=ownerParameter

    def saveToDB(self):
        conn=sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute('insert into dates(owner,howmanypeople,dateof,timeof) values(?,?,?,?)', [self.owner,self.numberOfPeople,self.dateOf,self.timeOf])
        conn.commit()
        return c.lastrowid
        conn.close()
