import requests


def get_heroes_data(heroes_list):
    response_list = list()
    for hero in heroes_list:
        response = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{hero}')

        for results in response.json()['results']:
            response_list.append(results)

            character_list = list()
            for data in response_list:
                name = data['name']
                intelligence = int(data['powerstats']['intelligence'])
                character_list.append([name, intelligence])

    sort_el_index = 1

    def sort_by_el(i):
        return i[sort_el_index]

    max_int_char = max(character_list, key=sort_by_el)
    return f"{max_int_char[0]} is the most intelligent one, his/her intelligence is {max_int_char[1]}"


print(get_heroes_data(['Hulk', 'Captain America', 'Thanos']))
