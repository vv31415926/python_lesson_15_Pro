from day_data import DayData
import datetime

class WeekData:
    def __init__(self):
        today = datetime.datetime.today()
        self.selected_day = today.strftime("%w")

        self.to_week = {'1': DayData(), '2': DayData(), '3': DayData(),
                        '4': DayData(), '5': DayData(), '6': DayData(),
                        '0': DayData()}
        self.to_week['1'].set_default()
        self.to_week['2'].set_default()
        self.to_week['3'].set_default()
        self.to_week['4'].set_default()
        self.to_week['5'].set_default()
        self.to_week['6'].set_default( mode='weekend' )
        self.to_week['0'].set_default( mode='weekend' )

    def __str__(self):
        s = str(   self.to_week[str(self.selected_day)]   )
        return s

    # получить планы на указанный день недели - смещение от текущего
    def get_plan_day(self,d):
        today = datetime.datetime.today()
        today = today + datetime.timedelta(d)
        self.selected_day = today.strftime("%w")
        s = str(   self.to_week[self.selected_day]   )
        return s


    def add_plan( self, d, lst:list ):
        today = datetime.datetime.today()
        today = today + datetime.timedelta(d)
        self.selected_day = today.strftime("%w")
        for s in lst:
            a = self.to_week[self.selected_day]
            self.to_week[self.selected_day].add_punkt( s )
            aa = self.to_week[self.selected_day]


if __name__ == '__main__':
    wd = WeekData()
    print( wd.get_plan_day( 0 ) )
    print( wd.get_plan_day( 1 ) )
    print( wd.get_plan_day( 2 ) )
    print( wd.get_plan_day( 3 ) )
    print( wd.get_plan_day( 4 ) )
    print( wd.get_plan_day( 5 ) )
    print( wd.get_plan_day( 6 ) )