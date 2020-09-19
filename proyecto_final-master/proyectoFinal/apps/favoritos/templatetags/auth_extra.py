from django import template


register = template.Library()


@register.filter(name='user_in')

def user_in(objects, user):
    if user.is_authenticated:
        return objects.filter(usuario=user).exists()

    return False