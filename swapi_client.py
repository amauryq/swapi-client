import requests
import json

def get_next_page(url):
    response = requests.get(
        url,
        allow_redirects = True
    )
    response.raise_for_status()
    if response.status_code == 200:
        page = response.json()
    return page

def get_all_records(url):
    records = {}
    response = requests.get(
        url,
        allow_redirects = True
    )
    response.raise_for_status()
    if response.status_code == 200:
        records = response.json()
        results = records['results']
        next_page = records['next']
        while next_page is not None:
            page = get_next_page(next_page)
            results = results + page['results']
            next_page = page['next']
            print(next_page)
    return results

try:
    print('start')
    records = get_all_records('https://swapi.co/api/people')
    print(json.dumps(records, indent=2))
    print('size: {}'.format(len(records)))
except Exception as e:
    print(e)
finally:
    print('done')