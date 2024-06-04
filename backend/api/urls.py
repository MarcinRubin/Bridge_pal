from rest_framework import routers
from django.urls import path
from .views import PlayerViewSet, DealViewSet, ScoreViewSet, PairingViewSet, \
    GameViewSet, MovementViewSet

router = routers.DefaultRouter()
router.register(r"players", PlayerViewSet)
router.register(r"deals", DealViewSet)
router.register(r"scores", ScoreViewSet)
router.register(r"pairings", PairingViewSet)
router.register(r"games", GameViewSet)
router.register(r"movements", MovementViewSet)

# urlpatterns =[
#     path("setup/", MovementList.as_view(), name="movement-list")
# ]

urlpatterns = router.urls
