import requests

url = "https://api.yelp.com/v3/businesses/search"
# API keys are like passwords. You should protect them at all cost.
# Try to add them to a separated file to deal with ir when necessary
api_key = "NoKg_9ZmKnJ2YJCKE6Vo1ubQpH8trH7_Tgz_oCQsljgTQ-A42r_fKjaZAKqsRD025xChQfFC01o5VUZNSpGa1bhqIYxakWvCWm26WBrM4TZ_QgwgsZzDfppa6cOxYnYx "

headers = {
    "Authorization": "Bearer " + api_key
}

params = {
    "term": "Sushi",
    "location": "Nagoya"
}

response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
name = [business["name"] for business in businesses if business["rating"] > 4]
print(name)

