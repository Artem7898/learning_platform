from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('lessons/', views.LessonListCreateView.as_view(), name='lesson-list-create'),
    path('view-history/', views.ViewHistoryListCreateView.as_view(), name='view-history-list-create'),
    path('', RedirectView.as_view(pattern_name='product-list-create', permanent=False)),
]
