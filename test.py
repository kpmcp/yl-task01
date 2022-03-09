import requests
from pprint import pprint

API = 'http://127.0.0.1:5000/api/v2'

# pprint(requests.get(f"{API}/news").json())

# pprint(requests.post(f"{API}/news", json={
#     'title': 'asda',
#     'content': 'asdasdasdas',
#     'user_id': 1,
#     'is_published': True,
#     'is_private': False
# }).json())
# pprint(requests.get(f"{API}/news").json())

# for i in range(5):
#     pprint(requests.get(f"{API}/news/{i}").json())

# pprint(requests.delete(f"{API}/news/2").json())


