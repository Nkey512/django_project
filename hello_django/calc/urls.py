from django.urls import path
from hello_django.calc import views


urlpatterns = [
    path('', views.index),
    path('history/', views.history),
    path('<int:a>/<int:b>', views.Calc.as_view(), name='calc')
]
