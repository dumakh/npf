import random

class RandomEl():
    months = ['01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12']
    days   = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    years  = ['2000','1999','1998','1997','1990','1988','1985','2002','1980','1986','1987']
    rand_date = random.choice(days)+"."+random.choice(months)+"."+random.choice(years)

class ManName():
    first_names = ('Артем', 'Александр', 'Максим', 'Илья', 'Василий', 'Михаил')
    last_names = (
    'Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Соколов', 'Михайлов', 'Новиков', 'Захаров',
    'Морозов', 'Волков', 'Алексеев', 'Лебедев', 'Семенов', 'Егоров', 'Павлов', 'Козлов', 'Степанов', 'Николаев',
    'Орлов', 'Андреев', 'Макаров', 'Никитин')
    patr_names = (
    'Олегович', 'Дмитриевич', 'Константинович', 'Сергеевич', 'Алексеевич', 'Александрович', 'Кузьмич', 'Михалыч')
    rand_surname = random.choice(last_names)
    rand_name = random.choice(first_names)
    rand_patr = random.choice(patr_names)

class WomanName():
    first_names = ('Алена', 'Марина', 'Яна', 'Светлана', 'Елизавета', 'Анастасия')
    last_names = (
    'Иванова', 'Смирнова', 'Кузнецова', 'Попова', 'Васильева', 'Петрова', 'Соколова', 'Михайлова', 'Новикова',
    'Федорова', 'Морозова', 'Волкова', 'Алексеева', 'Лебедева', 'Семенова', 'Егорова', 'Павлова', 'Козлова',
    'Степанова', 'Николаева', 'Орлова', 'Андреева', 'Макарова', 'Захарова')
    patr_names = ('Дмитриевна', 'Константиновна', 'Сергеевна', 'Алексеевна', 'Александровна', 'Кузьминична')
    rand_surname = random.choice(last_names)
    rand_name = random.choice(first_names)
    rand_patr = random.choice(patr_names)