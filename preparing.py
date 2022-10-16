from ast import Delete
import pandas as pd
import numpy as np

table = pd.read_csv("c:\\Users\\User\\Desktop\\Бекарыс\\python\\Data analysis\\data.csv", delimiter=',')
df = pd.DataFrame(table)

# ВОЗВВРАЩАЕТ FALSE ЕСЛИ ЯЧЕЙКА В ТАБЛИЦЕ ПУСТА
data = df.notnull() 

# ЕСЛИ TOTAL_INCOME  И  DAYS_EMPLOYED ПУСТЫЕ, ТО УДАЛЯЕТ ЭТИ СТРОКИ. ТАК КАК ЭТИ СТРОКИ НЕ ДАЮТ НАМ ПОЧТИ НИКАКУЮ ИНФОРМАЦИЮ
for i in range(len(df)):
    if data['total_income'][i] == False and data['days_employed'][i] == False:
        # DF.DROPNA УДАЛЯЕТ СТРОКУ ЕСЛИ ОНО ПОПАДАЕТ ПОД УСЛВИЕ 
        df = df.dropna()
# ПОСЛЕ УДАЛЕНИЯ СТРОКИ ИНДЕКСАЦИЯ СБИВАЕТСЯ. ТО ЕСТЬ ЕСЛИ БЫЛО 1 2 3 4 5 6.
# И УДАЛИЛИ 3 СТРОКУ. ТО ПОЛУЧИТСЯ 1 2 4 5 6(ПРОПУСТИТ 4)
# ТАК ВОТ ЧТО БЫ ЗАНОВО ПЕРЕ ИНДЕКСИРОВАТЬ ТАБЛИЦУ МЫ ИСПОЛЬЗУЕМ RESET_INDEX
df.reset_index(drop= True , inplace=True)





# 30000 let incorrect value
# used: absolute, round
def fixyears():
    for i in range(len(df['children'])):
        pos = abs(df['days_employed'][i])
        df['days_employed'][i] = pos/365
        year = pos/365
        age = df['dob_years'][i]
        if df['gender'][i] == 'F':
            if 18<(age - year)<58:
                df['days_employed'][i] = round(year)    
            else:
                df['days_employed'][i] = 'INCORRECT VALUE'
                daysemp = df['days_employed']
        if df['gender'][i] == 'M':
            if 18<(age - year)<63:
                df['days_employed'][i] = round(year)    
            else:
                df['days_employed'][i] = 'INCORRECT VALUE'
                daysemp = df['days_employed']
    # print(daysemp)
    return daysemp





# разделяем на 5 типа кредита

forwed = ['свадьба','на проведение свадьбы','сыграть свадьбу']

foreduc = ['заняться высшим образованием','дополнительное образование','высшее образование','образование','получение дополнительного образования',\
    'получение образования','профильное образование','получение высшего образования','заняться образованием']

forcar = ['на покупку своего автомобиля','автомобиль','сделка с автомобилем','сделка с подержанным автомобилем','автомобили',\
    'свой автомобиль','на покупку подержанного автомобиля','на покупку автомобиля','приобретение автомобиля']

forbus = ['покупка жилой недвижимости','операции с недвижимостью','покупка недвижимости','операции с коммерческой недвижимостью','строительство собственной недвижимости','недвижимость',\
    'операции со своей недвижимостью','строительство недвижимости','покупка коммерческой недвижимости']

forlive = ['операции с жильем','покупка жилья для сдачи','жилье','покупка своего жилья','покупка жилья','покупка жилья для семьи','ремонт жилью','строительство жилой недвижимости']

def credit_types():
    for i in range(len(df)):
        if df['purpose'][i] in foreduc:
            df['purpose'][i] = 'для образования'
        if df['purpose'][i] in forwed:
            df['purpose'][i] = 'для свадьбы'
        if df['purpose'][i] in forcar:
            df['purpose'][i] = 'для автомобиля'
        if df['purpose'][i] in forlive:
            df['purpose'][i] = 'для жилья'
        if df['purpose'][i] in forbus:
            df['purpose'][i] = 'для недвижимости'
    # с помощью value_counts видим каждые 5 типов по сколько раз встретились во всей таблицу
    counter_credit = df.value_counts("purpose")
    print(counter_credit)
#  возвращает таблицу с исправленными значениями по 5 типам кредита
    return df





def fix_salary():
    round_up_salary = round(df['total_income'])
    df['total_income'] = round_up_salary
    return df





# EDUCATIOn REPAIRING
"""ЗАМЕНЯЕМ ПОХОЖИЕ ДУБЛИКАТЫ, таблица EDUCATION имеет одинаковые элементы разных регистров по\
     типу ВЫСШЕЕ и высшее, приводим их к Однородности"""
def education_types():   
    for i in range(len(df['education_id'])):
        if df['education_id'][i] == 0:
            df['education'][i] = str.lower(df['education'][i]) 
        if df['education_id'][i] == 1:
            df['education'][i] = str.lower(df['education'][i]) 
        if df['education_id'][i] == 2:
            df['education'][i] = str.lower(df['education'][i]) 
        if df['education_id'][i] == 3:
            df['education'][i] = str.lower(df['education'][i])  
        if df['education_id'][i] == 4:
            df['education'][i] = str.lower(df['education'][i]) 

    counter_types = df.value_counts("education")
    print(counter_types)
    return df





fixyears()
fix_salary()
education_types()
credit_types()

# РЕЗУЛЬТАТ ОБРАБОТКИ.
print(df) 

# НА ЗАЩИТЕ ПРОЕКТА ЭТО ФУНКЦИЮ ПОКАЗЫВАТЬ ОТДЕЛЬНО. ТАК КАК ОНА УДАЛЯЕТ ДАННЫЕ И СОЗДАЕТ НОВУЮ ТАБЛИЦУ. И МЫ НЕ МОЖЕМ ПОКАЗАТЬ РЕЗУЛЬТАТ
# ЭТОЙ ФУНКЦИИ НА ОСНОВНОЙ ТАБЛИЦЕ



















"""ANALYS"""



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



'''ЗАДАНИЕ (Есть ли связь между наличием детей и возвратом кредита в срок?)'''

child0 = 0
child1 = 0
child2 = 0
child3 = 0
child4 = 0
count_no_debt0 = 0
count_no_debt1 = 0
count_no_debt2 = 0
count_no_debt3 = 0
count_no_debt4 = 0

# Этот цикл перебирает детей и долги

for i in range(len(df)):
    if df['children'][i] == 0:
        child0 += 1
        if df['debt'][i] == 0:
            count_no_debt0 += 1
    if df['children'][i] == 1:
        child1 += 1
        if df['debt'][i] == 0:
            count_no_debt1 += 1
    if df['children'][i] == 2:
        child2 += 1
        if df['debt'][i] == 0:
            count_no_debt2 += 1
    if df['children'][i] == 3: 
        child3 += 1
        if df['debt'][i] == 0:
            count_no_debt3 += 1    
        
    if df['children'][i] == 4:
        child4 += 1
        if df['debt'][i] == 0:
            count_no_debt4 += 1
# Этот код просто высчитывает процент тех у кого нет долгов
# Но код может не работать.Потому что в child может быть 0. А на 0 делить нельзя
# Если такая ошибка будет при тесте то я оставлю код в самом низу
# Но этой ошибки не должно быть если в таблице, есть клиент с 4 детьми
percent0 = (count_no_debt0/child0)*100
percent1 = (count_no_debt1/child1)*100
percent2 = (count_no_debt2/child2)*100
percent3 = (count_no_debt3/child3)*100
# percent4 = (count_no_debt4/child4)*100

print(str(percent0) + '% клиентов у которых 0 детей, НЕ ИМЕЮТ долги')
print(str(percent1) + '% клиентов у которых 1 детей, НЕ ИМЕЮТ долги')
print(str(percent2) + '% клиентов у которых 2 детей, НЕ ИМЕЮТ долги')
print(str(percent3) + '% клиентов у которых 3 детей, НЕ ИМЕЮТ долги\n' )
# print(str(percent4) + '% клиентов у которых 4 детей, НЕ ИМЕЮТ долги')

# При такой ошибке попробуйте это:
# try:
#     percent0 = (count_no_debt0/child0)*100
#     percent1 = (count_no_debt1/child1)*100
#     percent2 = (count_no_debt2/child2)*100
#     percent3 = (count_no_debt3/child3)*100
#     percent4 = (count_no_debt4/child4)*100
# except:
    # pass

'''КОНЕЦ ЗАДАНИЯ (Есть ли связь между наличием детей и возвратом кредита в срок?)'''




''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''




'''ЗАДАНИЕ (Есть ли связь между семейным положением клиента и возвратом его или ее кредита с срок)'''
married = 0
single = 0

no_debt_married = 0
no_debt_single = 0

# Проверка семейных пар у которых нет долгов

for i in range(len(df)):
    # ЖЕНАТЫЕ(0) ИЛИ В ГРАЖДАНСКОМ БРАКЕ(1)
    if df['family_status_id'][i] == 0 or df['family_status_id'][i] == 1:
        # КЛИЕНТЫ В БРАКЕ.
        married += 1
        if df['debt'][i] == 0:
            no_debt_married += 1
    
    if df['family_status_id'][i] == 2 or df['family_status_id'][i] == 3 or df['family_status_id'][i] == 4 :
        # ВДОВА/ВДОВЕЦ(2) ИЛИ НЕ ЗАМУЖЕМ/ЖЕНАТ(4) ИЛИ В РАЗВОДЕ(3)
        single += 1
        if df['debt'][i] == 0:
            no_debt_single += 1

# Высчитывает процент возвращаемости кредита одиноких клиентов и клиентов в браке
percent_married = (no_debt_married/married) * 100
percent_single = (no_debt_single/single) * 100

print(str(percent_married) + '% людей в браке не имеют долгов')
print(str(percent_single) + '% одиноких людей не имеют долгов\n')

''' КОНЕЦ ЗАДАНИЯ (Есть ли связь между семейным положением клиента и возвратом его или ее кредита с срок)'''



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



'''ЗАДАНИЕ (Влиеят ли уровень дохода на возврат кредита в срок?)'''


# ОКРУГЛЯЕМ ЗНАЧЕНИЯ  total_income  и  сохраняем их в таблице
round_up_salary = round(df['total_income'])
df['total_income'] = round_up_salary

# НАХОДИМ СРЕДНЮЮ ЗАРПЛАТУ ИЗ ВСЕХ В СТОЛБЦЕ total_income
tot_inc = df.mean(axis=0)
average_salary = tot_inc['total_income']

# Пустые переменные для подсчета 
# Число богатых у которых есть долги
rich_no_debt = 0
# Число бедных у которых есть долги
poor_no_debt = 0

# Общее число бедных и богатых клиентов 
count_rich = 0
count_poor = 0

for i in range(len(df['total_income'])):
    # Проверка для богатых
    if df['total_income'][i] > average_salary:
        count_rich +=1
        if df['debt'][i] == 0:
            rich_no_debt += 1
    
    # Проверка для бедных
    if df['total_income'][i] < average_salary:
        count_poor += 1
        if df['debt'][i] == 0:
            poor_no_debt += 1
        
rich_relation = (rich_no_debt/count_rich)*100
poor_relation = (poor_no_debt/count_poor)*100

print('\nПроцент богатых не имеющих долгов '+ str(rich_relation))
print('Процент бедных не имеющих долгов '+str(poor_relation))
if rich_relation>poor_relation:
    print('Статистика показывает, что отношение богатых не имеющих долг больше чем бедных не имеющих долг,\
 соответственно вероятнее всего доход человека напрямую влияет на факт погашения кредита в срок\n')
else:
    print('Доход человека не влияет на факт погашения кредита в срок\n')



'''КОНЕЦ ЗАДАНИЯ (Влиеят ли уровень дохода на возврат кредита в срок?)'''






''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



'''ЗАДАНИЕ (Какие типы кредитов больше всего возвращаются в срок)'''

forwed = ['свадьба','на проведение свадьбы','сыграть свадьбу']

foreduc = ['заняться высшим образованием','дополнительное образование','высшее образование','образование','получение дополнительного образования',\
    'получение образования','профильное образование','получение высшего образования','заняться образованием']

forcar = ['на покупку своего автомобиля','автомобиль','сделка с автомобилем','сделка с подержанным автомобилем','автомобили',\
    'свой автомобиль','на покупку подержанного автомобиля','на покупку автомобиля','приобретение автомобиля']

forbus = ['покупка жилой недвижимости','операции с недвижимостью','покупка недвижимости','операции с коммерческой недвижимостью','строительство собственной недвижимости','недвижимость',\
    'операции со своей недвижимостью','строительство недвижимости','покупка коммерческой недвижимости']

forlive = ['операции с жильем','покупка жилья для сдачи','жилье','покупка своего жилья','покупка жилья','покупка жилья для семьи','ремонт жилью','строительство жилой недвижимости']

for i in range(len(df['education'])):
    if df['purpose'][i] in foreduc:
        df['purpose'][i] = 'для образования'
    if df['purpose'][i] in forwed:
        df['purpose'][i] = 'для свадьбы'
    if df['purpose'][i] in forcar:
        df['purpose'][i] = 'для автомобиля'
    if df['purpose'][i] in forlive:
        df['purpose'][i] = 'для жилья'
    if df['purpose'][i] in forbus:
        df['purpose'][i] = 'для недвижимости'
    for i in df.columns:
        if df[i].dtypes == 'object':
            num = i 
            a = df[i].unique()

feduc = 0
fbus = 0
fhome = 0
fcar = 0
fwed = 0
# Те кто взял кредит на свадьбу
net_dolga1 = 0

# Те кто взял кредит на жилье
net_dolga2 = 0

# Те кто взял кредит на недвижимость
net_dolga3 = 0

# Те кто взял кредит на автомобиль
net_dolga4 = 0

# Те кто взял кредит на образование 
net_dolga5 = 0


for i in range(len(df['purpose'])):
    if df['purpose'][i] == 'для свадьбы':
        fwed += 1
        if df['debt'][i] == 0:
            net_dolga1 += 1
        
    if df['purpose'][i] == 'для жилья':
        fhome += 1
        if df['debt'][i] == 0:
            net_dolga2 += 1
        

    if df['purpose'][i] == 'для недвижимости':
        fbus += 1
        if df['debt'][i] == 0:
            net_dolga3 += 1
        
    if df['purpose'][i] == 'для автомобиля':
        fcar += 1
        if df['debt'][i] == 0:
            net_dolga4 += 1
        
    if df['purpose'][i] == 'для образования':
        feduc += 1
        if df['debt'][i] == 0:
            net_dolga5 += 1

# Подсчитываем проценты на разные виды кредитов 
percent5 = (net_dolga5/feduc)* 100
percent4 = (net_dolga4/fcar)* 100
percent3 = (net_dolga3/fbus)* 100
percent2 = (net_dolga2/fhome)* 100
percent1 = (net_dolga1/fwed)* 100

# Показываем на экран, и делаем выводы
print(str(percent1)+ '% возвращаемость кредита на свадьбу')
print(str(percent2)+ '% возвращаемость кредита на жилье')
print(str(percent3)+ '% возвращаемость кредита на недвижимость')
print(str(percent4)+ '% возвращаемость кредита на автомобиль')
print(str(percent5)+ '% возвращаемость кредита на образование\n')

'''КОНЕЦ ЗАДАНИЯ (Какие типы кредитов больше всего возвращаются в срок)'''