# Quoter - Flask Project

### Step-1: Install the required libraries(assuming you have already installed python-3.x.x)

Run this Command in your terminal/command line: 
~~~python
pip install requests,flask
~~~

### Step-2: Making Our Flask app

I named my file main.py and wrote a single page flask app.
~~~python
from flask import Flask,render_template

app =  Flask(__name__)


@app.route('/')
def index():
    quote = api()
    return render_template("index.html",quote=quote)
~~~
I Used Template rendering by doing so we can pass data to our html page.

#### *** Place your html file in templates folder ***

it should look like yourProjectFile/templates/filename.html

### Step-3: Get your self a API-Key for getting quotes

visit this site for Api key and code for implymenting that.

https://rapidapi.com/martin.svoboda/api/quotes15

After getting your code with Api-Key paste it in a python file to use it as module or use directly in main Flask App.
In My case I Made a seprate file Named api.py to test it. Later i caged it in a function  
#### *its important you convert it to function *
 And Make these Changes
 1. Conver the data to a json
 ~~~python
 data = response.json()
 ~~~
 2. Impliment a work limit *optional
 3. Return the quote only
 ~~~python
 return data["content"]
 ~~~

Your Code now should look like(i Implemented a word limit as there afre some big quotes)
~~~python
def api():
    limit = False
    while not limit:
        import requests

        url = "https://quotes15.p.rapidapi.com/quotes/random/"

        querystring = {"language_code":"en"}

        headers = {
            'x-rapidapi-host': "quotes15.p.rapidapi.com",
            'x-rapidapi-key': "Your-Api-Key-Here"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        if len(data["content"])<=250:
            limit = True

    return data["content"]
~~~
You can either use it directly in your main file or save it as a seprate file and add it to main file by writing this code in start of main.py file
~~~python
from api import api
~~~

### Step-4: Make a use of data on HTML page
~~~html
<!DOCTYPE html>
<html>
<head>
	<title>Quote</title>
</head>
<body>
    {{quote}} <!--The Quote is a variable send by flask app-->
</body>
</html>
~~~

 I have made a page with custome style and design with features like: 
 1. Auto refresh in 15 second
 2. A copy and Refresh button
 3. A 15 second timmer
Files present in templates folder.
## Thank You!
