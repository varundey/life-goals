from django import template

register = template.Library()

@register.filter
def count_done(value):

    try:
        completed = (100*value.filter(done=True).count()/value.count())
        return completed
    except ZeroDivisionError:
        return 0
