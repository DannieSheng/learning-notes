## Links to useful information
[course on udemy](https://www.udemy.com/course/rest-api-flask-and-python/learn/lecture/5960090?start=675#notes)
[e-book](https://rest-apis-flask.teclado.com/)
[course code repo](https://github.com/tecladocode/rest-apis-flask-python)
[course discord community](https://discord.gg/78Nvd3p)
[python-refresher](https://github.com/tecladocode/python-refresher)
[Formatting Numbers for Printing in Python](https://blog.teclado.com/python-formatting-numbers-for-printing/)

## Create an REST API
### Initial set-up for a Flask app
1. Environment：
`python3.10 -m venv .venv`
2. Activate
`source venv/bin/activate` or `. venv/bin/activate`
3. Basic app.py file  
`
from flask import Flask
app = Flask(__name__)
`

### First REST API endpoint (flask function)
When we return a Python dictionary in a Flask route, Flask automatically **turns it into JSON**. 
- Change Python keywords and values so that they match the JSON standard (e.g. `True` to `true`)
- Turn the whole thing into a single **string** that API can return 

### Test (接口测试)
1. Automated testing using Insomnia client

### Docker
How to run a Flask app in a Docker container
1. Create a Dockerfile
2. `docker build -t rest-apis-flask-python .`
3. Run image either in app or in command line:
` docker run -p 5005:5000 rest-apis-flask-python`