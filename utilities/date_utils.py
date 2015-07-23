from datetime import datetime
from math import ceil
from dateutil.relativedelta import relativedelta
import calendar

__author__ = 'Modulus'



def get_saturdays():
    today = datetime.now()
    start = datetime.date(datetime(1986, 1, 1))
    days = []
    for current_year in range(start.year, today.year):
        for current_month in range(1, 12):
            month_range = calendar.monthrange(current_year, current_month)
            for current_day in range(month_range[0], month_range[1]):
                try:
                    if current_day > 0:
                        date = datetime.date(datetime(current_year, current_month, current_day))
                        if date.isoweekday() == 6:
                            days.append(date)

                except ValueError as e:
                    #TODO: ADD logger
                    x = 10
    return days

class DateUtils(object):

    @staticmethod
    def get_dates(start_date, end_date=datetime.now()):
        dates = []
        if start_date == datetime.today():
            dates.append(datetime.now())
        elif start_date and end_date:
            delta1 = relativedelta(end_date, start_date).years
            decade = int(ceil(delta1 / 10.0))

            current_date = start_date
            for value in range(0, decade):
                dates.append(datetime.date(datetime(current_date.year, 12, 31)))
                current_date += relativedelta(years=10)

            rest = 9 - len(dates)
            current_date = start_date
            new_dates = []
            for value in range(0, decade):
                for sub_value in range(0, int(rest / len(dates))):
                    current_date += relativedelta(years=rest)
                    new_dates.append(current_date)

            dates.extend(new_dates)

        return dates



def dateformat():
    return "%d.%m.%Y"

def front_dateformat():
    return "%m/%d/%Y"