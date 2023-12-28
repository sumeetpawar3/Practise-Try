from .views import BlogListCreateView,BlogRetrieveUpdateDeleteView
from django.urls import path

urlpatterns = [
    path('Blogapi/',BlogListCreateView.as_view()),
    path('Blogapi/<int:pk>/',BlogRetrieveUpdateDeleteView.as_view())
]