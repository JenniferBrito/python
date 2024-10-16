"""
Programa que solicita os IDs dos principais artigos do momento em Hacker News.
"""

import requests
from operator import itemgetter

# Faz uma chamada de API e armazena o resto
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Processa informações sobre cada artigo submetido
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Cria uma chamada de API separada para cada artigo
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
            str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' +
                    str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }

    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), 
                          reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTítulo: {submission_dict['title']}")
    print(f"Link: {submission_dict['link']}")
    print(f"Comentários: {submission_dict['comments']}")