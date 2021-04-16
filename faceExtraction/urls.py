from django.urls import path
from .views import face_extraction_view

urlpatterns = [
    path('url/', face_extraction_view, name='faceExtraction')
]
