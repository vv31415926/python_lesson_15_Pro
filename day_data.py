class DayData:
    def __init__(self):
        self.to_day = {}   # 'ЧЧ:ММ':'что делать'

    def __str__(self):
        s = ''
        lst = sorted( self.to_day.items() )
        for v in lst:
            s += v[0] + ' - ' + v[1] +'\n'
        return s

    # def set_per_day( self, hour:int, minute:int, to_execute:str ):
    #     key = str(hour).zfill(2)+':'+str(minute).zfill(2)
    #     self.to_day[key] = to_execute
    def add_punkt(self, s:str) :  # s= '09:00 - Планерка'
        lst = s.split('-',1)
        key = lst[0].strip()
        val = lst[1].strip()
        self.to_day[key] = val

    def set_default(self, mode='worker' ):
        if mode == 'worker':
            self.to_day['09:00'] = 'Планерка'
            self.to_day['16:00'] = 'Итоги дня'
            self.to_day['18:00'] = 'Фитнес'
        else:
            self.to_day['11:00'] = 'Шашлык'
            self.to_day['17:00'] = 'Футбол'

