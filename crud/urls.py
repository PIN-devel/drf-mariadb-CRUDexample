from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

#viewsets
router = DefaultRouter()
router.register('viewset',views.ArticleViewSet)

urlpatterns = [
    path('',include(router.urls))
    # path('', views.read_or_create),
    # path('<int:id>/', views.update_or_delete)
]
