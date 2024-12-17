from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse
from wagtail.admin import widgets

@hooks.register('register_admin_menu_item')
def register_my_custom_menu_item():
    return MenuItem(
        'My Custom View',
        reverse('my_custom_view'),
        icon_name='folder-inverse',
        classnames='icon icon-site',
        order=10000
    )
