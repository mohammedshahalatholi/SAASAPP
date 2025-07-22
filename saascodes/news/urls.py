from django.urls import path
from . import views
urlpatterns = [
    path('', views.finance_news,name='finance_news')
]