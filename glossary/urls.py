from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('metric/<int:primary_key>/', views.metric_detail_view, name='metric-detail'),
    path('metric/introduction/', views.metric_intro_view, name='metric-intro'),
    path('feature/<slug:feature_name>/', views.feature_detail_view, name='feature-detail')
  
]
urlpatterns += [
    path('register/', views.register, name='register')
]

