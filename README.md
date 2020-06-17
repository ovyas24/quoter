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
    qoute = api()
    return render_template("index.html",quote=qoute)
~~~
I Used Template rendering by doing so we can pass data to our html page.

## *** Place your html file in templates folder ***

it should look like yourProjectFile/templates/filename.html

### Step-3: Get your self a API-Key for getting quotes

visit this site for Api key and code for implymenting that.

https://rapidapi.com/martin.svoboda/api/quotes15

After getting your code with Api-Key paste it in a python file to use it as module or use directly in main Flask App.
In My case I Made a seprate file Named api.py to test it. Later i caged it in a function *its important you convert it to function *

