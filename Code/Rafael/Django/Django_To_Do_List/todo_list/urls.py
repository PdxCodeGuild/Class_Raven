from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<item_id>', views.delete, name='delete'),
    path('crossoff/<item_id>', views.cross_off, name='cross_off'),
    path('uncross/<item_id>', views.uncross, name='uncross'),
    path('created/<item_id>', views.created, name='created'),
    path('priority/<item_id>', views.priority, name='priority'),
]
