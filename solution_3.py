import requests
from datetime import datetime

def _questions_request():
    current_date = int(datetime.now().timestamp())
    two_day_ago = int(current_date - 172800)
    url = "https://api.stackexchange.com/2.3/questions?fromdate={}&todate={}&order=desc&sort=" \
          "activity&tagged=Python&site=stackoverflow".format(two_day_ago, current_date)
    response = requests.get(url=url)
    return response.json()

def find_questions():
    dict_of_quests = {}
    link = _questions_request()
    for item in link['items']:
        dict_of_quests[item['title']] = item['link']

    return dict_of_quests


