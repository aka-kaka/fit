#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


class FoodInfo():
    """Расчет калорий исходя из потребленных жиров, углеводов и белков
 формула расчета 9*жиры+4(углеводы+белки)
 get_kkalories - вывод расчета"""

    def __init__ (self,prot, fats, carb):
        self.prot = prot
        self.fats = fats
        self.carb = carb
 
    def get_kcalories(self):
        return float("{:.2f}".format(4 * self.prot + 9 * self.fats + 4 * self.carb))
 
    def __add__ (self,value):
        return FoodInfo(self.prot + value.prot, self.fats + value.fats, self.carb + value.carb)
    
    
class Human():
    """imt - ииндекс массы тела
    BMR - Базовый метаболизм  (сколько нужно ккал в сутки)
    по формуле Миффлина-Сан Жеора 
    BMR = [9.99 x вес (кг)] + [6.25 x рост (см)] - [4.92 x возраст (в годах)]
    + 5 (для мужчин) -161 (дляженщин).
    Это количество калорий необходимых для поддержки организма впассивном
    состоянии. Умножив базовый метаболизм на 
    коэффициент нагрузки мы иполучаем нужно количество калорий в сутки."""
    dic={"1":1.2,
         "2":1.35,
         "3":1.55,
         "4":1.75,
         "5":1.95,
         'gend':["woman","муж","man","жен","m","w","м","ж"]}
    def __init__(self,weight,height, gender,age, activity):
        self.weight=float(weight)
        self.height=float(height)
        self.gender=gender.rstrip("\n")
        self.age=float(age)
        self.activity=float(activity)
    
    def imt(self):
        imt_dic={range(0,16): "Выраженный дефицит массы тела",
            range(16,18): 'Недостаточная (дефицит) масса тела',
            range(18,25):'Норма',
            range(25,30):'Избыточная масса тела (предожирение)',
            range(30,35):'Ожирение',
            range(35,40):'Ожирение резкое',
            range(40,100):'Очень резкое ожирение'}
        try:
            imt_int=int(self.height/((self.weight/100)**2))
            print(imt_int)
            for i in imt_dic.keys():
                if imt_int in i:
                    return imt_dic[i]
        except ValueError:
            print('some error')
        
        
        
    def calculate(self):
        BMR=(9.99*self.weight)+(6.25*self.height)-(4.92*self.age)
        if self.gender.lower() in ["m","м","муж","man"]:
            BMR=BMR+5
        else: BMR=BMR-161
        return float("{:.2f}".format(BMR*self.activity))
        

def new_hum():

    while True:
        try:
            weight=float(input('введите рост в сантиметрах: '))
            height=float(input('введите вес в киллограмах: '))
            gender=input("введите пол (M / Ж) : ")
            age=float(input('введите возраст: '))
            print("выберите активность..",
                  "1. Минимальная (1.2): сидячая работа, отсутствие спорта",
                  "2. Легкая (1.35): легкие физические упражнения около 3 раз за неделю,ежедневная утренняя зарядка, пешие прогулки;",
                  "3. Средняя (1.55): спорт до 5 раз за неделю;",
                  "4. Высокая (1.75): активный образ жизни вкупе с ежедневными интенсивными тренировками;",
                  "5. Экстремальная (1.95): максимальная активность - спортивный образ жизни, тяжелый физический труд, длительные тяжелые тренировки каждый день.",
                  sep="\n")
            activity=input(': ')
            if all([not Human.dic[activity],
                not gender.isalpha(),
                not 0<age<130,
                not 40<weight<230,
                not 10<height<130,
                gender.lower() not in Human.dic["gend"]]):
                raise ValueError 
        except ValueError:
            print("Введены недопустимые символы")
        else:
            return [weight,height,gender,age,Human.dic[activity]]


def open_file(file):
    with open(file,'r') as f:
        return f.readlines()


def save_file(file):
    v_new_hum=new_hum()
    with open(file,'w') as f:
        f.write("\n".join([str(l) for l in v_new_hum]))
        return v_new_hum


def get_data():
    while True:
        try:
            prot=float(input("Введите колличество белка потребленного за день в граммах: "))
            fats=float(input("Введите колличество жиров потребленных за день в граммах: "))
            carb=float(input("Введите колличество углеводов потребленных за день в граммах: "))
    
        except ValueError:
            print("Введены недопустимые символы")
        else:
            return FoodInfo(prot, fats, carb)

    
def minus(call):
    return call-(call*0.1)


def plus(call):
    return call+(call*0.1)


def get_hum():
    print (r"""давайте знакомится...
    введите имя: """)
    name=input()
    file=os.path.join(os.path.curdir,name.lower()+'.kkl')
    if os.path.isfile(file):
        while True:
            print (f'есть сохраненные даные по {name}',
               'что будем делать?', 
               "1.Прменить сохраненные данные", 
               '2.Ввести новые данные',
               "3.Показать сохраненные данные",
               "4.Выйти",
               sep="\n")
            inp=input()
    
            if inp =="1":
                a=open_file(file)
                print(a)
                human=Human(a[0],a[1],a[2],a[3],a[4])
                return human
            elif inp=="2":
                a=save_file(file)
                human=Human(a[0],a[1],a[2],a[3],a[4])
                return human
            elif inp =="3":
                print(open_file(file))
            elif inp=="4":
                break
            else: print ("Неправильный ввод")
    else: 
        a=save_file(file)
        human=Human(a[0],a[1],a[2],a[3],a[4])
        return human

   

if __name__ == '__main__':
    human=get_hum() #возвращает класс
    day=get_data()
    print (f'Всего за день получено {day.get_kcalories()} ккалл')
    print(f'Необходимо {human.calculate()}')
    if minus(human.calculate())<day.get_kcalories()<plus(human.calculate()):
        print ('суточное потребление в норме')
    elif day.get_kcalories()<minus(human.calculate()):
        print('суточное потребление меньше нормы')
    elif day.get_kcalories()>plus(human.calculate()):
        print('суточное потребление больше нормы')
    print(human.imt())