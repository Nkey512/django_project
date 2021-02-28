from django.urls import path
from hello_django.calc import views


urlpatterns = [
    path('', views.index),
    path('<int:a>/<int:b>', views.index, name='calc')
]
