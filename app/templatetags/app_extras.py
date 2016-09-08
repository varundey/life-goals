from django import template

register = template.Library()

@register.filter
def count_done(value):
    return (100*value.filter(done=True).count()/value.count())
