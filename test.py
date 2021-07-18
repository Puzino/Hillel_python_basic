persons = [{'John': 12, 'Jack': 34}]
persons_other = {'Anna': 42, 'Jack': 64}

# persons = {}
# persons_result = persons.update(persons)
# persons_result.update(persons_other)  # dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
# print(persons_result)
max_age = max(persons.values())
print(max_age)
print(max(list(persons.values()) + list(persons_other.values())))
persons_result = {**persons, **persons_other}  # распаковка словарей
print(persons_result, persons)
