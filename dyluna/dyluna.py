from io import BytesIO

def notfound(environ,start_response):
	start_response('404 OK', [('Content-Type', 'text/plain')])
	return [bytes(404)]

class Dyluna():
	def __init__(self):
		self.urls = []
	def route(self,func):
		def func_wrapper(environ,start_response,*args,**kwargs):
			start_response("200 OK",[("Content-Type","text/html")])
			function = func(environ,*args,**kwargs)
			if isinstance(function, str):
				convert = bytes(function.encode("utf-8"))
				return [convert]
			return function
		return func_wrapper
	def application(self,environ, start_response,*args,**kwargs):
		path = environ.get("PATH_INFO","")
		for regex,callback in self.urls:
			if regex == path:
				#l = int(environ.get('CONTENT_LENGTH'))
				#print(environ['wsgi.input'].read(l))
				return callback(environ, start_response,*args,**kwargs)
		return notfound(environ,start_response)
	def run(self,host="127.0.0.1",port=8080):
		from paste import httpserver
		httpserver.serve(self.application,host=host,port=port)
