from datetime import datetime, timezone, date, timedelta
import datetime


class DateTime():
    def __init__(self) -> None:
        '''self.now = datetime.datetime.now()
        self.days_ahead = datetime.datetime.now() + relativedelta(days=3)
        self.weeks_ahead = datetime.datetime.now() + relativedelta(weeks=2)
        self.month_ahead = datetime.datetime.now() + relativedelta(months=1)
        self.months_ahead = datetime.datetime.now() + relativedelta(months=3)'''


    def generateDatetimeNow(self, date_time =None):
        date_time = date_time
        if date_time is None:
            dt = datetime.date.today().strftime('%A %d %B %Y')
        elif date_time is datetime:
            dt = date_time.strftime('%A %d %B %Y')
        else:
            dt =datetime.date(date_time).strftime('%A %d %B %Y')
        return dt
    
    def testDate(self, startDate: list = None):
        now = datetime.datetime.now()
        if startDate is None:
            date = datetime.datetime.now()
            dt = self.generateDatetimeNow(None)
        else:
            date = datetime.datetime(startDate[0],startDate[1],startDate[2])
            dt = datetime.date(startDate[0],startDate[1],startDate[2]).strftime('%A %d %B %Y')
        if  date > now or date == now:
            date = True
        else: 
            date = False
        return date, dt

    def betweenTwoDates(self, start_date, end_date):
        sDate = [int(i) for i in start_date]
        startDate = datetime.datetime(sDate[0], sDate[1], sDate[2])
        eDate = [int(i) for i in end_date]
        endDate = datetime.datetime(eDate[0], eDate[1], eDate[2])
        allDates = [startDate + timedelta(days=x) for x in range((endDate-startDate).days + 1)]
        dateList = [date.strftime('%A %d %B %Y') for date in allDates]
        return dateList
    
    def datetimeToUtc(self, startDate = None):
        startDate = startDate.split(',')
        startDate = [int(i) for i in startDate]
        if startDate is None:
            dt = datetime.datetime.now()
            date = dt.replace(tzinfo=timezone.utc).timestamp()
        else:
            dt = datetime.datetime(startDate[0], startDate[1], startDate[2])
            date = dt.replace(tzinfo=timezone.utc).timestamp()
        return int(date) 



