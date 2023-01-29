from pprint import pprint
with open('data.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for i in f:
        food = i.strip()
        ingredients_cont = int(f.readline())
        ingredients = []
        for i in range(ingredients_cont):
            line = f.readline().strip('')
            eat, count, metering = line.split(' | ')
            ingredients.append({'eat' : eat,'count' : count,'metering' : metering })
        f.readline()     
        cook_book[food] = ingredients
#pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    dict_dishes = {}
    for i in dishes:
        if i in cook_book:
            print(i)
            for ingridients in cook_book[i]:
                dict_dishes[ingridients['eat']] = {'count': int(ingridients['count']) * person_count, 'metering': ingridients['metering']}

    return dict_dishes

# res = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# pprint(res)