from django import template
from menu_app.models import Menu


register = template.Library()


@register.inclusion_tag('menu.html')
def main_menu():
    menu = Menu.objects.get(menu_label='main_menu')
    return {'menu': menu.links.order_by('priority').all()}


@register.inclusion_tag('menu.html', takes_context=True)
def user_menu(context):
    if context.request.user.is_authenticated:
        menu = [
            {
                'title': context.request.user.username,
                'url': '/profile',
            },
            {
                'title': 'Logout',
                'url': '/logout',
            },
        ]
    else:
        menu = [
            {
                'title': 'Authorization',
                'url': '/authorization',

            },
            {
                'title': 'Registration',
                'url': '/registration'
            },
        ]
    return {'menu': menu}