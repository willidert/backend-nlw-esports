from .views import GameViewSet, AdViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'games', GameViewSet, basename='game')
router.register(r'ads', AdViewSet, basename='ads')

urlpatterns = router.urls
