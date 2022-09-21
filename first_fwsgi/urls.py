from views import index_view, About

routes = {
    '/': index_view,
    '/about/': About()
}
