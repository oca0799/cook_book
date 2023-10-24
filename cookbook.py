def my_cook_book():
    from pprint import  pprint
    with open("text.txt", encoding="utf-8") as file:
        cook_book = {}
        for line in file.read().split(("\n\n")):
            #print(line)
            dish_name, *ingredients = line.split("\n")
            cook_list = []
            #print(ingredients)
            for ingredient in ingredients[1:]:
                ingredient_name, quantity, measure = ingredient.split(" | ")
                cook_list.append(
                    {
                        "ingredient_name": ingredient_name,
                        "quantity": int(quantity),
                        "measure": measure,
                    }
                )
            cook_book[dish_name] = cook_list
    return cook_book

print(my_cook_book())


def get_shop_list_by_dishes(dishes, person_count):
    new_cook = {}
    for dish, ingredients in my_cook_book().items():
        if dish in dishes:
            for ingredient in ingredients:
                name, quantity, measure = ingredient.values()
                new_cook.setdefault(name, {"measure": measure, "quantity": 0})
                new_cook[name]["quantity"] += quantity * person_count
    return  new_cook


print(get_shop_list_by_dishes(["Омлет", "Фахитос"], 2))