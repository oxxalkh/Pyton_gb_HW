"""
3.Реализовать структуру данных «Товары». Она должна представлять собой список
кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у
пользователя.

Пример готовой структуры:
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”})
,(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:
{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

goods, order = [], 1
title, price, amount, unit = None, None, None, None
while True:
    if title is None:
        tmp = input('Введите наименование товара: ')
        if not tmp.isalnum():
            print('Наименование не введено. Попробуйте еще раз.')
            continue
        title = tmp
    if price is None:
        tmp = input('Введите стоимость товара: ')
        if not tmp.isdigit():
            print('Стоимость должна быть числом. Попробуйте еще раз.')
            continue
        price = int(tmp)
    if amount is None:
        tmp = input('Введите количество: ')
        if not tmp.isdigit():
            print('Количество должно быть целым числом. Попробуйте еще раз.')
            continue
        amount = int(tmp)
    if unit is None:
        tmp = input('Введите единицы измерения: ')
        if not tmp.isalpha():
            print('Единицы изменерения не введены. '
                  'Попробуйте еще раз.')
            continue
        unit = tmp
    goods.append(
        (order, dict(title=title, price=price, amount=amount, unit=unit)))
    title, price, amount, unit = None, None, None, None
    order += 1
    q = input('Формирование списка завершено? (y/N)) ')
    if q.lower() == 'y':
        break
print(goods)
analitics = dict(title=[], price=[], amount=[], unit=[])
for _, item in goods:
    analitics['title'].append(item['title'])
    analitics['price'].append(item['price'])
    analitics['amount'].append(item['amount'])
    analitics['unit'].append(item['unit'])
print(analitics)
