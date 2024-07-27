from django.urls import path
from . import views

app_name = 'notices'

urlpatterns = [
    path('', views.notice_list_view, name='home'),
    path('<int:notice_id>/', views.notice_view, name='notice_view'),
    path('new/', views.new_notice_page, name='new_notice'),
    path('u/<str:username>/', views.user_notice_list_view, name='user_notices'),
    path('save/<int:notice_id>/', views.save_notice, name='save_notice'),
    path('remove/<int:notice_id>/', views.remove_saved_notice, name='remove_saved_notice'),
    path('saved/', views.saved_notice_list_view, name='saved_notice_list'),
]
