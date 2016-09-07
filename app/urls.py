from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name="index"),
    url(r'^goals/$', views.goals, name='goals'),
    url(r'^add/$', views.add, name="add_new"),
    url(r'^goal/(?P<pk>\d+)/edit/$', views.goal_edit, name='goal_edit'),
    url(r'^goal/(?P<pk>\d+)/delete/$', views.goal_delete, name='goal_delete'),
    # url(r'^delete/(?P<pk>\d+)/$', 'app.views.GoalDelete.as_view()', name="delete_goal")
]
