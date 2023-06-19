recipe = []

while True:
    ingredient = input('ингридиент:')
    if ingredient == '':
        break
    if "лук" in ingredient:
        continue
    recipe.append(ingredient)

print(*recipe)