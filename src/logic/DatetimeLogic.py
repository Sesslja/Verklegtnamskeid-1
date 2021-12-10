from datetime import datetime, timezone, date
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
        return dt
    
    def testDate(self, start_date: list = None):
        now = datetime.datetime.now()
        if start_date is None:
            date = datetime.datetime.now()
            dt = self.generateDatetimeNow(None)
        else:
            date = datetime.datetime(start_date[0],start_date[1],start_date[2])
            dt = datetime.date(start_date[0],start_date[1],start_date[2]).strftime('%A %d %B %Y')
        if  date > now or date == now:
            date = True
        else: 
            date = False
        return date, dt

    def betweenTwoDates(self, start_date, end_date):
        date_search_from = self.datetime(start_date)
        date_search_to = self.datetime(end_date)
        date_list = list(range(date_search_from, date_search_to))
        return date_list



