from django import template

register = template.Library()

@register.filter(name='cutwords')
def cutwords(value,arg):
    """
    This cuts all values or 'arg' from string
    """
    return value.replace(arg,'')


# register.filter('cut',cut)
