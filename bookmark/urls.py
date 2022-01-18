from django.urls import path
from . import views

app_name = "bookmark"

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:pk>/', views.cate_detail, name='cate_detail'),
    path('cate_new/', views.cate_new, name='cate_new'),
    path('<int:pk>/cate_edit/', views.cate_edit, name='cate_edit'),
    path('<int:pk>/cate_delete/', views.cate_delete, name='cate_delete'),
    path('mark_new/', views.mark_new, name='mark_new'),
    path('<int:pk>/mark_edit/', views.mark_edit, name='mark_edit'),
    path('<int:pk>/mark_delete/', views.mark_delete, name='mark_delete'),
]
