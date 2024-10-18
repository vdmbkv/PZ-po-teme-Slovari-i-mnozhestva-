# 1

my_dict = {'Burger King': 52.512103, "Rostic's": 52.540492, 'Phorne': 52.539108}
print("Список координатов:", my_dict)
print("Присутствующие в списке координаты:", my_dict['Phorne'])
my_dict['Apteka'] = 52.212105
print("Отсутствующие в списке координаты:", my_dict['Apteka'])
my_dict.update({'VkusnoItochka': 52.018405,
                'KroshkaKartoshka': 59.990308})
print("Список с новыми координатами", my_dict)
bakery = my_dict.pop('Phorne')
print("Удаленные координаты:", bakery)
print("Измененный словарь координатов:", my_dict)

# 2

my_set = {'Dvoyka', 2, 2, 'Dvoyka', 3, 4, False, False}
print("Набор значений из разных типов данных:", my_set)
my_set.update({5, True})
my_set.discard(False)
print("Измененное множество:", my_set)