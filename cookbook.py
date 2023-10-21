
def my_cook_book():
    from pprint import pprint
    with open("recipes.txt", encoding="utf-8") as file:
        cook_book = {}
        for line in file.read().split("\n\n"):
            meal_name, *ingredients = line.split("\n")
            cook_lst = []
            for ingredient in ingredients.split[1:]:
                ingredient_name, quantity, measure = ingredient.split(" / ")
                cook_lst.append(
                    {
                        "ingredient_name": ingredient_name,
                        "quantity": int(quantity),
                        "measure": measure,
                    }
                )
            cook_book[meal_name] = cook_lst
        del cook_book ["Фахитос"]
    print(f"my_cook_book = {cook_book}")


cook_book = my_cook_book()

def get_shop_list_by_dishes(dishes, person_count):
    counted_list = {}
    for dish, ingredients in cook_book.items():
        count = {}
        if dish in dishes:
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                count = {ingredient_name: {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}}
            return count
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
  



