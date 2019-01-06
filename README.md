# Dyluna
A very simple wsgi based python web framework

Example:
```python
app = Dyluna()

@app.route
def hello(environ):
	if environ.get("REQUEST_METHOD") == "POST":
		name = environ["POST"].get("name")
		return render_template("index.html",{"name":name})
	return render_template("hello.html")
app.urls.append(["/hello",hello])

@app.route
def hello(environ,name):
	context = {"name":name}
	return render_template("hello2.html",context)
app.urls.append(["/hello/<name>",hello])

app.run()
```
hello.html
```html
<html>
<head>
	<title>Hello</title>
</head>
<body>
	{% if name %}
		<h1>Hello, {{name}}</h1>
	{% else %}
		<form method="POST">
			name: <input name="name"><br>
		<button type="submit">Submit</button>
		</form>
	{% endif %}
</body>
</html>
```
hello2.html
```html
<html>

<head>
	<title>Hello</title>
</head>
<body>
	<h1>Hello, {{name}}</h1>
</body>
</html>
```
Run the code and visit http://127.0.0.1:8080/
