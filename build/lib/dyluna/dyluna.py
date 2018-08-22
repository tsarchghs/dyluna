from io import BytesIO

def notfound(environ,start_response):
	start_response('404 OK', [('Content-Type', 'text/plain')])
	return [bytes(404)]

class Dyluna():
	def __init__(self,urls):
		self.urls = urls
	def application(self,environ, start_response):
		path = environ.get("PATH_INFO","")
		for regex,callback in urls:
			if regex == path:
				#l = int(environ.get('CONTENT_LENGTH'))
				#print(environ['wsgi.input'].read(l))
				return callback(environ, start_response)
		return notfound(environ,start_response)
	def run(self,host="127.0.0.1",port=8080):
		from paste import httpserver
		httpserver.serve(self.application,host=host,port=port)
