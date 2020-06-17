def api():
    limit = False
    while not limit:
        import requests

        url = "https://quotes15.p.rapidapi.com/quotes/random/"

        querystring = {"language_code":"en"}

        headers = {
            'x-rapidapi-host': "quotes15.p.rapidapi.com",
            'x-rapidapi-key': "YOUR-API-KEY-HERE"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        if len(data["content"])<=250:
            limit = True

    return data["content"]
