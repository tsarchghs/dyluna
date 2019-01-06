from io import BytesIO
from collections import OrderedDict
from jinja2 import Template

def get_url_parameters(url):
	params = {}
	val = ""
	start = False
	url_parts = [url_part for url_part in url.split("/") if url_part]
	partN = 0
	for url_part in url_parts:
		if url_part:
			if url_part[0] == "<" and url_part[-1] == ">":
				params[partN] = url_part[1:-1]
			partN += 1
	return params

def get_url_arguments(url,params):
	param_arg = {}
	url_parts = [url_part for url_part in url.split("/") if url_part]
	partN = 0;
	for location,parameter in params.items():
		try:
			param_arg[parameter] = url_parts[location]
		except IndexError:
			return 1
	return param_arg

def abort(environ,start_response,error,message):
	start_response('{} OK'.format(error), [('Content-Type', 'text/html')])
	return bytes("{}".format(message).encode("utf-8"))

def render_template(path,context):
	html = open("templates/{}".format(path),"r").read()
	template = Template(html)
	template = template.render(**context)
	return [bytes(template.encode("utf-8"))]

class Dyluna():
	def __init__(self):
		self.urls = []
	def route(self,func):
		def func_wrapper(args):
			args["start_response"]("200 OK",[("Content-Type","text/html")])
			del args["start_response"];
			function = func(**args)
			if isinstance(function, str):
				convert = bytes(function.encode("utf-8"))
				return [convert]
			return function
		return func_wrapper
	def application(self,environ, start_response,*args,**kwargs):
		path = environ.get("PATH_INFO","")
		args = OrderedDict()
		args["environ"] = environ
		args["start_response"] = start_response
		for regex,callback in self.urls:
			if regex == path:
				#l = int(environ.get('CONTENT_LENGTH'))
				#print(environ['wsgi.input'].read(l))
				return callback(args)
			elif "<" in regex and ">" in regex:
				params = get_url_parameters(regex)
				param_arg = get_url_arguments(path,params)
				if param_arg != 1:
					for param,arg in param_arg.items():
						args[param] = arg
					return callback(args)
		return abort(environ,start_response,404,"Page not found!")
	def run(self,host="127.0.0.1",port=8080):
		from paste import httpserver
		httpserver.serve(self.application,host=host,port=port)