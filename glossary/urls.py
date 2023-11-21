from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('metric/<int:primary_key>', views.metric_detail_view, name='metric-detail'),
    path('metrics/', views.metric_intro_view, name='metric-intro')
  
]
urlpatterns += [
    path('register/', views.register, name='register')
]

