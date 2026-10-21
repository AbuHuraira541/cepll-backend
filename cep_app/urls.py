from django.urls import path
from .views import (
    ProjectListView, ProjectDetailView,
    BlogPostListView, BlogPostDetailView,
    QuoteSubmissionViewSet, ContactMessageViewSet,
)
from rest_framework.routers import DefaultRouter

# Router setup for ViewSets
router = DefaultRouter()
router.register(r'quotes', QuoteSubmissionViewSet, basename='quotessubmission')
router.register(r'contact', ContactMessageViewSet, basename='contactmessage')

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
    path('blogs/', BlogPostListView.as_view(), name='blog-list'),
    path('blogs/<slug:slug>/', BlogPostDetailView.as_view(), name='blog-detail'),
]

# Yahan router ke URLs ko properly urlpatterns mein add kar diya gaya hai
urlpatterns += router.urls