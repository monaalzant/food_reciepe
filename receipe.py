import requests


def recipe_search(ingredient):
    # Register to get an API key https://www.food2fork.com/about/api
    api_key = '7a7cd9b85dd6e0d516903b7c2d582bfa'
    application_id = 'a720f909'
    url = 'https://api.edamam.com/search?app_id={}&app_key={}&q={}'.format(application_id,api_key, ingredient)
    print(url)
    result = requests.get(url)
    data = result.json()
    return data['hits']


def run():
    ingredient = input('Enter an ingredient: ')
    hits = recipe_search(ingredient)
    for single_hit in hits:
        recipe_json = single_hit['recipe']
        print(recipe_json['label'])
        print(recipe_json['ingredientLines'])
        print(recipe_json['dietLabels'])

        print('----------------------------------')
run()