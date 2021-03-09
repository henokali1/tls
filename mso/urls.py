from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard.html'),
    path('new_mso', views.new_mso, name='new_mso.html'),
    path('all_msos', views.all_msos, name='all_msos.html'),
]
