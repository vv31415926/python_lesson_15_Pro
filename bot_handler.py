

class BotHandler:
    def __init__(self):
        self.dic_user={}   #{ номер id:{ 'name': имяПольз, 'chatcount':'0', 'begtime':''  }    }


    def __str__(self):
        if len(self.dic_user) == 0:
            s = 'Пусто'
        else:
            s = ''
            for k,v in self.dic_user.items():
                name = self.dic_user[k]["name"]
                chatcount = self.dic_user[k]["chatcount"]
                begtime = self.dic_user[k]["begtime"]

                s += f'Пользователь id={k}\nимя: {name}\nзарегистрирован: {begtime}\nобращался: {chatcount} раз'
        return s

    def is_user(self, id_user):
        r = True
        if id_user not in self.dic_user:
            print(self.dic_user)
            self.dic_user[id_user] = {}
            self.dic_user[id_user]['name'] = '?'
            self.dic_user[id_user]['chatcount'] = '0'
            self.dic_user[id_user]['begtime'] = '0'
            r = False
        return r


    def get_name_user(self, id_user):
        # if id_user not in self.dic_user:
        #     print(self.dic_user)
        #     self.dic_user[id_user] = {}
        #     self.dic_user[id_user]['name'] = '?'
        #     self.dic_user[id_user]['chatcount'] = '0'
        #     self.dic_user[id_user]['begtime'] = '0'
        return self.dic_user[id_user]['name']

    def set_name_user(self, id_user, name ):
        self.dic_user[id_user]['name'] = name

    def get_chat_count( self,id_user ):
        v = self.dic_user[id_user]['chatcount']
        return v

    def set_beg_time( self, id_user, t ):
        self.dic_user[id_user]['begtime'] = t

    def calc_chat( self,id_user ):
        self.dic_user[id_user]['chatcount'] =  str(int( self.dic_user[id_user]['chatcount'])+1)
