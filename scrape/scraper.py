from bs4 import BeautifulSoup
import requests

def scrapeI(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features='lxml')
    ingredient_map = {
        'skinless chicken thighs': 'chicken',
        'ground chicken': 'chicken',
        'chicken thigh': 'chicken',
        'chicken wings': 'chicken',
        'skinless chicken breast': 'chicken',
        'skin-on chicken thighs': 'chicken',
        'chicken stock': 'chicken_broth',
        'green onion': 'scallion',
        'large eggs': 'egg',
        'large egg (':'egg',
        'large egg yolks': 'egg',
        'ramen egg': 'egg',
        'carrot': 'carrot',
        'carrot' :'carrot',
        'short-grain rice': 'rice',
        'shiitake': 'mushroom',
        'mushroom': 'mushroom',
        'beef stock': 'stock',
        'pork belly': 'pork',
        'cucumber': 'cucumber',
        'tomatoes': 'tomato',
        'thinly sliced beef': 'beef',
        'boneless beef chuck roast': 'beef',
        'beef short rib': 'beef',
        'salmon' : 'salmon',
        'shrimp': 'shrimp',
        'cabbage': 'cabbage',
        'cilantro (coriander)':'cilantro',
        'myoga ginger': 'ginger',
        'fresh ramen noodles': 'noodle',
        'udon noodles': 'noodle',
        'dried somen noodles': 'noodle',
        'yakisoba': 'noodle',
        'onion': 'onion',
        'mitsuba': 'parsley',
        'pork': 'pork',
        'russet': 'potato',
        'short-grain': 'rice',
        'sushi rice': 'rice'
    }

    # ingredients_list = ['apple', 'background', 'beef', 'cabbage', 'carrot', 'chicken', 'chicken_broth', 'chili', 
    # 'cilantro', 'coriander', 'cucumber', 'egg', 'fish', 'garlic', 'ginger', 'honey', 'lemon', 'lime', 'milk', 'mushroom', 
    # 'noodle', 'olive', 'onion', 'orange', 'parsley', 'peanut', 'pork', 'potato', 'rice', 'salmon', 'scallion', 'shrimp', 
    # 'stock', 'tomato', 'yoghurt']



    ingredient_html = soup.find_all('span', class_="wprm-recipe-ingredient-name")
    ingredient_name = [ next((replacement for keyword, replacement in ingredient_map.items() if keyword in igrd.text.lower()), igrd.text.lower())
    for igrd in ingredient_html]

    return ingredient_name
    

def scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features='lxml')


    title = soup.find('h2', class_="wprm-recipe-name").text
    #print(title)

    # rating out of 5
    rating = soup.find('span', class_="wprm-recipe-rating-average").text

    #print(rating)

    # time hours, minutes
    time_h_html = soup.find('span', class_="wprm-recipe-details wprm-recipe-details-hours wprm-recipe-total_time wprm-recipe-total_time-hours")
    time_m_html = soup.find('span', class_="wprm-recipe-details wprm-recipe-details-minutes wprm-recipe-total_time wprm-recipe-total_time-minutes")

    time_h = None
    time_m = None
    if time_h_html is None:
        time_h = ''
    else:
        time_h = time_h_html.text

    if time_m_html is None:
        time_m = ''
    else:
        time_m = time_m_html.text

    #print( time_h + ' ' + time_m)


    servings = soup.find('span', class_='wprm-recipe-servings').text.strip()
    #print(servings)

    # ingreident name, amount, unit
    ingredients = soup.find_all('li', class_="wprm-recipe-ingredient")

    ingredient_map = {
        'skinless chicken thighs': 'chicken',
        'ground chicken': 'chicken',
        'chicken thigh': 'chicken',
        'chicken wings': 'chicken',
        'skinless chicken breast': 'chicken',
        'skin-on chicken thighs': 'chicken',
        'chicken stock': 'chicken_broth',
        'green onion': 'scallion',
        'large eggs': 'egg',
        'large egg (':'egg',
        'large egg yolks': 'egg',
        'ramen egg': 'egg',
        'carrot': 'carrot',
        'carrot' :'carrot',
        'short-grain rice': 'rice',
        'shiitake': 'mushroom',
        'mushroom': 'mushroom',
        'beef stock': 'stock',
        'pork belly': 'pork',
        'cucumber': 'cucumber',
        'tomatoes': 'tomato',
        'thinly sliced beef': 'beef',
        'boneless beef chuck roast': 'beef',
        'beef short rib': 'beef',
        'salmon' : 'salmon',
        'shrimp': 'shrimp',
        'cabbage': 'cabbage',
        'cilantro (coriander)':'cilantro',
        'myoga ginger': 'ginger',
        'fresh ramen noodles': 'noodle',
        'udon noodles': 'noodle',
        'dried somen noodles': 'noodle',
        'yakisoba': 'noodle',
        'onion': 'onion',
        'mitsuba': 'parsley',
        'pork': 'pork',
        'russet': 'potato',
        'short-grain': 'rice',
        'sushi rice': 'rice'
    }

    ingredient_html = soup.find_all('span', class_="wprm-recipe-ingredient-name")
    ingredient_name = [ next((replacement for keyword, replacement in ingredient_map.items() if keyword in igrd.text.lower()), igrd.text.lower())
    for igrd in ingredient_html]
    #print(ingredient_name)

    ingredient_amount_html = [igrd.find('span', class_= "wprm-recipe-ingredient-amount") for igrd in ingredients]
    ingredient_amount = []
    for igrd in ingredient_amount_html:
        if igrd is None:
            ingredient_amount.append('')
        else:
            ingredient_amount.append(igrd.text)
    #print(ingredient_amount)

    ingredient_unit_html = [igrd.find('span', class_="wprm-recipe-ingredient-unit") for igrd in ingredients]
    ingredient_unit = []
    for igrd in ingredient_unit_html:
        if igrd is None:
            ingredient_unit.append('')
        else:
            ingredient_unit.append(igrd.text)
    #print(ingredient_unit)

    instructions_html = soup.find_all('div', class_="wprm-recipe-instruction-text")
    instructions = [instr.text for instr in instructions_html[1:]]
    #print(instructions)

    recipe_data = {
        'title': title,
        'rating': rating,
        'servings': servings,
        'time_h': time_h,
        'time_m': time_m,
        'ingredient_name': ingredient_name,
        'ingredient_amount': ingredient_amount,
        'ingredient_unit': ingredient_unit,
        'instructions': instructions
    }

    return recipe_data

#print(recipe_data)






