from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_services,name='show_services'),
    path('add_services/', views.add_services,name='add_services'),
    path('edit_services/<int:pk>', views.edit_services,name='edit_services'),
    path('delete_services/<int:pk>', views.delete_services,name='delete_services'),
    path('admin_page/',views.admin_services,name='admin_page')
]
