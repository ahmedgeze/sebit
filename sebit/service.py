import requests, json



def post(name,city,country):
    payload={
    "person_name": name,
    "city_name": city,
    "country_name": country
    }
    r=requests.post("https://api.myjson.com/bins",json=payload)
    x=r.text
    d=json.loads(x)
    return d


def get(link):
    r=requests.get(link)
    d=json.loads(r.text)
    return d
