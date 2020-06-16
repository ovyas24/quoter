def api():
    import requests

    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    querystring = {"language_code":"en"}

    headers = {
        'x-rapidapi-host': "quotes15.p.rapidapi.com",
        'x-rapidapi-key': "5b9fba41ddmsh2f2caea5dd3684bp13a7a2jsna70b2449b028"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    return data["content"]