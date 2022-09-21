from wsgiref.simple_server import make_server

from fwsgi import Application
from fronts_middleware import main_front, second_front
from urls import routes

fronts = [main_front, second_front]
application = Application(routes, fronts)

with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
