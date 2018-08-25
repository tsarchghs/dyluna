# Dyluna
A very simple wsgi based python web framework

Example:
```python
from dyluna.dyluna import Dyluna
from dyluna.dyluna import render_template

app = Dyluna()

@app.route
def helloworld(environ):
    return "Hello world"
app.urls.append(["/helloworld",helloworld]) #Route "/helloworld" will call helloworld view

@app.route
def index(environ):
    return render_template("index.html") #it will look for templates/index.html
app.urls.append(["/",index]) #Route "/" will call index view

app.run() #default port 8080
```	
Run the code and visit http://127.0.0.1:8080/
