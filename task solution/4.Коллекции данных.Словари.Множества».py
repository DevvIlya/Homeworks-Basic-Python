#Задание № 1

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
visit = [geo_log for geo_log in geo_logs if "Россия" in next(iter(geo_log.values()))]
print()
print(visit)
print()


#Задание № 2

from itertools import chain
 
ids = {'user1': [213, 213, 213, 15, 213],
'user2': [54, 54, 119, 119, 119],
'user3': [213, 98, 98, 35]} 
result = list(dict.fromkeys(chain(*ids.values())).keys())
print()
print(result)
print()


#Задание № 3

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

storage = {}

for query in queries:
    words = query.split()

    if len(words) in storage.keys():
        storage[len(words)] += 1
    else:
        storage.update({
            len(words): 1
        })

for key, value in storage.items():
    percentage = round((value / len(queries)) * 100, 2)
    print(f'Поисковых запросов из {key} слова: {percentage}% ({value} запр.)')
print()


#Задание № 4

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
print(max(stats, key=stats.get))
print()


#Задание № 5 (дополнительное)

from itertools import zip_longest

l = ['2018-01-01', 'yandex', 'cpc', 100]

for z in zip_longest(*[iter(l)] * 4):
    first, second, third, forth = z
    print({first:{second:{third:forth}}})