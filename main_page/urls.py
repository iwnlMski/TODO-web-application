from django.urls import path
from main_page import views

app_name = 'main_page'
urlpatterns = [
    path('', views.index, name='index'),
    path('anothersite', views.test, name='test'),
    path('listtasks', views.show_tasks, name='show_tasks'),
    path('sharebundle', views.share_bundle, name='share_bundle'),
]
