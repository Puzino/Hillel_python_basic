# Тема: Методы словарей
# Генератор словарей

symbols = {symbol: ord(symbol) for symbol in 'eyuioa'}
print(symbols)

# Словарь
persons = {'John': 12,
           'Jack': 34,
           'Anya': 27
           }
print(persons)

# Добавление к словарю
persons['Jackob'] = 34
# persons.clear() #Удаляет словарь
# persons = {} - пустой словарь
print(persons.get('Vova', 1000))
result = 'Anya' in persons  # in проверяет только ключи.
print(result)

key = 'Vova'  # Ключ, меняется
if key not in persons:
    persons[key] = 41
print(persons)

for key in persons:
    print(key, persons[key])

# items, key, values

# items
for key, value in persons.items():
    print(key, value)

# keys
# print(type(persons.keys()), persons.keys())
# print(type(persons.values()), persons.values())

max_age = max(persons.values())
print(persons)
print(max_age)

# pop - действует как в списке, тут передаем ключ который удаляем, теряется вся пара, удаляет по ключу
for key in persons:
    print(key, persons[key])
value = persons.pop('Jackob')
print('>>>>>>>>', value)
for key, value in persons.items():
    print(key, value)
print(persons)

# popitem - удаляет какой-то элемент
# dict.clear() - очищает словарь.
#
# dict.copy() - возвращает копию словаря.
#
# classmethod dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).
# dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).
#
# dict.items() - возвращает пары (ключ, значение).
#
# dict.keys() - возвращает ключи в словаре.
#
# dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).
#
# dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.
#
# dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default (по умолчанию None).
#
# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
#
# dict.values() - возвращает значения в словаре.
# persons = {'John': 12, 'Jack': 34}
# persons_other = {'Anna': 42, 'Jack': 64}

# persons = {}
# persons_result = persons.update(persons)
# persons_result.update(persons_other)  # dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
# print(persons_result)
# max_age = max(persons_result.values())
# print(max_age)
# print(max(list(persons.values()) + list(persons_other.values())))
# persons_result = {**persons, **persons_other}  # распаковка словарей
# print(persons_result, persons)


# список однотипных словарей
products = [{'name': 'water', 'price': 12, 'title': 'bonaqua'},
            {'name': 'bread', 'price': 9, 'title': 'WhileBread'},
            {'name': 'bread', 'price': 7, 'title': 'baton'},
            {'name': 'apple', 'price': 25, 'title': 'golden'}]


bread_price = []
for product in products:
    # print(product['title'])
    # product['sale'] = True
    if product ['name'] == 'bread':
        # print(product['price'])
        # bread_price.append(product['price'])
        product['price'] = product['price'] * 1.1 - 1
print(products)


# дз №1.1 писать в виде генератора списков, создать список возрастов для него, с помощью min, а дальше как делали с хелобом (если age = min(age)
# дз №1.3