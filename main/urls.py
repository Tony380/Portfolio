from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

]

handler404 = views.my_404_view
handler500 = views.my_500_view

app_name = 'main'