import re

class User_Data:
    def __init__(self, arr):
        self.data = arr
        self.data_base = []

    def add_to_base(self, arr):
        self.data = self.data + arr
    
    def clear_data(self):
        for i in range(len(self.data)):
            temp = len(self.data_base) + i
            user_name = ''
            user_mail = ''
            pattern =  r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
            for j in range(len(self.data[i])):
                if j == 0 and (self.data[i][j] not in [name[j] for name in self.data_base]):
                    user_name = self.data[i][j]
                    continue
                elif j == 0 and not (self.data[i][j] not in [name[j] for name in self.data_base]):
                    print('Имя пользователя не уникально')
                    break

                if j == 1 and re.match(pattern, self.data[i][j]) is None:
                    print('Не существует такой почты')
                    break
                elif j == 1 and (not (self.data[i][j] not in [mail[j] for mail in self.data_base])) :
                    print('Адрес электронной почты недействителен ')
                    break
                elif j == 1:
                    user_mail = self.data[i][j]
                    continue
                if (int(self.data[i][j]) < 0) and j == 2:
                    print('Возраст не является положительным целым числом')
                    break
                elif (int(self.data[i][j]) < 16) and j == 2:
                    print('Пользователю меньше 16 лет')
                    break
                elif (int(self.data[i][j]) >= 16) and j == 2:
                    user_age = self.data[i][j]
                    self.data_base.append((user_name, user_mail))
                    continue
                    

    def print_data_base(self):
        self.clear_data()
        print(self.data_base)

