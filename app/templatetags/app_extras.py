from django import template
# from todo.app.models import Event

register = template.Library()
# events = Event.objects.all().filter(done=True)
@register.filter
def count_done(value):
    return (100*value.filter(done=True).count()/value.count())
