from django.urls import path
from . import views

urlpatterns = [
    path('', views.EntityListView.as_view(), name='entity_list'),
    path('<int:pk>/', views.EntityDetailView.as_view(), name='entity_detail'),
    path('add/', views.EntityCreateView.as_view(), name='entity_add'),
    path('<int:pk>/edit/', views.EntityUpdateView.as_view(), name='entity_edit'),
    path('<int:pk>/delete/', views.EntityDeleteView.as_view(), name='entity_delete'),
    path('activities/', views.ActivityListView.as_view(), name='activity_list'),
    path('activities/<int:pk>/', views.activity_delete, name='activity_delete'),
    path('comments/', views.CommentListView.as_view(), name='comment_list'),
    path('comments/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]