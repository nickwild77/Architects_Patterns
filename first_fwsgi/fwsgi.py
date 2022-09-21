from views import not_found_404_view


class Application:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        """
            :param environ: словарь данных от сервера
            :param start_response: функция для ответа серверу
        """
        print('working...')
        path = environ['PATH_INFO']
        if path in self.routes:
            view = self.routes[path]
        else:
            view = not_found_404_view
        request = {}
        # front controller
        for front in self.fronts:
            front(request)

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode()]
