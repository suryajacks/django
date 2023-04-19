
from django.urls import path ,include
from .views import ArticlesViewSet
from rest_framework.routers import DefaultRouter

router =DefaultRouter()
router.register('articles',ArticlesViewSet, basename='articles')

urlpatterns = [
      path('',include(router.urls))
    # path('articles/', ArticleList.as_view()),
    # path('articles/<int:pk>/', ArticlesDetail.as_view()),
      
]
