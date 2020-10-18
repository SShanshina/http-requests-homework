import requests
import time


def get_questions(num_of_days):
    now = int(time.time())
    days_ago = now - (86400 * num_of_days)

    response = requests.get('https://api.stackexchange.com/2.2/questions',
                            params={
                                'fromdate': days_ago,
                                'todate': now,
                                'sort': 'creation',
                                'tagged': 'python',
                                'site': 'stackoverflow',
                            })

    for i, question in enumerate(response.json()['items']):
        title = question['title']
        tags = ', '.join(question['tags'])
        print(f'{i + 1}. {title}')
        print(f'Tags: {tags}')
        print()

    return


print(get_questions(2))
