from django import template

register = template.Library()

@register.filter
@register.filter(name='img_path_remove_code')
def img_path_remove_code(value):
    return value.replace("/code","")