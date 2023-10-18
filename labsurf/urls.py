from django.urls import path
from labsurf.views import index, blank, buttons, charts, elements, formu, signup, signin, tables, typography, widget

urlpatterns = [
    path('', index, name='index'),
    path('blank/', blank, name='blank'),
    path('buttons/', buttons, name='buttons'),
    path('charts/', charts, name='charts'),
    path('elements/', elements, name='elements'),
    path('formu/', formu, name='formu'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signin/', signin, name='signin'),
    path('tables/', tables, name='tables'),
    path('typography/', typography, name='typography'),
    path('widget/', widget, name='widget'),
]