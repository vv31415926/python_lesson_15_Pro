
from week_data import WeekData

class Plans:
    def __init__(self):
        self.wd = WeekData()

    def get_works_day(self, d=0 ):
        s = self.wd.get_plan_day( d )
        return s

    def set_works_day(self, d=0, lst=[] ):
        s = self.wd.add_plan( d, lst )
        return s


if __name__ == '__main__':
    plan = Plans()
    print(  plan.get_works_day( 1 )  )