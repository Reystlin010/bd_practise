from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    # path('<int:pk>', views.UserDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.UserRedacting.as_view(), name='update'),
    path('<int:pk>/delete', views.UserDeleteView.as_view(), name='delete')
]   
