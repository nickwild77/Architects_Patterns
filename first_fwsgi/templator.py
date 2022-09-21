from jinja2 import Template
import os


def render_(template_name, context, folder='templates', **kwargs):
    """
    :param template_name: имя шаблона
    :param context: словарь с переменными для шаблона
    :param folder: папка в которой ищем шаблон
    :param kwargs: параметры
    :return:
    """
    file_path = os.path.join(folder, template_name)
    # Открываем шаблон по имени
    with open(file_path, encoding='utf-8') as f:
        # Читаем
        template = Template(f.read())
    # рендерим шаблон с параметрами
    return template.render(context, **kwargs)
