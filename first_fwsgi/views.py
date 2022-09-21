from templator import render_


def index_view(request):
    print(request)
    context = {
        'title': 'Главная страница',
        'welcome': 'Добро пожаловать на главную  страницу!'
    }
    return '200 OK', render_('index.html', context)


def not_found_404_view(request):
    print(request)
    return '404 PAGE NOT FOUND', '404 PAGE NOT FOUND'


class About:

    def __call__(self, request):
        context = {
            'title': 'about',
            'about': 'about'
        }
        return '200 OK', render_('about.html', context=context)
