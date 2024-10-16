def get_recipe_and_nutrient_data():
    recipe = {}
    print('Enter an ingredient, and then its nutrient information.\n')
    print('Enter "done" when you have listed all ingredients.\n')

    while True:
        ingredient = input('Enter an ingredient (or "done" to finish): ').strip().lower()
        if ingredient == 'done':
            break

        fat = float(input(f'  Enter fat (g) for "{ingredient}": '))
        sodium = float(input(f'  Enter sodium (mg) for "{ingredient}": '))
        sugar = float(input(f'  Enter sugar (g) for "{ingredient}": '))
        fiber = float(input(f'  Enter fiber (g) for "{ingredient}": '))
        protein = float(input(f'  Enter protein (g) for "{ingredient}": '))

        recipe[ingredient] = {
            'nutrition': {
                'Fat (g)': fat,
                'Sodium (mg)': sodium,
                'Sugar (g)': sugar,
                'Fiber (g)': fiber,
                'Protein (g)': protein
            }   
        }

    return recipe


def calc_nutritional_info(recipe):
    total_nutrients = {'Fat (g)': 0, 'Sodium (mg)': 0, 'Sugar (g)': 0, 'Fiber (g)': 0, 'Protein (g)': 0}

    for ingredient in recipe.values():
        if ingredient in recipe.values():
            for nutrient in total_nutrients:
                total_nutrients[nutrient] += ingredient['nutrition'][nutrient]
    
    return total_nutrients


def run_calculation():
    print('--- Nutritional Information Calculator ---')

    recipe = get_recipe_and_nutrient_data()
    total_nutrients = calc_nutritional_info(recipe)

    serving_size = float(input(f'Enter total number of servings (in number of pieces): '))

    print('##################')
    print('##################')
    print(f'Total Nutrition Facts per serving (1 piece of {serving_size} total pieces): ')
    for nutrient, value in total_nutrients.items():
        print(f'- {nutrient.capitalize()}: {value/serving_size:.2f}')
    print('##################')
    print('##################')

run_calculation()
