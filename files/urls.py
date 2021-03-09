from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'podcasts', views.PodcastList)
router.register(r'songs', views.SongList)

urlpatterns = [
    path('overall', views.TextAPIView.as_view()),
    path('<int:pk>/', views.PodcastDetail.as_view()),
    path('', include(router.urls)),   
]
