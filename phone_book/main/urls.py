from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    # path('new_record', views.new_record),
    # path('show_tables', views.show_tables),
    path('create', views.create)
]
