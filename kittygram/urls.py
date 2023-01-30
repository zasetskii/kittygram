from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cats.views import CatList, CatDetail, CatViewSet

router = DefaultRouter()
router.register('cats', CatViewSet)

urlpatterns = [
    path('', include(router.urls))
]
