from datetime import datetime, timezone
import datetime
try:
    from dateutil.relativedelta import relativedelta
except ModuleNotFoundError:
    print('virkar ekki')

class DateTime():
    def __init__(self) -> None:
        self.datetime = datetime()
        '''self.now = datetime.datetime.now()
        self.days_ahead = datetime.datetime.now() + relativedelta(days=3)
        self.weeks_ahead = datetime.datetime.now() + relativedelta(weeks=2)
        self.month_ahead = datetime.datetime.now() + relativedelta(months=1)
        self.months_ahead = datetime.datetime.now() + relativedelta(months=3)'''


    def datetimeToUtc(self, start_date: list=None):
        start_date = start_date
        if start_date is None:
            dt = self.datetime.now()
            date = dt.replace(tzinfo=timezone.utc).timestamp()
        else:
            dt = self.datetime(start_date[0], start_date[1], start_date[2])
            date = dt.replace(tzinfo=timezone.utc).imestamp()
        return int(date) 
    
    def testDate(self, start_date: list = None): 
        start_date = start_date
        if start_date is None:
            dt = self.datetime.now()
        else:
            dt = self.datetime(start_date[0], start_date[1], start_date[2])
        try: 
            dt >= self.datetime.now()
            date = True
        except: 
            date = False
        return date

    def betweenTwoDates(self, start_date, end_date):
        date_search_from = self.datetime(start_date)
        date_search_to = self.datetime(end_date)
        date_list = list(range(date_search_from, date_search_to))
        return date_list
    
    def relative_date(self, dt):

        if dt is not None and len(dt) > 0:

            now = datetime.now()
            then = arrow.get(dt).naive

            rd = relativedelta(then, now)
            if rd.years or rd.months:
                months = 12 * rd.years + rd.months

                if months < 0:
                    if months == -1:
                        return "Due 1 month ago"

                    return "Due %i months ago" % -months

                if months == 1:
                    return "Due in 1 month"
                return "Due in %d months" % months

            elif rd.days > 7 or rd.days < -7:
                weeks = rd.days / 7

                if weeks < 0:
                    if weeks == -1:
                        return "Due 1 week ago"
                    return "Due %i weeks ago" % -weeks

                if weeks == 1:
                    return "Due in 1 week"
                return "Due in %d weeks" % weeks

            else:

                if rd.days == 0:
                    return "Due Today"

                elif rd.days < 0:
                    if rd.days == -1:
                        return "Due 1 day ago"
                    return "Due %i days ago" % -rd.days

                elif rd.days == 1:
                    return "Due in 1 day"

                return "Due in %d days" % rd.days

        else:
            return ""
    
    
    def get_relative_date(dt):

        ahead = (dt - now).days

        if ahead < 7:
            print("Due in " + str(ahead) + " days")

        elif ahead < 31:
            print("Due in " + str(ahead/7) + " weeks")

        else:
            print("Due in " + str(ahead/30) + " months")


